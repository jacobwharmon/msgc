import pandas as pd

def variables_dict(years='01_22') -> dict:
    """
        years: value in ['01_22','91_00']
        
        
        Description:
            Summary of variable's meaning from the meta_01_22.column_names_to_labels which comes from the 2011-2022_MSGC_MonitoringDataCodebookSPSSCodeBook.xlsx
            where meta_01_22 is the metadata from reading in File01_22.sav

        Variable Types:
            index - 
            defendant - represents fixed demographic identifiers for the defendant. age, race, sex, ethnicity, ...
            crime_history - 
            crime_current - 
            sentence - 
            hearing - identifiers for the hearing itself. county, district, ...


        Levels:
            for categorical variables with discrete levels, this is a dictionary mapping the level code to what it represents in the CodeBook using the following code:
            
            for col in variables_dict.keys():
                if col in meta_01_22.variable_value_labels.keys():
                    variables_dict[col]['levels'] = meta_01_22.variable_value_labels[col]
                else:
                    variables_dict[col]['levels'] = None

        Note:
            if you'd like to print the variables_dict in a more human-like format use the following code:
                
                import json

                print(json.dumps(
                    variables_dict,
                    sort_keys=False,
                    indent=4,
                    separators=(',', ': ')
                ))
    """
    variables_dict = {
        # Indexes
        "chargeid": {"description": "Charge_ID","variable_type": "identifier","levels": None},

        # Defendant demographic information
        "dborn": {"description": "Date of birth","variable_type": "defendant","levels": None},
        "sex": {"description": "Offender sex","variable_type": "defendant","levels": {"0.0": "corp","1.0": "male","2.0": "female"}},
        "race": {"description": "Offender race","variable_type": "defendant","levels": {"0.0": "corp","1.0": "White","2.0": "Black","3.0": "Am Ind","4.0": "Hispanic","5.0": "Asian","6.0": "Other","7.0": "Unk"}},
        "ethnic": {"description": "Offender ethnicity","variable_type": "defendant","levels": {"0.0": "none","1.0": "Hispanic","2.0": "unknown"}},
        "ageoff": {"description": "Age at offense","variable_type": "defendant","levels": None},
        "agesent": {"description": "Age at sentence","variable_type": "defendant","levels": None},

        # Defendant criminal history
        "history": {"description": "Total history (6 thru hi=6)","variable_type": "crime_history","levels": None},
        "totprior": {"description": "Total number of priors","variable_type": "crime_history","levels": None},
        "histall": {"description": "Total history","variable_type": "crime_history","levels": None},
        "countfel": {"description": "Num Felony priors on ws","variable_type": "crime_history","levels": None},
        "tfelony": {"description": "Felony points","variable_type": "crime_history","levels": None},
        "tgross": {"description": "Misd/GM points","variable_type": "crime_history","levels": None},
        "tweight": {"description": "Total felony weight","variable_type": "crime_history","levels": None},

        # Defendant current crime
        "doff": {"description": "Date of offense","variable_type": "crime_current","levels": None},
        "dconv": {"description": "Date of offense","variable_type": "crime_current","levels": None},
        "Offense": {"description": "Offense title - coded","variable_type": "crime_current","levels": {"1.0": "Other Person","2.0": "Murder 1","3.0": "Mur 2 sev=11","4.0": "Mur 2 sev=10","5.0": "Mur 3 sev=9/10","6.0": "Mansl 1 sev=9","7.0": "Mansl 1 sev=8","8.0": "Mansl 2 sev=8","9.0": "CVH","10.0": "CVI sev=5","11.0": "CVI sev=3","12.0": "Asslt 1","13.0": "Asslt 2","14.0": "Asslt 3","15.0": "Asslt 4","16.0": "Asslt 5","17.0": "Dom Asslt","17.5": "DomAsltStrang","18.0": "Simp Robb","19.0": "Agg Robb 1","20.0": "Agg Robb 2","21.0": "Kidnap sev=6","22.0": "Kidnap sev=8/9","23.0": "False Impris","24.0": "Parental Rights","25.0": "Coercion","26.0": "Accidents","27.0": "CSC 1","28.0": "CSC 2","29.0": "CSC 3","30.0": "CSC 4","31.0": "CSC 5","32.0": "Solicit Minor Sex","33.0": "Malic Punish","34.0": "Terr Th sev=4","35.0": "Terr Th sev=1/2","35.5": "Interfere Privacy","35.6": "Surreptitious Observation Device (Minor & Sexual Intent)","36.0": "Stalk sev=4","37.0": "Stalk sev=5","37.5": "Private Images","38.0": "Drive-by","39.0": "Viol Rest Or","40.0": "Other Prop","41.0": "Theft","42.0": "Theft Firearm","43.0": "Theft Over 35K","44.0": "Shoplift Gear","45.0": "Theft Fr Pers","46.0": "Theft MV","47.0": "MV Use","48.0": "Rec Stln Prop","49.0": "Arson 1","50.0": "Arson 2","51.0": "Arson 3","52.0": "Burg 1 sev=6","53.0": "Burg 1 sev=8","54.0": "Burg 2 sev=5","55.0": "Burg 2 sev=4","56.0": "Burg 3","57.0": "Poss Burg Tools","58.0": "Crim Damage","59.0": "Other Forg","60.0": "Chk Forg sev=5","61.0": "Chk Forg sev=3","62.0": "Chk Forg sev=2","63.0": "Chk Forg sev=1","64.0": "Dishonored  Chk","65.0": "FTCF","66.0": "WOA/FoodS/Unemp","67.0": "Identity Theft","68.0": "Counterfeit Check","68.5": "Counterfeit Currency","69.0": "Mail Theft","70.0": "Other Drug","71.0": "Con Sub 1","72.0": "Con Sub 2","73.0": "Con Sub 3","74.0": "Con Sub 4","75.0": "Con Sub 5","76.0": "Subs Intent Manuf","80.0": "Other Other","81.0": "Oth Wpn Related","82.0": "Disch Firearm","83.0": "Felon W Gun","84.0": "Bribery","85.0": "Perjury","86.0": "Escape sev=3","87.0": "Flee Police","88.0": "Aid Offender","89.0": "Accomplice After","90.0": "Tamper witness","91.0": "Obstr Leg Proc","92.0": "Prostitution","93.0": "Lottery Fraud","94.0": "Felony DWI","95.0": "Fail Register","96.0": "Child Porn","96.5": "Use of Minor","97.0": "Failure to Appear","98.0": "Other Sex Grid","98.5": "Ind Exposure","99.0": "Tax Offenses"}},
        "offtype": {"description": "General offense type","variable_type": "crime_current","levels": {"1.0": "person","2.0": "property","3.0": "drugs","4.0": "other","5.0": "noncsc/sex grid","6.0": "DWI","7.0": "Weapons","8.0": "Other"}},
        "severity": {"description": "Severity Level","variable_type": "crime_current","levels": {"1.0": "1","2.0": "2","3.0": "3","4.0": "4","5.0": "5","6.0": "6","7.0": "7","8.0": "8","9.0": "9","10.0": "10","11.0": "11","12.0": "Murder 1","13.0": "A","14.0": "B","15.0": "C","16.0": "D","17.0": "E","18.0": "F","19.0": "G","20.0": "H","21.0": "I","51.0":"D1","52.0":"D2","53.0":"D3","54.0":"D4","55.0":"D5","56.0":"D6","57.0":"D7","58.0":"D8","59.0":"D9",}},
        "weapon": {"description": "Dangerous weapon variable or MOC","variable_type": "crime_current","levels": {"0.0": "None/Missing","1.0": "Firearm Used","2.0": "Firearm Poss.","3.0": "Other Weapon","4.0": "Wpn Type UK","5.0": "Firearm","6.0": "Weapon Rel. Off","7.0": "Replica","8.0": "Feigned"}},
        "dngwpn": {"description": "Dangerous weapon","variable_type": "crime_current","levels": {"0.0": "No Dng Wpn","1.0": "Use Firearm","2.0": "Poss Firearm","3.0": "Oth Dng Wpn","4.0": "Viol Felon","5.0": "Ammo"}},
        "subwpn": {"description": "Subsequent weapon offense?","variable_type": "crime_current","levels": {"0.0": "No","1.0": "Yes"}},
        "subsex": {"description": "Subsequent sex offense?","variable_type": "crime_current","levels": {"0.0": "No","1.0": "Yes"}},
        "subdrug": {"description": "Subsequent drug offense?","variable_type": "crime_current","levels": {"0.0": "No","1.0": "Yes"}},
        "subdwi": {"description": "Subsequent DWI?","variable_type": "crime_current","levels": {"0.0": "no","1.0": "yes"}},
        "subfailr": {"description": "Subseq Fail to Register","variable_type": "crime_current","levels": {"0.0": "No","1.0": "Yes"}},
        "Subburg": {"description": "Subseq Burglary","variable_type": "crime_current","levels": {"0.0": "No","1.0": "Yes"}},

        # Sentence information
        "sentyear": {"description": "Year of sentence","variable_type": "sentence","levels": None},
        "dsent": {"description": "Date of sentence","variable_type": "sentence","levels": None},
        "presumpt": {"description": "Recommended disposition","variable_type": "sentence","levels": {"1.0": "Stay","2.0": "Commit"}},
        "time": {"description": "Presumptive sentence in months","variable_type": "sentence","levels": None},
        "confine": {"description": "Pronounced confinement - months","variable_type": "sentence","levels": None},
        "aggsentc": {"description": "Aggragated sentence in mos","variable_type": "sentence","levels": None}, # FROM MATT: "we use aggsentc to view the pronounced sentence rather than confine. The reason is that aggsentc accounts for consecutive sentencing whereas confine does not. All of our internal files contain all three of these variables, including those with data from 1991-2000, 2001-2010, and 2011-2022"
        "staylnth": {"description": "Length of stay - months","variable_type": "sentence","levels": None},
        "prison": {"description": "Executed prison sentence?","variable_type": "sentence","levels": {"0.0": "No","100.0": "Yes"}},
        "stayexec": {"description": "Stay of execution?","variable_type": "sentence","levels": {"0.0": "No","1.0": "Yes"}},
        "impose": {"description": "Stay imposition?","variable_type": "sentence","levels": {"0.0": "No","1.0": "Yes"}}, # local jail or facility up to one year of probation sentence
        "typecust": {"description": "Type of custody","variable_type": "sentence","levels": {"0.0": "None","1.0": "Probation","2.0": "Parole/Sup.Rel","3.0": "Confined","4.0": "Rel Pending Sent","5.0": "Escape","6.0": "EJJ","7.0": "Other","8.0": "Within Original Probation Term","9.0": "Conditional Release"}},
        "typeprob": {"description": "Type of probation","variable_type": "sentence","levels": {"0.0": "none","1.0": "supervised","2.0": "unsupervised","3.0": "court"}},
        "inctype": {"description": "Incarceration Type","variable_type": "sentence","levels": {"0.0": "Other Sanctions","1.0": "State Prison","2.0": "Cond Jail","3.0": "Jail Sent"}},
        
        "dispdep": {"description": "Dispositional Departure?","variable_type": "sentence","levels": {"0.0": "None","1.0": "Aggravated","2.0": "Mitigated","3.0": "Misd Sent","4.0": "Stay Length","5.0": "Stay Length+Agg","6.0": "Stay Length+Mit","7.0": "NoHalfCSP","8.0": "Kirby","9.0": "Def. Demanded"}},
        "durdep": {"description": "Durational Departure?","variable_type": "sentence","levels": {"0.0": "None","1.0": "Aggravated","2.0": "Mitigated","3.0": "Misd Sent","4.0": "Stay Length","5.0": "Stay Length+Agg","6.0": "Stay Length+Mit","7.0": "NoHalfCSP","8.0": "Kirby","9.0": "Def. Demanded"}},
        "deptype": {"description": "Departure type","variable_type": "sentence","levels": {"0.0": "none","1.0": "up","2.0": "down","3.0": "mixed","4.0": "stay length"}},
        "Maxtime": {"description": "Grid Maximum Duration","variable_type": "sentence","levels": None},
        "Mintime": {"description": "Grid Minimum Duration","variable_type": "sentence","levels": None},
        
        "plea": {"description": "Plea entered?","variable_type": "sentence","levels": {'1.0': 'guilty', '2.0': 'trial'}},
        "convstat": {"description": "Conv_Statute","variable_type": "sentence","levels": None},
        "statute": {"description": "MN Statute","variable_type": "sentence","levels": None},

        # Hearing
        "county": {"description": "County sentenced","variable_type": "hearing","levels": {"1.0": "Aitkin","2.0": "Anoka","3.0": "Becker","4.0": "Beltrami","5.0": "Benton","6.0": "Big Stone","7.0": "Blue Earth","8.0": "Brown","9.0": "Carlton","10.0": "Carver","11.0": "Cass","12.0": "Chippewa","13.0": "Chisago","14.0": "Clay","15.0": "Clearwater","16.0": "Cook","17.0": "Cottonwood","18.0": "Crow Wing","19.0": "Dakota","20.0": "Dodge","21.0": "Douglas","22.0": "Faribault","23.0": "Fillmore","24.0": "Freeborn","25.0": "Goodhue","26.0": "Grant","27.0": "Hennepin","28.0": "Houston","29.0": "Hubbard","30.0": "Isanti","31.0": "Itasca","32.0": "Jackson","33.0": "Kanabec","34.0": "Kandiyohi","35.0": "Kittson","36.0": "Koochiching","37.0": "Lac Qui Parle","38.0": "Lake","39.0": "Lake of the Woods","40.0": "LeSueur","41.0": "Lincoln","42.0": "Lyon","43.0": "McLeod","44.0": "Mahnomen","45.0": "Marshall","46.0": "Martin","47.0": "Meeker","48.0": "Mille Lacs","49.0": "Morrison","50.0": "Mower","51.0": "Murray","52.0": "Nicollet","53.0": "Nobles","54.0": "Norman","55.0": "Olmsted","56.0": "Otter Tail","57.0": "Pennington","58.0": "Pine","59.0": "Pipestone","60.0": "Polk","61.0": "Pope","62.0": "Ramsey","63.0": "Red Lake","64.0": "Redwood","65.0": "Renville","66.0": "Rice","67.0": "Rock","68.0": "Roseau","69.0": "St. Louis","70.0": "Scott","71.0": "Sherburne","72.0": "Sibley","73.0": "Stearns","74.0": "Steele","75.0": "Stevens","76.0": "Swift","77.0": "Todd","78.0": "Traverse","79.0": "Wabasha","80.0": "Wadena","81.0": "Waseca","82.0": "Washington","83.0": "Watonwan","84.0": "Wilkin","85.0": "Winona","86.0": "Wright","87.0": "Yellow Medicine"}},
        "district": {"description": "MN Judicial District","variable_type": "hearing","levels": None},
        "jfname": {"description": "Judge firstname","variable_type": "hearing","levels": None},
        "jlname": {"description": "Judge lastname","variable_type": "hearing","levels": None},

    }
        
    if years == '91_00':
        # Exclude the variables from the 01_22 data not found in the 91_00 data
        keys_to_keep = set(variables_dict.keys()) - {'chargeid', 'dborn', 'ethnic', 'dconv', 'Offense', 'dngwpn', 'subwpn', 'subsex', 'subdrug', 'subdwi', 'subfailr', 'Subburg', 'inctype', 'deptype', 'Maxtime', 'Mintime', 'convstat', 'statute', 'jfname', 'jlname'}
        variables_dict = {k: variables_dict[k] for k in keys_to_keep}
        
        # Add in the ones that are named differently
        variables_dict_91_00_supplement = {
            "caseno": {"description": "NEEDS CONFIRMED, but believed to be chargeid", "variable_type":"identifier", "levels": None},
            "offense": {"description": "Offense title - coded","variable_type": "crime_current","levels": {"1.0": 'OTHER PERSON', "2.0": 'AT MUR 1', "3.0": 'MUR 2 SEV=10', "4.0": 'MUR 2 SEV=9', "5.0": 'MUR 3', "6.0": 'MANSL 1 SEV=8', "7.0": 'MANSL 1 SEV=7', "8.0": 'MANSL 2 SEV=7', "9.0": 'CVH', "10.0": 'CVI SEV=5', "11.0": 'CVI SEV=3', "12.0": 'ASSLT 1', "13.0": 'ASSLT 2', "14.0": 'ASSLT 3', "15.0": 'ASSLT 4', "16.0": 'ASSLT 5', "17.0": 'DOM ASSLT', "18.0": 'SIMP ROBB', "19.0": 'AGG ROBB 1', "20.0": 'AGG ROBB 2', "21.0": 'KIDNAP SEV=6', "22.0": 'KIDNAP SEV=78', "23.0": 'FALSE IMPRIS', "24.0": 'PARENTAL RIGHTS', "25.0": 'COERCION', "27.0": 'CSC 1', "28.0": 'CSC 2', "29.0": 'CSC 3', "30.0": 'CSC 4', "31.0": 'CSC 5', "32.0": 'MINOR SEX COND', "33.0": 'MALIC PUNISH', "34.0": 'TERR TH SEV=4', "35.0": 'TERR TH SEV=12', "36.0": 'STALK SEV=34', "37.0": 'STALK SEV=5', "38.0": 'DRIVE-BY', "39.0": 'VIOL REST OR', "40.0": 'OTHER PROP', "41.0": 'THEFT', "42.0": 'THEFT FIREARM', "43.0": 'THEFT OVER 35K', "44.0": 'SHOPLIFT GEAR', "45.0": 'THEFT FR PERS', "46.0": 'THEFT MV', "47.0": 'MV USE', "48.0": 'REC STLN PROP', "49.0": 'ARSON 1', "50.0": 'ARSON 2', "51.0": 'ARSON 3', "52.0": 'BURG 1 SEV=6', "53.0": 'BURG 1 SEV=7', "54.0": 'BURG 2 SEV=5', "55.0": 'BURG 2 SEV=4', "56.0": 'BURG 3', "57.0": 'POSS BURG TOOLS', "58.0": 'CRIM DAMAGE', "59.0": 'OTHER FORG', "60.0": 'CHK FORG SEV=5', "61.0": 'CHK FORG SEV=3', "62.0": 'CHK FORG SEV=2', "63.0": 'CHK FORG SEV=1', "65.0": 'FTCF', "66.0": 'WOA/FOODS/UNEMP', "70.0": 'OTHER DRUG', "71.0": 'CON SUB 1', "72.0": 'CON SUB 2', "73.0": 'CON SUB 3', "74.0": 'CON SUB 4', "75.0": 'CON SUB 5', "80.0": 'OTHER OTHER', "81.0": 'OTH WPN RELATED', "82.0": 'DISCH FIREARM', "83.0": 'FELON W GUN', "84.0": 'BRIBERY', "85.0": 'PERJURY', "86.0": 'ESCAPE SEV=3', "87.0": 'FLEE POLICE', "88.0": 'AID OFFENDER', "89.0": 'ACCOMPLICE AFTER', "90.0": 'TAMPER WITNESS', "91.0": 'OBSTR LEG PROC', "92.0": 'PROSTITUTION', "93.0": 'LOTTERY FRAUD', "94.0": 'ACCIDENTS'}},
        }
        return {**variables_dict, **variables_dict_91_00_supplement}
    
    return variables_dict

def county_types() -> dict:
    """
    Categorizing counties by metropolitan, micropolitan, or rural using https://www.health.state.mn.us/data/workforce/docs/2017cbsa.pdf
    """
    county_types = {
        'aitkin': 'rural',
        'anoka': 'metropolitan',
        'becker': 'rural',
        'beltrami': 'micropolitan',
        'benton': 'metropolitan',
        'big stone': 'rural',
        'blue earth': 'metropolitan',
        'brown': 'micropolitan',
        'carlton': 'metropolitan',
        'carver': 'metropolitan',
        'cass': 'micropolitan',
        'chippewa': 'rural',
        'chisago': 'metropolitan',
        'clay': 'metropolitan',
        'clearwater': 'rural',
        'cook': 'rural',
        'cottonwood': 'rural',
        'crow wing': 'micropolitan',
        'dakota': 'metropolitan',
        'dodge': 'metropolitan',
        'douglas': 'micropolitan',
        'faribault': 'rural',
        'fillmore': 'metropolitan',
        'freeborn': 'micropolitan',
        'goodhue': 'micropolitan',
        'grant': 'rural',
        'hennepin': 'metropolitan',
        'houston': 'metropolitan',
        'hubbard': 'rural',
        'isanti': 'metropolitan',
        'itasca': 'rural',
        'jackson': 'rural',
        'kanabec': 'rural',
        'kandiyohi': 'micropolitan',
        'kittson': 'rural',
        'koochiching': 'rural',
        'lac qui parle': 'rural',
        'lake': 'rural',
        'lake of the woods': 'rural',
        'lesueur': 'metropolitan',
        'lincoln': 'rural',
        'lyon': 'micropolitan',
        'mahnomen': 'rural',
        'marshall': 'rural',
        'martin': 'rural',
        'mcleod': 'micropolitan',
        'meeker': 'rural',
        'mille lacs': 'metropolitan',
        'morrison': 'rural',
        'mower': 'micropolitan',
        'murray': 'rural',
        'nicollet': 'metropolitan',
        'nobles': 'micropolitan',
        'norman': 'rural',
        'olmsted': 'metropolitan',
        'otter tail': 'micropolitan',
        'pennington': 'rural',
        'pine': 'rural',
        'pipestone': 'rural',
        'polk': 'metropolitan',
        'pope': 'rural',
        'ramsey': 'metropolitan',
        'red lake': 'rural',
        'redwood': 'rural',
        'renville': 'rural',
        'rice': 'micropolitan',
        'rock': 'rural',
        'roseau': 'rural',
        'scott': 'metropolitan',
        'sherburne': 'metropolitan',
        'sibley': 'metropolitan',
        'st. louis': 'metropolitan',
        'stearns': 'metropolitan',
        'steele': 'micropolitan',
        'stevens': 'rural',
        'swift': 'rural',
        'todd': 'rural',
        'traverse': 'rural',
        'wabasha': 'metropolitan',
        'wadena': 'rural',
        'waseca': 'rural',
        'washington': 'metropolitan',
        'watonwan': 'rural',
        'wilkin': 'micropolitan',
        'winona': 'micropolitan',
        'wright': 'metropolitan',
        'yellow medicine': 'rural',
    }

    return county_types

def statute_codes() -> dict:
    """
    statute_codes_2022: the main set of statute number to offense description pairs that gets combined with
    statute_codes: For a handful of items that do not have the statute labels written
    """
    statute_codes_2022 = pd.read_excel('..\\data\\nick_files\\statuteName2022.xlsx').set_index('Recoded Statute')['Offense Title'].to_dict()
    
    statute_codes = {
        609821210: "Financial Transaction Card Fraud",
        609223110: "Assault 4  Bodily Harm, Peace Officer",
        152025220: "Fifth Deg. Poss. Procurement by Fraud",
        609222200: "Assault 2 Dangerous Weapon and Sub. Bodily Harm",
        609352210: "Electronic Solicitation of Children to Engage in Sexual Conduct",
        609343183: "CSC2 Under 16, Sig. Relation. and Multiple Acts",
        609520251: "Temporary Theft",
        201014100: "Voting Violation",
        609343170: "CSC2 Under 16, Sig. Relation.",
        169124130: "First Degree DWI - w/prior applicable CVO",
        609342170: "CSC1 Victim under 16, Significant Relationship",
        609713310: "Threats of ViolenceReplica Firearm",
        609342183: "Under 16, Sig. Relation. and Multiple Acts",
        609324130: "Engage or Hire a Minor to Engage in Prostitution",
        609520233: "Theft (>$5k) False Rep. - Medical Assist. Reimbursement Claim",
        624731811: "Tear Gas and Tear Gas Compounds; Electronic incapacitation devices",
        289163100: "Tax Evasion Laws",
        609632300: "Counterfeiting of Currency",
        201054100: "Voting Violations",
        609322112: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        609500200: "Obstructing Legal Process, Arrest, Firefighting, or Ambulance Service Personnel",
        609630110: "Forgery",
        609821220: "Financial Transaction Card Fraud",
        609342130: "CSC1 Fear Great Bodily Harm",
        609344122: "CSC3 Actor between 24 mos. And 48 mos. Older than victim",
        343210940: "Torture or cruelty to pet or companion animal",
        617247420: "Possession--Child Pornography",
        609378100: "Child Neglect/Endangerment",
        609210112: "Criminal Vehicular Operation Great Bodily Harm Gross Negligence",
        609210113: "Criminal Vehicular Operation Substantial Bodily Harm Gross Negligence",
        609625110: "Aggravated Forgery Noncheck",
        609625300: "Aggravated Forgery Noncheck",
        609344150: "CSC3 Victim 16-18, Significant Relationship",
        609821240: "Financial Transaction Card Fraud",
        609344160: "CSC3 Not Specified",
        152022162: "Second Deg. Sale Methamphetamine/Amphetamine in Zone/DTF",
        609345160: "CSC4 Victim 16-18, Significant Relationship",
        152022161: "Second Deg. Sale Narcotic/LSD in Zone/Drug Treatment Facility",
        518201224: "Violation of a Domestic Abuse No Contact Order",
        609345150: "CSC4 Victim 16-18, Actor 4 years older & Pos. Authority",
        609890120: "Computer Theft",
        152022120: "Second Deg. Sale 10+ G Other Narcotic",
        609322114: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        609668610: "Explosive Devices/Incendiary Devices",
        609322120: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        609625100: "Aggravated Forgery Noncheck",
        609322113: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        617246200: "Use of Minors in Sexual Performance Prohibited",
        609343181: "CSC2 Under 16, Sig. Relation. and Force or Coercion",
        609498120: "Tampering with a Witness, Aggravated First Degree",
        609322140: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        297210100: "Motor Vehicle Excise Tax",
        609324120: "Engage or Hire a Minor to Engage in Prostitution",
        609344173: "CSC3 Sig. Relation. and Multiple Acts over Time",
        169124132: "First Degree DWI - w/prior applicable CVO",
        169124133: "First Degree DWI - w/prior applicable CVO",
        609345015: "CSC 4 Massage Therapist",
        609630100: "Forgery",
        152021120: "First Deg. Sale 50+ G Other Narcotic",
        609630130: "Forgery",
        152022220: "Second Deg. Poss. 50+ G Other Narcotic",
        609630130: "Forgery",
        609821230: "Financial Transaction Card Fraud",
        609342161: "CSC1 Accomplice and use Force or Coercion",
        609343130: "CSC2 Fear Great Bodily Harm",
        609420130: "Bribery",
        624731814: "Tear Gas and Tear Gas Compounds; Electronic incapacitation devices",
        201054210: "Voting Violations",
        609630160: "Forgery",
        617247411: "Possession of Pictoral Representations of Minors Subsequent Possession",
        609343182: "CSC2 Under 16, Sig. Relation. and Personal Injury",
        609420110: "Bribery",
        609630150: "Forgery",
        609630200: "Forgery",
        609322110: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        617247320: "Dissemination--Child Pornography",
        204314000: "Unlawful Voting",
        609223130: "Assault 4 - Corrections, Prosecutor, Judge, Probation",
        609322111: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        609344013: "CSC3 Correctional Employee",
        609344180: "CSC3 Psychotherapist - Patient",
        609345013: "CSC4 Correctional Employee",
        609344015: "CSC3 Massage Therapist",
        169124131: "First Degree DWI - w/prior applicable CVO",
        609342182: "CSC1 Under 16, Sig. Relation. and Personal Injury",
        609632423: "Counterfeiting of Currency",
        609760300: "Gambling Acts (cheating, certain devices, counterfeit chips, manufacture/sale/mod. devices, instruction)",
        152021220: "First Deg. Poss 500+ G Other Narcotic",
        609270140: "CoercionProp. Value",
        609345113: "Criminal Sexual Conduct 5",
        609520253: "Temporary Theft",
        343210990: "Torture or cruelty to pet or companion animal",
        609270150: "CoercionProp. Value",
        609625150: "Aggravated Forgery Noncheck",
        609632410: "Counterfeiting of Currency",
        624731813: "Tear Gas and Tear Gas Compounds; Electronic incapacitation devices",
        609270130: "CoercionProp. Value",
        609322130: "Solicit, Promote, or Profit from Prost.; Sex Trafficking in the ? Degree",
        609344012: "CSC3 Clergy",
        609625160: "Aggravated Forgery Noncheck",
        609630120: "Forgery",
        609890110: "Computer Theft",
        169124134: "First Degree DWI - w/prior applicable CVO",
        349212720: "Gambling Regulations",
        609324110: "Engage or Hire a Minor to Engage in Prostitution",
        609342181: "CSC1 Under 16, Sig. Relation. and Force or Coercion",
        609344171: "CSC3 Sig. Relation. and Force or Coercion",
        609345014: "CSC4 Special Transprtation Service",
        609345173: "CSC4 Sig. Relation. and Multiple Acts over Time",
        609520252: "Temporary Theft",
        609668630: "Explosive Devices/Incendiary Devices",
        609821260: "Financial Transaction Card Fraud",
        609821280: "Financial Transaction Card Fraud",
        609821290: "Financial Transaction Card Fraud",
        624731810: "Tear Gas and Tear Gas Compounds; Electronic incapacitation devices",
        609343161: "CSC2 Accomplice and use Force or Coercion",
        609345011: "CSC4 Deception/False Rep. for Medical Purpose",  
        609345012: "CSC4 Clergy",
        609498121: "Tampering with a Witness, Aggravated First Degree",
        609630140: "Forgery",
        609630220: "Forgery",
        609671400: "Hazardous Wastes",
        609671520: "Hazardous Wastes",
        609821250: "Financial Transaction Card Fraud",
        609821263: "Financial Transaction Card Fraud",
        609821270: "Financial Transaction Card Fraud",
        609830200: "Falsely Impersonating Another",
        609880120: "Computer Damage",
        624731812: "Tear Gas and Tear Gas Compounds; Electronic incapacitation devices",
        152022163: "Second Deg. Sale 5+ K MJ in Zone/Drug Treatment Facility",
        201014300: "Voting Violations",
        203203111: "Voting Violations",
        203203112: "Voting Violations",
        203203115: "Voting Violations",
        203203200: "Voting Violations",
        343210970: "Torture or cruelty to pet or companion animal",
        349212730: "Gambling Regulations",
        609210230: "Criminal Vehicular Homicide Negligent while under Influence",
        609270120: "CoercionProp. Value",
        609270160: "CoercionProp. Value",
        609282000: "Labor Trafficking",
        609342150: "CSC1 Not Specified",
        609342160: "CSC1 Not Specified",
        609342162: "Accomplice and Dangerous Weapon",
        609344014: "CSC3 Special Transportation Service",
        609344172: "CSC3 Sig. Relation. and Personal  Injury",
        609345171: "CSC4 Sig. Relation. and Force or Coercion",
        609345180: "CSC4 Psychotherapist - Patient",
        609345190: "CSC4 Psychotherapist - -Former Patient Emot. Dependent",
        609420120: "Bribery",
        609420150: "Bribery",
        609498124: "Tampering with a Witness, Aggravated First Degree",
        609520234: "Theft (>$5k) False Rep. - Medical Assist. Reimbursement Claim",
        609625130: "Aggravated Forgery Noncheck",
        609625140: "Aggravated Forgery Noncheck",
        609625170: "Aggravated Forgery Noncheck",
        609630170: "Forgery",
        609630300: "Forgery",
        609632000: "Counterfeiting of Currency",
        609632400: "Counterfeiting of Currency",
        609632420: "Counterfeiting of Currency",
        609632432: "Counterfeiting of Currency",
        609668620: "Explosive Devices/Incendiary Devices",
        609821261: "Financial Card Transaction Fraud",
        609880100: "Computer Damage",
        # From Nick's Cleaning Above ^^ From My Cleaning Below \/\/
        152021120: "First Deg. Sale 10+ G Cocaine or Meth",
        152022161: "Second Deg. Sale Cocaine or Meth in School, Park, Public Housing, or Drug Treatment Facility", # https://www.revisor.mn.gov/statutes/cite/152.022
        152022162: "Second Deg. Sale Cocaine or Meth in School, Park, Public Housing, or Drug Treatment Facility", # https://www.revisor.mn.gov/statutes/cite/152.022
        152022163: "Second Deg. Sale Cocaine or Meth in School, Park, Public Housing, or Drug Treatment Facility", # https://www.revisor.mn.gov/statutes/cite/152.022
        152021220: "First Deg. Poss 25+ G Cocaine or Meth",
        152022120: "Second Deg. Sale 3+ G Cocaine or Meth",
        152022220: "Second Deg. Poss 10+ G Cocaine or Meth",
    }

    return {**statute_codes, **statute_codes_2022}