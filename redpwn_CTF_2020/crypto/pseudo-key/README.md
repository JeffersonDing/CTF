# pseudo-key
This crypto challenge is all about reversing the encryption. The problem provided us with the encryption method, since each char in the ciphertext and plaintext is encrypted independantly, and does not change according to other characters in the string, i like to run all possible readable strings on the cipher text. This way, we could check our output and see if it gives us a readable answer. I'll say this is NOT the best way of solving this challenge, but it saves some time on reversing the encryption.
## Understanding the Code
The million dollar question here is to understand the core code.
```python
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
```
This is the encrypte function, it takes a plain text and key and returns a cipher text. The key is cycled to match the length of the plain text and then the encryption starts. The two paralle arrays elements at `i` will get converted into a number then the cipher text is just the sum of them mod 26 back to a char.  
By using my method of guessing all the posible chars, I don't really need to understand and reverse the algorithem since the programe does the work.
## Solution
```python
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
```
First we run key to key, we get all posible keys. Then we run this againts the cipher text. 
## Get the flag
To get the flag, we need a bit of searching and guessing. By looking at the output, we can summarize the flag to readable words.
## Flag
`flag{i_guess_pseudo_keys_are_pseudo_secure}`
