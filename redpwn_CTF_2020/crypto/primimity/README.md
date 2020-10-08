# primimity
This challenges gives us the `n` and `e` in a RSA encryption. And it tells us that `n` consists of 3 1024-bit primes. In this case, we probably can't factor `n` with Crypto tools and by checking factordb, there is no entry of `n`. So we need to start from the prime-generation python script.
## The Script
```python
def prime_gen():
    i = getRandomNBitInteger(1024)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    p = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    q = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    r = find_next_prime(i)
    return (p,q,r)
```
this is the prime genration function of the script and we can see how it works. First in generates a random 1024 bit integer to form the base of the random generation. Then for three primes, it generates an 8 bit integer and finds the next_integer after the 1024 base integer that many times.   
What can se spot here? Like the name suggests, I kind of get of sence of "proximity". This is because all three primes are generated base off one 1024 bit random integer, and the only thing thats different between the three primes are how many times `next_prime` is called. An 8 bit integer can be `0-255` which is not that much. So the biggest gap between each prime is `255` primes away. 
## The Exploit
By knowing that these primes are close to each other, we could just write something that goes around the cube root of `n` and check each prime around the range of `+-255` primes. This is tedious work so I wrote a script to handle that. We check each prime by `n%found_prime == 0` and it's a factor of n, we found a factor of `n`. Notice we only need 2 out of 3 primes to find all of them. In my case, I was only able to get 2 primes, but that gives me the third one as well.We know that one is above the cube root and one is below, we could just find the third one by division.
```python
curr = # Cube root of n, skiped to save space
for x in range(300):
    curr=find_prev_prime(curr)
    posible.append(curr)

curr = # Cube root of n, skiped to save space
for x in range(300):
    curr=find_next_prime(curr)
    posible.append(curr)

ans=[]
for x in posible:
    if(n%x==0):
        ans.append(x)

curr = # Cube root of n, skiped to save space
for x in range(curr,n):
    if(new*x==n):
        ans.append(x)
        break

curr = # Cube root of n, skiped to save space
for x in range(curr,n,-1):
    if(new*x==n):
        ans.append(x)
        break
print(ans)
```
I modified the `find_next_prime` function to find the previous prime so that we get a range of `+-256`. Then we just wait for the primes to get calculated. 
## The Flag
Finally, we get the three primes we could just do our regular RSA decryption by finding the totient and the moduler inverse of `e` and `phi`
```python
from Crypto.Util.number import inverse
p,q,r=139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409208581,139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409397803,139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409494847
n=# Deleted to Save Space
e=65537
c= # Deleted to Save Space
phi = (p-1)*(q-1)*(r-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(hex(m))
```