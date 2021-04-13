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
cookie = s.cookies['auth_name']
cookie_len = len(b64decode(b64decode(cookie)))
print("initial cookie:{}".format(cookie))
found = False
flag = ['\033[91m', '', '\033[0m']

# Reference: https://crypto.stackexchange.com/questions/66085/bit-flipping-attack-on-cbc-mode
# Modified for double base64


def bitFlip(position, bit, cookie):
    raw = bytearray(b64decode(b64decode(cookie).decode()))
    raw[position] = raw[position] ^ bit
    raw = bytes(raw)
    return b64encode(b64encode(raw)).decode()


def testCookie(i):
    global found
    global flag
    for j in range(cookie_len):
        if(found):
            exit()
        newcookie = bitFlip(i, j, cookie)
        cookies_dict = {'auth_name': newcookie}
        response = requests.get(
            url, cookies=cookies_dict)
        # print("{}|testing:{}".format(i, newcookie))
        if "pico" in response.content.decode():
            found = True
            print("\033[92mfound cookie:{}\033[0m".format(newcookie))
            flag[1] = response.content.decode().split(
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
print(''.join(flag))
