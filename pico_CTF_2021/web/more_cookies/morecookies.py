# CBC bit flipping attack
import requests

s = requests.Session()

response = s.get('http://mercury.picoctf.net:34962/')
cookie = s.cookies['auth_name']
print(s.cookies)
print(cookie)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
for i in range(0, len(cookie)):
    for alphchar in alphabet:
        newcookie = cookie[:i] + alphchar + cookie[i + 1:]
        print(newcookie)
        cookies_dict = {'auth_name': newcookie}
        response = requests.get(
            'http://mercury.picoctf.net:34962/', cookies=cookies_dict)
        if 'pico' in response.content:
            print("**********************")
            print(response.content)
            print(newcookie)
            exit()
