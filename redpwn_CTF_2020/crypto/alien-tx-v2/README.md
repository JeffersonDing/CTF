# alien tx v2
We are provede with an explanation that has some key points and a file that contains the doble XOR encrypted message.
```
The aliens are at it again! We've discovered that their communications are in base 512 and have transcribed them in base 10. However, it seems like they used XOR encryption twice with two different keys! We do have some information:

    This alien language consists of words delimitated by the character represented as 481
    The two keys appear to be of length 21 and 19
    The value of each character in these keys does not exceed 255

Find these two keys for me; concatenate their ASCII encodings and wrap it in the flag format.
```
Our goal here is to recover the two keys but not the message. So we could leverage the message and the special factors of the alens language to "guess" the keys.
## Effective Key Length
By doing an XOR encryption with a key length of 21 and 19, we have a effective key length of `21*19=399`. This means that the text will be encrypted by the same key every 399 chars. Heres a visualization.
```
key1 = 101
key2 = 11010
plaintext = 00000
    First XOR with key1
    
    10110 ('101' plus '10' to fill the length of the plaintext)
XOR 00000
------------------
    10110

    Second XOR with key2

    10110
XOR 11010
------------------
    01100
```
You can see the result more clearly with a test script `@GeoffreyY(Discord)` showed me
```python
from itertools import cycle
key1 = [1,2,3]
key2 = [4,5,6,7,8]
ptxt = [0]*50
[z^k1^k2 for ((z,k1),k2) in zip(zip(ptxt,cycle(key1),cycle(key2)))]

OUTPUT:
[
5,7,5,6,10,7,4,4,4,9,6,6,7,5,11
5,7,5,6,10,7,4,4,4,9,6,6,7,5,11
5,7,5,6,10
]
```
## Sorting
After we determine the effective key length, we could sort the provide alien message into 399 different bins, as each bin is using the same key to encrypt the data. To do this, a python script could do the job, this will be included in the final exploit.
```python
from collections import *
encrypted = open("encrypted.txt", 'r').read().strip().split('\n')
bins=defaultdict(list)
k399=[0]*399
k21=[[]]*21
k19=[[]]*19
for x in range(len(encrypted)):
    bins[x%399].append(encrypted[x])
```
## Finding Deliminators
By the provided imformation about the alien language, we know that the deliminator is `481` and that should be the most common "word" in each bin. By using the `Counter()` in itertools, we can see that there is always a significant difference between the most used word and the second most used word. Therefore, we could tell that the most used word in each bin should be `481`. Now we need a piece of script to pick out these deliminators.
```python
for x in range(0,399):
    count = Counter(bins[x])
        delim = list(count.keys())[list(count.values()).index(max(list(count.values())))]
    k399[x]=int(delim)^481
```
After finding the deliminators, by XORing it with `481` the knowned deliminator, we can get the encryption key for `k399[i]`
## "Brute Forcing" the Keys
We know the relation of `key399`, `key21` and `key19` by examining the test script @GeoffreyY wrote which is `key399[i] = key21[i % 21] ^ key19[i % 19]`  
By knowing this imformation in addition to the other specification of the alien language `The value of each character in these keys does not exceed 255` we can try every value between `0 ~ 255`. Since we know all `k399` by finding the deliminators, we just need to guess a value for `k21` or `k19` and see if the other one makes sence, since we want our final output to be readable characters. I wrote this script that will write all the posibilities of `k19` when `k21` is a certain value, and evaluate `k21` with the found `k19` value and `k399`.
```python
with open("ape1.txt", 'w') as f:
    with open("ape.txt",'w') as j:
        for c in range(0, 255):
            for idx in range(0, 399, 21):
                k19[idx % 19] = k399[idx] ^ c
            f.write("".join([chr(c) for c in k19]) + '\n')
            for i in range(0,399):
                k21[i % 21]=k19[i%19]^k399[i]
            j.write("".join([chr(c) for c in k21])+"".join([chr(c) for c in k19])+'\n')
```
## Final Output and Finding the Flag
For our output, we get a huge list of characters and we need to find the one that "looks" right.
```
.
.
.(Giberish)
e>>*8Rye>Rk<8yRe9akRye>R8>n=ciR<8Rye<8
f=|=);Qzf=Qh?|;zQf:bhQzf=Q;=m>`jQ?;Qzf?;
g<}<(:P{g<Pi>}:{Pg;ciP{g<P:<l?akP>:P{g>:
h3r3'5_th3_f1r5t_h4lf_th3_53c0nd_15_th15
i2s2&4^ui2^g0s4u^i5mg^ui2^42b1oe^04^ui04
j1p1%7]vj1]d3p7v]j6nd]vj1]71a2lf]37]vj37
k0q0$6\wk0\e2q6w\k7oe\wk0\60`3mg\26\wk26
.(Giberish)
.
.
```
Just find the string that "Seems" like the flag, you should be able to spot it!

