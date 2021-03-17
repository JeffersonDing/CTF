from pwn import *
conn = remote('mercury.picoctf.net',21135)

data = conn.recv().decode('utf-8').split('\n')
data.pop()
for i in data:
    print(chr(int(i)), end = '')