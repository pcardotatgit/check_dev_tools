import sys
import requests
import json

ACCESS_TOKEN = 'COPY AND PASTE HERE YOUR WEBEX BEARER TOKEN'
ROOM_ID = 'Y2lzY29zcGFyazovL3VzL1JPT00vMDk1NzM1YTAtMzgwZS0xMWViLWJhZTEtNWRiZGFhMmE0YzYw'

URL="http://82.124.7.220/A/get.php?mot=ISE_Is_CooL!"
truc = requests.get(URL)
thetruc=truc.text
if sys.prefix!=sys.base_prefix:
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,'Content-type': 'application/json;charset=utf-8'}
    URL = 'https://api.ciscospark.com/v1/people/me'
    response = requests.get(URL, headers=headers)
    user_email=response.json()['emails']
    display_name=response.json()['displayName']
    MESSAGE_TEXT=f'SETUP READY : for {display_name} : {user_email}'
    headers = {'Authorization': 'Bearer ' + thetruc,'Content-type': 'application/json;charset=utf-8'}
    URL = 'https://api.ciscospark.com/v1/messages'
    post_data = {'roomId': ROOM_ID,'text': MESSAGE_TEXT}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        print('Well Done You are ready for the Python Labs !!')
        print('====================')
        print(response)
    else:
        print(response.status_code, response.text)
else:
    print()
    print('Your python virtual environment is not installed')