import requests
import json
import time

count = 0


def count_and_get_init(sku):
    returneddata = requests.get('url'+sku+)
    global count
    count += 1
    print(returneddata.status_code)
    new_data = returneddata.json()
    # print(new_data)
    time.sleep(10)
    write_to_file(new_data)


def write_to_file(writedata):
    with open('crystalsNew.json', 'a+') as outfile:
        json.dump(writedata, outfile)
        outfile.write('\n,')
        print('finished write')


with open('crystals.json') as json_file:
    data = json.load(json_file)
    for p in data['keywordSearchReturn']['products']:
        print(p['sku'])
        productSku = p['sku']
        count_and_get_init(productSku)