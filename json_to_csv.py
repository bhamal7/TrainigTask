import json
import csv


#opening the json file

with open("simple.json") as json_file:
    data = json.load(json_file)

employ_data = data['employdetails']

csv_file = open('simple.csv','w')
csv.writer = csv.writer(csv_file)


count = 0
for i in employ_data:
    if count == 0:
        header = i.keys()
        csv.writer.writerow(header)
        count+=1
    csv.writer.writerow(i.values())

csv_file.close()


