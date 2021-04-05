import requests
url = "http://mercury.picoctf.net:46199/"

headers = {
    "Host": "mercury.picoctf.net:46199",
    "User-Agent": "PicoBrowser",
    "Accept-Language": "sv-sv",
    "X-Forwarded-For": "31.15.32.0",
    "DNT": "1",
    "Referer": "http://mercury.picoctf.net:46199",
    "Date": "2018",
}
r = requests.get(url, headers=headers)
# print(r.text)
print(r.text.split("<b>")[1].split("</b>")[0])
