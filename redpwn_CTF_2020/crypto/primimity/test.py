#!/usr/bin/env python3

from Crypto.Util.number import getRandomNBitInteger, isPrime

def find_next_prime(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        while not isPrime(n):
            n += 2
        return n
    
def prime_gen():
    i = getRandomNBitInteger(1024)#Gets 1024 bit rnd int
    
    
    d = getRandomNBitInteger(8)#Gets 8 bit rnd int
    for _ in range(d):
        i = find_next_prime(i) # Find next prime d times
    p = find_next_prime(i) #Find next prime again (d+1) times
    
    
    d = getRandomNBitInteger(8)#Gets 8 bit new value
    for _ in range(d):
        i = find_next_prime(i)# Find next prime d times
    q = find_next_prime(i)
    
    
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    r = find_next_prime(i)
    
    return (p,q,r)
