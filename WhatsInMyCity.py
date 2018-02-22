import json
import requests
limit = 50
offset = 0
location = "Washington,DC"
api_token = ''
api_url = 'https://api.yelp.com/v3/businesses/search?location='+ location +'&term="restaurants"&limit='+str(limit)+'&offset='+str(offset)

headers = {'Authorization': 'Bearer {0}'.format(api_token)}
           
response = requests.get(api_url, headers = headers)

print(response.status_code)

content = json.loads(response.content.decode('utf-8'))

total = content['total']

list = []

def callYelp(list,limit,offset):
    api_token = 'FZy0X7bZDxwmTTJHHW2jNNfueAzTU4sq5HVBEUuJuSn5sJccurZoqYdtkCMMWJ6P6JT_tPKTAsQhth4gJmGmPq5hnqDo60ZmGij9dLPhmVNbfiA4S2neTAlvkk2OWnYx'
    api_url = 'https://api.yelp.com/v3/businesses/search?location="Washington,DC"&term="restaurants"&limit='+str(limit)+'&offset='+str(offset)

    headers = {'Authorization': 'Bearer {0}'.format(api_token)}
           
    response = requests.get(api_url, headers = headers)

    print(response.status_code)

    content = json.loads(response.content.decode('utf-8'))

    for rest_num in range(0, len(content['businesses'])):
        for cat_num in range(0, len(content['businesses'][rest_num]['categories'])):
            title= content['businesses'][rest_num]['categories'][cat_num]['title']
            if title not in list:
                list.append(title)
    return list;


list = callYelp(list,limit,offset)

for offset in range(limit,min(1000-limit,total),limit):
    list = callYelp(list,limit,offset)

print(list)
