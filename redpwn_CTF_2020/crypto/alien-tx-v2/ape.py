from collections import *
encrypted = open("encrypted.txt", 'r').read().strip().split('\n')
bins=defaultdict(list)
k399=[0]*399
k21=[[]]*21
k19=[[]]*19
for x in range(len(encrypted)):
    bins[x%399].append(encrypted[x])


for x in range(0,399):
    count = Counter(bins[x])
    delim = list(count.keys())[list(count.values()).index(max(list(count.values())))]
    k399[x]=int(delim)^481

#for c in range(0, 255):
#    for idx in range(0, 399, 21):
#        k19p = k399[idx] ^ c        
#        if(k19p>2**6 and k19p<2**7):
with open("ape1.txt", 'w') as f:
    with open("ape.txt",'w') as j:
        for c in range(0, 255):
            for idx in range(0, 399, 21):
                k19[idx % 19] = k399[idx] ^ c
            for i in range(0,399):
                k21[i % 21]=k19[i%19]^k399[i]
            j.write("".join([chr(c) for c in k21])+"".join([chr(c) for c in k19])+'\n')