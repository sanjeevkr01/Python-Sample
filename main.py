import json
import requests

items=json.loads('[{"id":1,"text":"item 1"},{"id":2,"text":"item 2"}]')

for item in items:
    print(item['text']) 

response=requests.get('https://randomuser.me/api/?results=12')

data=response.json()

for user in data['results']:
    print(user['name'])


    

    