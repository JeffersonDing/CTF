from base64 import b64decode
from base64 import b64encode
import requests


def bitFlip(pos, bit, data):
    raw = bytearray(b64decode(b64decode(data).decode()))
    raw[pos] = raw[pos] ^ bit
    raw = bytes(raw)
    return b64encode(b64encode(raw)).decode()


ck = "UXVDRDhEMmNrbTFCV25jbzdheFBjbHNmOWErZnNJdnY5Nk5pUkVNTkVXYUdRK0FVSk9tTGtRT3h1a0dWSDJrbmNHSUxsRTlNR2FZZFJaZ3RRb09EdngyUnd6L3FlbCtPSmZjbnJUVE5pWnVVUHNDQ1lJdFkzbTI4N29NWWxBRU4="

for i in range(96):
    for j in range(96):
        print("position:{},bit={}".format(i, j))
        c = bitFlip(i, j, ck)
        cookies = {'auth_name': c}
        r = requests.get('http://mercury.picoctf.net:34962/', cookies=cookies)
        if "picoCTF{" in r.text:
            print(r.text)
            break
