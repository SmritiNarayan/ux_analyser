import csv
import json
import collections

CSV_PATH = 'input.csv'
JSON_PATH = 'd3.json'

csv_file = csv.DictReader(open(CSV_PATH, 'r'))

#print(csv_file)

json_list = []
for row in csv_file:
    #print(type(row))
    x = [("label", row["label"]), ("y", row["y"])]
    json_list.append(collections.OrderedDict(x))

#print(json_list)

a = json.dumps(json_list)
b = "d3 = '"
c = b + a+"';"
file(JSON_PATH, 'w').write(c)

