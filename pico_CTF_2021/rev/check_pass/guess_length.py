from pwn import *

context.log_level = 'critical'


for i in range(0, 50):
    p = process(['./checkpass', 'A'*i])
    out = p.recvall().decode()
    if 'length' not in out:
        print("Found! Length: {}".format(i))
