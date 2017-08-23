import csv
import jsonlines

total = 0
docnpi = 0
docinfo = 0
pracnpi = 0
pracinfo = 0
nomatch = 0


# source_data = json.load('data_files/source_data.json'')
# with open('data_files/match_file.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         with open('data_files/source_data.json') as json_file:  
#             data = json.load(json_file)
#             for p in data['people']:
#                 print('Name: ' + p['name'])
#                 print('Website: ' + p['website'])
#                 print('From: ' + p['from'])
#                 print('')

with open('data_files/match_file.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        with jsonlines.open('data_files/source_data.json') as json_file:
            for p in json_file:
                total+=1
                if row['npi'] == p['doctor']['npi']:
                    docnpi+=1
                elif row['first_name'] == p['doctor']['first_name'] and row['last_name'] == p['doctor']['last_name']: #and row['street'] == p['doctor']['street'] and row['street_2'] == p['doctor']['street_2'] and row['city'] == p['doctor']['city'] and row['state'] == p['doctor']['state'] and row['zip'] == p['doctor']['zip']:
                    docinfo += 1
                elif (x for x in p['practices'] if x['city'] == row['city'] and x['street'] == row['street'] and x['street_2'] == row['street_2'] and x['state'] == row['state'] and x['zip'] == row['zip']):
                    pracinfo += 1
                else:
                    nomatch += 1


print(total, docnpi, docinfo, pracinfo)







