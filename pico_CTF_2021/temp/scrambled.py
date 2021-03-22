from pwn import *
import string

chars = string.ascii_letters+string.digits+"_-\{\}"

decrypted_flag = ''
known = []
r = remote("mercury.picoctf.net", 4484)
flag = r.recvline(keepends=False).decode()[6:]
r.recvline()
r.recvline()

while '}' not in decrypted_flag:
    for i in chars:
        payload = decrypted_flag+i
        r.sendafter("me: ", payload+"\n")
        enc = r.recvline(keepends=False).decode().split("Here you go: ")[1]
        for chunks in known:
            enc = enc.replace(chunks, '')
        if(enc in flag):
            flag = flag.replace(enc, '')
            known.append(enc)
            decrypted_flag += i
            print(decrypted_flag)
            break
