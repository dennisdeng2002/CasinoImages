import json

map = {}

def extract_shortnames_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        for obj in data:
            map[obj['casinoID']] = obj['shortName']

input_file = 'casinos.json'
extract_shortnames_from_json(input_file)

with open("casino_names.txt", 'w') as f:  
    for id, name in map.items():  
        f.write('%s, %s\n' % (id, name))