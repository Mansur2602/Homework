import json
import requests

with open('index.json', 'r') as file:
    data = json.load(file)


print(data)

json_data = json.dumps(data)
with open('index_2.json', 'w') as file:
    file.write(json_data)