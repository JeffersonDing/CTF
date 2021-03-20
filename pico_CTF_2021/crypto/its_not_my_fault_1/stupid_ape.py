from pwn import *
import hashlib
import secrets
r = remote('mercury.picoctf.net', 48006)
recv = r.recvline(keepends=False).decode()
print(recv)
start = recv[33:38]
hash_end = recv[-6:]
flag = True
while (flag):
    junk = secrets.token_hex(nbytes=16)
    str = "{}{}".format(start, junk)
    result = hashlib.md5(str.encode()).hexdigest()
    log.info("Running! Goal:{} Current:{}".format(hash_end, result[-6:]))
    if(result[-6:] == hash_end):
        log.info("found! {}".format(result))
        flag = False
        r.interactive()
        break
