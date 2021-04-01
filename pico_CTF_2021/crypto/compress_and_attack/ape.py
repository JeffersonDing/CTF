from pwn import *

possibilities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}{"

r = remote("mercury.picoctf.net", 2431)

flag = "picoCTF{"
compressLen = 49  # found by testing the first character
while "}" not in flag:
    for i in range(len(possibilities)):
        f = flag+possibilities[i]
        r.sendline(f)
        r.readline()
        r.readline()
        n = r.readline()
        l = int([int(word) for word in n.split() if word.isdigit()][0])
        print(f)
        # print(l)
        if l < compressLen:
            flag = f
            break
