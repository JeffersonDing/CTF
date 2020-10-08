import itertools
posible=[
[11,10],
[11,10],
[11,10],
]
odd=[]
even=[]
for x in itertools.product(posible[0],posible[1],posible[2]):
    curr=''
    for y in x:
        curr+=str(y)
    curr+="1"
    odd.append(curr)

posible=[
[1,0],
[11,10],
[11,10],
[11,10]

]

for x in itertools.product(posible[0],posible[1],posible[2],posible[3]):
    curr=''
    for y in x:
        curr+=str(y)
    even.append(curr)
for x in even:
    print(x)
#print(odd)