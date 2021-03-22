from pwn import *

possibilities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}{"

r = remote("mercury.picoctf.net", 2431)

flag = ""
compressLen = 99999999
for i in range(len(possibilities)):
    f = "picoCTF{}sheriff_you_solved_the_crime{}".format('{', possibilities[i])
    r.sendline(f)
    r.readline()
    r.readline()
    n = r.readline()
    l = int([int(word) for word in n.split() if word.isdigit()][0])
    print(f)
    print(n)
    print(l)
    if l < compressLen:
        compressLen = l
        flag = f

print(flag)
