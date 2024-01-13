import json
from os import scandir

ids = set()

with open('casinos.txt', 'r') as file:
    for line in file:
        ids.add(line.split(',')[0])

total = len(ids)

processed_ids = set()

with open('processed_casinos.txt', 'r') as file:
    for line in file:
        processed_ids.add(line.strip())

for entry in scandir('original'):
    if entry.path.endswith('.jpg') and entry.is_file():
        id = entry.name.replace('.jpg', '')
        if id not in ids:
            print(id)
        else:
            ids.remove(id)
        
        if id in processed_ids:
            processed_ids.remove(id)

    elif not entry.path.endswith('.DS_Store'):
        print(entry)

known_skipped_ids = {'CAMC', 'GGAM'}
for id in processed_ids:
    if id not in known_skipped_ids:
        print(id)

print("{} / {} remaining".format(len(ids) - len(known_skipped_ids), total))