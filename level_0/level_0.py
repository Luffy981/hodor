#!/usr/bin/python3
import requests

success_votes = 0
user_id = 3344
number_print = 1024
url = 'http://158.69.76.135/level0.php'
votation = {'id': user_id, 'holdthedoor': 'Submit'}

for i in range(0, number_print):
    r = requests.post(url, data=votation)
    print(r.status_code)
    if r.status_code == 200:
        print("print success: {}".format(success_votes))
        success_votes += 1
