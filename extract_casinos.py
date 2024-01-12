import json

map = {}

def extract_shortnames_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        for obj in data:
            map[obj['casinoID']] = [obj['shortName'], obj['city']]

input_file = 'casinos.json'
extract_shortnames_from_json(input_file)

with open("casinos.txt", 'w') as f:  
    for key in sorted(map.keys()):
        name = map[key][0]
        city = map[key][1]
        f.write('%s, %s, %s\n' % (key, name, city))