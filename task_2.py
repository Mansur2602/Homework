import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

with open('index.json', 'w') as index:
    index.write(response.text)



