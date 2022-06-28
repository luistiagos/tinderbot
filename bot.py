import requests
import time
import sys
import gender_guesser.detector as gender

sys.setrecursionlimit(999999999)

KEY = ''
url = 'https://api.gotinder.com/v2/recs/core?locale=pt'
headers = {"Content-Type": "application/json; charset=utf-8",
           "x-auth-token": KEY}

def likes():
    response = requests.get(url, headers=headers)
    try:
        data = response.json()['data']
        for r in data['results']:
            try:
                userid = r['user']['_id']
                print(r['user']['name'])
                requests.get('https://api.gotinder.com/like/' + userid + '?locale=pt', headers=headers)
                time.sleep(2)
            except:
                time.sleep(10)
    except:
        time.sleep(10)
        pass
    likes()
    
likes()