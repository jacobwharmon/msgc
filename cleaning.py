import pandas as pd
import pyreadstat
import numpy as np
import os
import matplotlib.pyplot as plt

from msgc_tools import variables_dict # dict definining a particular subset of columns, as well as their integer to category label mappings (default behavior is the '01_22' version)
variables_dict_01_22 = variables_dict('01_22')
variables_dict_91_00 = variables_dict('91_00') 

from msgc_tools import county_types # dict segmenting counties into metropolitan, micropolitan, and rural
from msgc_tools import statute_codes # dict of long description forms of the numeric statutes

DATA_PATH = "..\\data\\UMN Data\\"

# LOAD THE RAW DATA ----------------------------------------------------------------------------------------------------------------------------------
### 01-22 raw data ---------------
raw_data_01_22, meta_data_01_22 = pyreadstat.read_sav(f"{DATA_PATH}File01_22.sav")

# keeping subset of variables
df_01_22 = raw_data_01_22[[*variables_dict_01_22.keys()]].copy()

# mapping integer categories to their string counterparts
for var, info in variables_dict_01_22.items():
    if info['levels'] is not None:
        df_01_22[var] = df_01_22[var].astype(str).map(variables_dict_01_22[var]['levels'])

# everything lowercase
df_01_22 = df_01_22.map(lambda x: x.lower() if isinstance(x, str) else x)

### 91-00 raw data ---------------
raw_data_91_00, meta_data_91_00 = pyreadstat.read_sav(f"{DATA_PATH}PublicFile91_00.sav")

# keeping subset of variables
df_91_00 = raw_data_91_00[[*variables_dict_91_00.keys()]].copy()

# mapping integer categories to their string counterparts
for var, info in variables_dict_91_00.items():
    if info['levels'] is not None:
        df_91_00[var] = df_91_00[var].astype(str).map(variables_dict_91_00[var]['levels'])

# everything lowercase
df_91_00 = df_91_00.map(lambda x: x.lower() if isinstance(x, str) else x)

# Things in 91_00 data that need to change to match 01_22 data
# doff is mmddyyyy
df_91_00['doff'] = pd.to_datetime(df_91_00['doff'], format='%M%d%Y').dt.date

# rename offense to Offense, jail to prison, caseno to chargeid
df_91_00.rename(columns={'offense': 'Offense', 'caseno': 'chargeid'}, inplace=True)

# Stacking 01_22 and 91_00 data --------------
# NAs for the columns that 91_00 doesn't have
df = pd.concat([df_01_22, df_91_00], axis=0, ignore_index=True)

# Following Nick's cleaning -------------------------------------------------------------------------------------------------------------------------
df['priorfelonies'] = df['totprior'].clip(upper=10)

df['race'] = df['race'].replace('corp', np.nan).replace('unk', np.nan)

df['severity_reg'] = np.where(df['severity'].isin(['1','2','3','4','5','6','7','8','9','10','11','murder 1']), df['severity'], np.nan)
df['severity_sex'] = np.where(df['severity'].isin(['a','b','c','d','e','f','g','h','i']), df['severity'], np.nan)
df['severity_drug'] = np.where(df['severity'].isin(['d1','d2','d3','d4','d5','d6','d7','d8','d9']), df['severity'], np.nan)

df['ageoff'] = np.where(df['ageoff'] == 0, np.nan, df['ageoff'])
df['agesent'] = np.where(df['agesent'] == 0, np.nan, df['agesent'])

df['subsequent_combined'] = np.where(df[['subwpn','subsex','subdrug','subdwi','subfailr','Subburg']].eq('yes').any(axis=1), 'yes', 'no')

df['probation'] = np.select([df['typeprob'] == 'none', df['typeprob'].isin(['supervised', 'unsupervised', 'court'])],
                            ['no','yes'],
                            default = np.nan)

df['county_type'] = df['county'].map(county_types)

df['statute_long'] = df['statute'].map(statute_codes)

df['judge_id'] = (df['jfname']+'_'+df['jlname']).apply(hash)

df = df[df['sex'] != 'corp']

# Alternative measures for departures -------------------------------------------------------------------------------------------------------------------------------
# df['departure_SC'] = (df['presumpt'] == 'stay') & (df['prison'] == 'yes') # (df['departure_SC'] != (df['dispdep'] == 'aggravated')).sum() # 2518 more departure_SC's than dispdep==aggravated's

# df['departure_CS'] = (df['presumpt'] == 'commit') & (df['prison'] == 'no') # (df['departure_CS'] != (df['dispdep'] == 'mitigated')).sum() # 50 mismatches

df['departure_grid'] = np.select(condlist = [df['aggsentc'] < df['Mintime'],
                                            df['aggsentc'] > df['Maxtime']],
                                 choicelist = [df['aggsentc'] - df['Mintime'],
                                                df['aggsentc'] - df['Maxtime']],
                                 default = 0)

df['departure_presumpt'] = df['aggsentc'] - df['time']

df.to_csv(f"..\\data\\jake_files\\data_clean.csv")