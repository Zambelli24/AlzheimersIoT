import requests
import datetime
import json

def UploadAPI(User, score,token):
    #base_url = 'http://api:8080/api/memoryGame'
    base_url = 'http://api:8080/add_data'
    authorization_string = "Bearer " + token
    header = {'Authorization' : authorization_string}
    time = datetime.datetime.utcnow().isoformat()
    #payload = {'user': User,'score': score, 'time': date}
    #sendUserResults = requests.post(base_url, data=payload,headers=header)
    data = json.dumps({'score': score})
    payload = {'key': 'memory_game', 'time': time, 'data': data}
    #payload = {'key': 'memory_game'}
    sendUserResults = requests.post(base_url, data=payload)
    print(sendUserResults)