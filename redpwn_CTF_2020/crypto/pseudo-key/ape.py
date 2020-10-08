#! bin/bash/python3
from string import ascii_lowercase
import itertools
from collections import defaultdict


chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
    return ctxt



cipher="iigesssaemk"
key="iigesssaemk"
key = ''.join(key[i % len(key)] for i in range(len(cipher))).lower()
flag=''
posible=[]
for curr in range(0,len(key)):
    posible.append([])
    for y in ascii_lowercase:
        x = chr_to_num[y]
        z = chr_to_num[y]
        if(num_to_chr[(x + z) % 26]==cipher[curr]):
            flag+=y
            if y not in posible[curr]:
                posible[curr].append(y)
posible=list(itertools.product(*posible))
for x in range(0,len(posible)):
    posible[x]=''.join(posible[x])

for choice in posible:
    cipher="z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"
    key=choice
    key = ''.join(key[i % len(key)] for i in range(len(cipher))).lower()
    flag=''
    for curr in range(0,len(cipher)):
        if(cipher[curr]=='_'):
            flag+='_'

        for y in ascii_lowercase:
            x = chr_to_num[y]
            z = chr_to_num[key[curr]]
            if(num_to_chr[(x + z) % 26]==cipher[curr]):
                flag+=y
    print(flag)            