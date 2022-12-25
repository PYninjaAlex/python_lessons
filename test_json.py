import json

with open('serials.json', 'r', encoding='utf-8') as jason:
    reading = json.load(jason)

reading['Serials'][0]['name'] = 'Flash'

with open('serials.json', 'w', encoding='utf-8') as outfile:
    json.dump(reading, outfile)