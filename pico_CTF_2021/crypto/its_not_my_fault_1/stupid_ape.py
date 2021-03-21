from pwn import *
import hashlib
import secrets
r = remote('mercury.picoctf.net', 48006)
recv = r.recvline(keepends=False).decode()
print(recv)
start = recv[33:38]
hash_end = recv[-6:]
flag = True
i = 0
while (flag):
    str = "{}{}".format(start, i)
    result = hashlib.md5(str.encode()).hexdigest()
    log.info("Running! Goal:{} Current:{}".format(hash_end, result[-6:]))
    i += 1
    if(result[-6:] == hash_end):
        log.info("found! {}".format(result))
        flag = False
        r.interactive()
        break
