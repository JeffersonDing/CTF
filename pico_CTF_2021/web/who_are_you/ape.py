import requests
url = "http://mercury.picoctf.net:46199/"

headers = {
    "Host": "mercury.picoctf.net:46199",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "PicoBrowser",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    "Cookie": "name=18",
    "Origin": "http://mercury.picoctf.net:46199"
}
r = requests.get(url, headers=headers)
print(r.headers)
print(r.text.split("<h3 style=\"color:red\">")[1].split('</h3>')[0])
