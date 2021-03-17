from pwn import *
conn = remote('mercury.picoctf.net', 36981)
buffer1 = bytearray([65] * (4000-32))
buffer2 = bytearray([65] * 4000)
buffer3 = bytearray([65] * 2000)
payload = bytearray([65] * 32)
conn.recvline()
conn.recvline()
flag_e = conn.recvline().decode('utf-8')
conn.recvuntil("?")
conn.sendline(buffer1)
for i in range(0, 11):
    conn.recvuntil("?")
    conn.sendline(buffer2)
conn.recvuntil("?")
conn.sendline(buffer3)
conn.recvuntil("?")
conn.sendline(payload)
conn.recvline()
leaked = conn.recvline()
leaked = leaked.decode('utf-8')


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


flag = splitStr(2, flag_e)
flag.pop()
leaked = splitStr(2, leaked)
leaked.pop()
print("picoCTF{", end='')
for i in range(len(leaked)):
    key = int(leaked[i], 16) ^ 65
    p = int(flag[i], 16)
    print(chr(p ^ key), end='')
print("}", end='')
