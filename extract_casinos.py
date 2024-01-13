import json

map = {}

with open('casinos.json', 'r') as file:
    data = json.load(file)
    for obj in data:
        map[obj['casinoID']] = [obj['shortName'], obj['city']]

with open('casinos.txt', 'w') as f:  
    for key in sorted(map.keys()):
        name = map[key][0]
        city = map[key][1]
        f.write('%s, %s, %s\n' % (key, name, city))