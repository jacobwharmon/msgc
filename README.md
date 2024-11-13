# A) Directory Structure
## data
#### `\data\jake_files\`: this is where all of Jake's data outputs live, namely `data_clean.csv` which is the cleaned and combined 1991-2022 dataset

#### `\data\nick_files\`: this is where some of Nick's data outputs live, namely `statuteName2022.xlsx`

#### `\data\UMN Data\`: this is a raw, unedited mirror of the files in the MSGC Dropbox. This is all view-only so that we have documentation (via the python scripts) of every cleaning step we do from the raw files all the way to `\data\jake_files\data_clean.csv`


## figures
#### This is where are all the figures produced by `\scripts\drug_grid_introduction.ipynb` and `\scripts\drug_grid_intent_to_treat.ipynb` live as well as 

#### Relevant versions of the Standard Sentencing Guidelines Grids and Drug Sentencing Guidelines Grids also live here, as they are used in the reports found in `\output\`


## output
#### This is where all of the reports I've made in overleaf live, both the `.tex`'s and their corresponding `.pdf`'s

#### `output\tables\`: the tables you see used in the reports above, as well as in `\slides\`, are produced by scripts as `.csv` or `.xlsx` and then formatted and printed as `.pdf`


## scripts
#### Every python file lives in here and is described in detail in section B


## slides
#### Materials (`.tex` and corresponding `.pdf`) for the 20 July 2024 presentation to the Minnesota Sentencing Guidelines Commission of our work on the 2016 Introduction of the Drug Grid

#### `slides\images\` is where all of the `.png`'s referenced in the `.tex` file live


# B) Description of Work Done
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

