import requests
import json
import time

count = 0


def count_and_get_init():
    data = requests.get('https://apiurl')
    global count
    count += 1
    # print(data.status_code)
    new_data = data.json()
    total_count = new_data['keywordSearchReturn']['numberOfResults']
    limit = total_count/10
    new_data = json.dumps(new_data['keywordSearchReturn']['products'])
    write_to_file(new_data)

    if type(limit) is float:
        limit += 1
        limit = int(limit)
    elif type(limit) is int:
        limit = int(limit)
    else:
        print(limit)

    while count < limit:
        time.sleep(30)
        print(count)
        repeated_get(count)
        count += 1

    print('finished')


def repeated_get(offset):
    offset = offset * 30
    offset = str(offset)
    data = requests.get('https://apiUrl')
    print(data.status_code)
    if data.status_code == 200:
        print(data.content)
        new_data = data.json()
        new_data = json.dumps(new_data['keywordSearchReturn']['products'])
        write_to_file(new_data)
    elif data.status_code == 403:
        time.sleep(120)
        repeated_get(offset)
    else:
        print(data.status_code+'some error')


def write_to_file(data):
    with open('amphenol.json', 'a+') as outfile:
        outfile.write(data)

        print('finished')


count_and_get_init()
