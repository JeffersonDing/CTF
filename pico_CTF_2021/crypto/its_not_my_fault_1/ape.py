
from pwn import *
import hashlib
import secrets


def findstring(stringstart, hashend):
    for x in range(0, 100000000):
        hstring = stringstart + str(x)
        h = str(hashlib.md5(hstring.encode('utf-8')).hexdigest())
        if (h[-len(hashend):] == hashend):
            return hstring


r = remote('mercury.picoctf.net', 48006)
recv = r.recvline(keepends=False).decode()
print(recv)
start = recv[33:38]
hash_end = recv[-6:]
string = findstring(start, hash_end)
r.sendline(string.encode())
r.interactive()
