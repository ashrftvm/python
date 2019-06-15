import json

newData = {}
newData['products'] = []

with open('some.json') as json_file:
    data = json.load(json_file)
    newData = data
    for p in newData['products']:
        for c in p['prices']:
            c['cost'] = c['cost'] * 1.10
    print(newData)



with open('ard.json', 'w') as outfile:
    json.dump(newData, outfile)

print('finished')





