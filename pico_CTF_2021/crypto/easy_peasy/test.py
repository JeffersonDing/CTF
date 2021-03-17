from pwn import *
conn = remote('mercury.picoctf.net', 36981)
buffer = bytearray([65] * (1000-32))
data = bytearray([65]*1000)
conn.recvuntil("?")
conn.sendline(buffer)

for i in range(0, 49):
    conn.recvuntil("?")
    conn.sendline(data)

conn.interactive()
