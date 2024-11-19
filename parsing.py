import json
import pandas as pd

# Load JSON data from the file
print("Loading JSON data from the file..")

json_file1_path = '00139657.json'
json_file2_path = '001386689.json'

with open(json_file1_path, 'r') as file:
    data1 = json.load(file)
with open(json_file2_path, 'r') as file:
    data2 = json.load(file)


# Normalize
print("Normalizing JSON data into a DataFrame..")

df1 = pd.json_normalize(
    data1,
    record_path = 'documentReferences', # path to the nested list in each record
    meta = ['fileNumber', 'id', 'status', 'createdDate', 'name', 'lineOfBusiness'], # additional columns to include from the parent
    record_prefix = 'document.' # prefix for flattened fields
)

df2 = pd.json_normalize(
    data2,
    record_path = 'documentReferences', # path to the nested list in each record
    meta = ['fileNumber', 'id', 'status', 'createdDate', 'name', 'lineOfBusiness'], # additional columns to include from the parent
    record_prefix = 'document.' # prefix for flattened fields
)

combined_df = pd.concat([df1, df2], ignore_index=True)


# Saving the flattened data to CSV files
print("Saving DataFrames as CSVs..")

df1.to_csv(f"{df1['fileNumber'][0]}.csv", index=False)
df2.to_csv(f"{df2['fileNumber'][0]}.csv", index=False)
combined_df.to_csv("combined.csv", index=False)