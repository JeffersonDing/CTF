# itsy-bitsy
For this question, we were given a script and a netcat connection to work with. We want to recover the flag with the encrypted flag printed out by the programme.
## Examine the Source Code
```python
n = len(flag_bits)
random_bits = generate_random_bits(lb,ub,n)
encrypted_bits = bit_str_xor(flag_bits,random_bits)
print(f'Ciphertext: {encrypted_bits}')
```
this is the core encryption call to encryption function. We can see that it gets the length of the `flag_bits` and genrates some random bits based on our `i` and `j` input. Then it sends these values to a bitwise XOR encryption.
```
XOR Demonstration
rnd  = 10100101
flag = 10110111

    10110101
XOR 10110111
--------------
    00000010
```
## The Random Generator
It would be imposible to solve this question if the programm really genrerates random bits to XOR against the flag. We do have some control over the genreation of the bits and thats where we find our exploit/
```python
i,j = recv_input()
lb = 2**i
ub = 2**j - 1
random_bits = generate_random_bits(lb,ub,n)
def generate_random_bits(lower_bound, upper_bound, number_of_bits):
    bit_str = ''
    while len(bit_str) < number_of_bits:
        r = randint(lower_bound, upper_bound)
        bit_str += bin(r)[2:]    
    return bit_str[:number_of_bits]
```
The program first takes in an input of `i` and `j` but `j>i>0`. It calculates an upper bound and lower bound by raising `2` to the `i` and `2` to the `j` minus one. Then it sends the `ub` and `lb` along with the number of bits to the genreation. Here the `number_of_bits` is just the flag length, which is `301`.(I found it by doing `len(n)`).

In the `generate_random_bits` function, we first get an random integer bounded by the `ub` and `lb` then it just turs that integer in to binary bits and appends it to the random bits.
## Finding Patterns
The only control over the program is `i` and `j`. Theres a number of things we need to notice
* We don't want a huge range of `i` and `j` since we don't want the `randint()` to gives us too unpredictable results
* We have to follow the rules of `j>i>0`. I was initially thinking about setting `i` and `j` equal so that we could get huge chunk of all `1`'s in the random bits
* There are some special things about `j` since the `ub` is determined by `2**j -1` not `2**j`
  
___
Based on these observation I started to test the inputs `i` and `j` and I saw some patterns.
| i | j | bin(2**i)|bin(2**j-1)|
|---|---|---|---|
| 1 | 2 | 10| 11 |
| 2 |3  |100|111|
| 3 |4  |1000|1111|
Do we see some patterns here? If we list out all the posibilities of binary `ub` and `lb` for each group, we can see that they always have the same amount of digits, where the first digit always seem to be `1`.
To verify this though, I wrote a test script that will list out all the possibilities for each char(7 bits) in the case of `i=1` and `j=2`. This is what I got
```python
even=[0b1111111,0b1111110,0b1111011,0b1111010,0b1101111,0b1101110,0b1101011,0b1101010,0b0111111,0b0111110,0b0111011,0b0111010,0b0101111,0b0101110,0b0101011,0b0101010]

odd=[0b1111111,0b1111101,0b1110111,0b1110101,0b1011111,0b1011101,0b1010111,0b1010101]
```
and if we lay it out vertically indeed we can see that every 2nd bit is always a `1` no matter what.
```
odd
1 1 1 1 1 1 1
1 1 1 1 1 0 1
1 1 1 0 1 1 1
1 1 1 0 1 0 1
1 0 1 1 1 1 1
1 0 1 1 1 0 1
1 0 1 0 1 1 1
1 0 1 0 1 0 1

even
1 1 1 1 1 1 1
1 1 1 1 1 1 0
1 1 1 1 0 1 1
1 1 1 1 0 1 0
1 1 0 1 1 1 1
1 1 0 1 1 1 0
1 1 0 1 0 1 1
1 1 0 1 0 1 0
0 1 1 1 1 1 1
0 1 1 1 1 1 0
0 1 1 1 0 1 1
0 1 1 1 0 1 0
0 1 0 1 1 1 1
0 1 0 1 1 1 0
0 1 0 1 0 1 1
0 1 0 1 0 1 0
```
This is the case because any integer from the range `2**i` to `2**j-1` always start with a one and they are all the same length for example:
```
i = 3
j = 4
2**i = 8
2**j -1 = 15
8       9       10      11      12      13      14      15
1000    1001    1010    1011    1100    1101    1110    1111
```
So now we know that for each pair of `i` we have `j = i+1` and we get to know each `j` bits for certain!
## The Exlpoit
For the `301` bits we need to get, we need to run all the way up to `i=300` and `j=301` and we need to have a way to save the answers of `1^flag[i]` to a buffer. I wrote a scrip that will handle everything.
```python
from pwn import *
context.log_level = 'error'
def BinaryToDecimal(binary): 

	string = int(binary, 2) 
	return string 

def Bin2Str(bin):
    str_data =' ' 
    for i in range(0, len(bin), 7): 
    	temp_data = bin[i:i + 7] 
    	decimal_data = BinaryToDecimal(temp_data) 
    	str_data = str_data + chr(decimal_data) 
    return str_data


ans=['0']*301
host,port='2020.redpwnc.tf',31284
for i in range(1,300):
    print("Getting Every "+str(i+1)+" Bits")
    s = remote(host,port)
    s.sendline(str(i))
    s.sendline(str(i+1))
    res=s.recvline()
    res=list(str(res).replace("b'Enter an integer i such that i > 0: Enter an integer j such that j > i > 0: Ciphertext: ","").replace("\\n'",''))
    for j in range(len(res)):
        if(j%(i+1)==0):
            ans[j]=str(int(res[j])^1)
    print(Bin2Str(''.join(ans)))
print(''.join(ans))
```
