import requests
import re
url='https://tux-fanpage.2020.redpwnc.tf'
response=requests.get(url)
print(response.text)