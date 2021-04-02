import sys
import requests
import json

ip_address=" IP ADDRESS SHARED BY PATRICK HERE"

ACCESS_TOKEN = 'COPY AND PASTE HERE YOUR WEBEX BEARER TOKEN'
ROOM_ID = 'COPY HERE WEBEX TEAM ROOM ID SHARED BY PATRICK'

URL=f"http://{ip_address}/A/get.php?mot=ISE_Is_CooL!"
truc = requests.get(URL)
thetruc=truc.text

print('====================')
print()
print("This script helps you to check that you have installed the following tools in your development environment")
print()
print('- POSTMAN')
print('- Python 3.7')
print('- Python Virtual Environment')
print('- Git clone capability')
print('- Webex Team Account')
print()
print('====================')

running_in_virtualenv = bool(os.getenv("VIRTUAL_ENV"))        

if running_in_virtualenv:
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,'Content-type': 'application/json;charset=utf-8'}
    URL = 'https://api.ciscospark.com/v1/people/me'
    response = requests.get(URL, headers=headers)
    user_email=response.json()['emails']
    display_name=response.json()['displayName']
    print()
    print("STEP 1 OK")
    MESSAGE_TEXT=f'SETUP READY : for {display_name} : {user_email}'
    headers = {'Authorization': 'Bearer ' + thetruc,'Content-type': 'application/json;charset=utf-8'}
    URL = 'https://api.ciscospark.com/v1/messages'
    print("STEP 2 OK")
    print()    
    post_data = {'roomId': ROOM_ID,'text': MESSAGE_TEXT}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        print()
        print(f"SUCCESS : Well Done {display_name} You  are ready for the Python Labs !!")
        print('')
        print()
        print('POSTMAN = OK')
        print('Python 3.7 = OK')
        print('Python Virtual Environment = OK')
        print('Git clone capability = OK')
        print('Webex Team Account = OK')
        print(response)
        print()
        print('====================')
        print('And in addition to this, If you are attending to the 3rd Party Relay Module workshop you absolutelty need :')
        print()
        print('- AWS CLI : https://aws.amazon.com/cli/')
        print('- NGROK : https://ngrok.com/download')
    else:
        print(response.status_code, response.text)
else:
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,'Content-type': 'application/json;charset=utf-8'}
    URL = 'https://api.ciscospark.com/v1/people/me'
    response = requests.get(URL, headers=headers)
    user_email=response.json()['emails']
    display_name=response.json()['displayName']
    print()
    print("STEP 1 OK")
    MESSAGE_TEXT=f'SETUP READY : for {display_name} : {user_email}'
    headers = {'Authorization': 'Bearer ' + thetruc,'Content-type': 'application/json;charset=utf-8'}
    URL = 'https://api.ciscospark.com/v1/messages'
    print("STEP 2 OK")
    print()    
    post_data = {'roomId': ROOM_ID,'text': MESSAGE_TEXT}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        print()
        print(f"SUCCESS : Well Done {display_name} You  are ready for the Python Labs !!")
        print('')
        print()
        print('POSTMAN = OK')
        print('Python 3.7 = OK')
        print('Python Virtual Environment = ERROR. It is not an issue')
        print('Git clone capability = OK')
        print('Webex Team Account = OK')
        print(response)
        print()
        print('====================')
        print('And in addition to this, If you are attending to the 3rd Party Relay Module workshop you absolutelty need :')
        print()
        print('- AWS CLI : https://aws.amazon.com/cli/')
        print('- NGROK : https://ngrok.com/download')
    else:
        print(response.status_code, response.text)