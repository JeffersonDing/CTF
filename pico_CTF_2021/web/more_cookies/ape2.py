# Credits to @ZeroDayTea from Discord
import requests
import threading
from base64 import b64decode
from base64 import b64encode

# CBC bit flipping attack

s = requests.Session()
url = 'http://mercury.picoctf.net:{}/'.format(
    input("Please enter your port number:"))
# url = 'http://mercury.picoctf.net:34962'
print("Starting enumeration on {}".format(url))
response = s.get(url)
cookie = b64decode(s.cookies['auth_name']).decode()
cookie_len = len(cookie)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
print("initial cookie:{}".format(cookie))
found = False
flag = ''


def getNewCookie(i, char, cookie):
    return b64encode((cookie[:i] + char + cookie[i + 1:]).encode()).decode()


def testCookie(i):
    global found
    global flag
    for char in alphabet:
        if(found):
            exit()
        newcookie = getNewCookie(i, char, cookie)
        cookies_dict = {'auth_name': newcookie}
        response = requests.get(
            url, cookies=cookies_dict)
        # print("{}|testing:{}".format(i, newcookie))
        if "pico" in response.content.decode():
            found = True
            print("found cookie:{}".format(newcookie))
            flag = response.content.decode().split(
                "<code>")[1].split("</code>")[0]
            exit()


threads = []

for i in range(0, cookie_len):
    t = threading.Thread(target=testCookie, args=[i])
    t.daemon = True
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    try:
        thread.join()
    except:
        continue
print(flag)
