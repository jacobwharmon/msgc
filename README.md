## 0) `cleaning.py` 
(`cleaning.ipynb` is just the interactive/debugging version of `cleaning.py`)
### Inputs:
* `\\data\\UMN Data\\File01_22.sav`
    * This is the raw data for 2001-2022 from the MSGC Dropbox 
* `\\data\\UMN Data\\PublicFile91_00.sav`
    * This is the raw data for 1991-2000 from the MSGC Dropbox (some differences between it and the previous data since it is 'PublicFile')
* `\\scripts\\msgc_tools.py`
    * This file defines 3 dictionary-generating functions that get used in the cleaning of the data:
        1) `variables_dict()`  
            By default, calling this function returns a dictionary for the variables we use in the 2001-2022 data. (To return a dictionary for the variables we use in the 1991-2000 data, use `variables_dict('91_00')`)
            * keys: variables that we will keep (e.g. `chargeid`, `severity`, `district`, ...)
            * values: 
                * description: description of the variable obtained from the .sav file metadata's `column_names_to_labels` attribute
                * variable_type: my own categorization of the variables to remember the timing of the variables. variable_type is one of these: `identifier`, `defendant`, `crime_current`, `crime_history`, `sentence`, or `hearing`
                * levels: mapping of the numeric-type category labels in the .sav file to their string-type category labels (e.g. `{"1.0": "Stay","2.0": "Commit"}` is the mapping for `presumpt`)

        2) `county_types()`
            * keys: county name (e.g. `anoka`, `crow wing`, `ramsey`, ...)
            * values: county type: `metropolitan`, `micropolitan`, or `rural`

        3) `statute_codes()`
            * keys: 9-digit statute code
            * values: string-type statute description (e.g. `Counterfeiting of Currency`, `Second Deg. Sale 10+ G Other Narcotic`, ...)
            * majority of key-value pairs come from `\\data\\nick_files\statuteName2022.xlsx` and the rest are added manually from the [Minnesota Statutes Site](https://www.revisor.mn.gov/statutes/) 

### Outputs: 
* `\\data\\jake_files\\data_clean.csv`
    * dataset cleaned and indexed by charge_id from 1991-2022

## 1) drug_grid_introduction.ipynb
### Inputs:
* `\\data\\jake_files\\data_clean.csv`
    * dataset cleaned and indexed by charge_id from 1991-2022

### Outputs:


## 2) drug_grid_intent_to_treat.ipynb
### Inputs:
* `\\data\\jake_files\\data_clean.csv`
    * dataset cleaned and indexed by charge_id from 1991-2022

### Outputs:


## 3) dwi_intent_to_treat.ipynb
Failed project :/

