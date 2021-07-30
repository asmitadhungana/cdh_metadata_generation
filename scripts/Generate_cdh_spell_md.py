import csv
import json
import pandas as pd
from pandas.core.reshape.merge import merge

complete_df = pd.read_csv('../datasets/CDH_Complete_List.csv',keep_default_na=False, na_values=[""])
spell_df = pd.read_csv('../datasets/CDH_Spell.csv',keep_default_na=False, na_values=[""])

merged_df = pd.merge(complete_df, spell_df, on="Card" or "OLD NAME")
print(merged_df)
del merged_df['OLD NAME']
merged_df.rename(columns={'Attribute 6 Affinity': 'Affinity'}, inplace=True)

merged_df.to_csv('../datasets_output/final_cdh_spell.csv', index=False)


nonAttributes = ["Card", "Description"]
counter = 0
complete_dict = []

csv_file = open('../datasets_output/final_cdh_spell.csv', 'r') 
csv_reader = csv.DictReader(csv_file)
for i, row in enumerate(csv_reader):
    if i != 0:
        new_dict = {}
        innerCounter = 0
        attributes = []

        new_dict['name'] = row['Card']
        new_dict['description'] = row['Description']
        new_dict['external_url'] = ""
        new_dict['image'] = ""
        for key, value in row.items():
            if value != "":
                if key in nonAttributes:
                    new_dict['name'] = row['Card']
                
                elif key not in nonAttributes:
                    attributes.append(
                        {
                            "trait_type": key,
                            "value": value
                        }
                    )
                    innerCounter+=1

        print(innerCounter)
                
        new_dict['attributes'] = attributes
        counter += 1
        # print(f'newDict{new_dict}')
        
        
        jsonfile = open('../metadatas/metadata_cdh_spell/'+ 'spell'+str(counter)+'.json', 'w')
        json.dump(new_dict, jsonfile, indent=4)
        jsonfile.write('\n')

        complete_dict.append(new_dict)
    jsonComplete =  open('../metadatas/metadata_cdh_spell_complete'+ '.json', 'w')
    json.dump(complete_dict, jsonComplete, indent=4)
    jsonComplete.write('\n')
    
    print(complete_dict)
    