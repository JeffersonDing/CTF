from pwn import *
p = remote('mercury.picoctf.net', 23584)  # process("./rop")
p.sendlineafter("sErVeR!", b'hello')
p.interactive()
