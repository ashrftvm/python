import csv
import json

csvFilePath = 'farnell cat.csv'
jsonFilePath = 'data.json'

data={}
with open(csvFilePath) as csvfile:
   csvReader = csv.DictReader(csvfile)
   for rows in csvReader:
       PCC = rows['PCC']
       data['PCC'] = PCC


with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))