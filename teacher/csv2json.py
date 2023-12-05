import pdb
import csv
import json

file_name = 'oidv6-class-descriptions'

# the path you download the csv.
with open(f'/mnt/d/UniVTG-main/UniVTG-main/teacher/oidv6-class-descriptions.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = [row for row in reader]

class_list = [x[1] for x in data]

with open('/mnt/d/UniVTG-main/UniVTG-main/teacher/oidv6-class-descriptions.jsonl', 'w') as jsonfile:
    json.dump(class_list, jsonfile)
    