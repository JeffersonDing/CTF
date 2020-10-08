# bubbly
By running `file` on the binary, we see something very interesting.
```
bubbly: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=edb56d2d9355bcee01909f171d8a272a3e82d053, with debug_info, not stripped
```
This binary is not strippe and also contains `debug_info` which makes it pretty easy to reverse.
# Decompiler
By putting the binary in `ghydra` and analyzing the code, we get a sence of what the functinos do. There are 2 main functions we care about `main` and `check`.
I converted the functions and arguments into python code and here's the logic behind the binary
```python
p=False
import operator
def check():
    i=0
    while(True):
        if(8<i):
            return True
        if(nums[i+1]<nums[i]):
            break
        i+=1
    return False

while(True):
    n=int(input())
    if(n>8):
        break
    nums[n]=operator.xor(nums[n],nums[n+1])
    nums[n+1]=operator.xor(nums[n+1],nums[n])
    nums[n]=operator.xor(nums[n],nums[n+1])
    print(nums)
    p=check()
if(p):
    print("got it")
else:
    print("nope")
```
These are some lines that we do care about.  
This is the condition where `check()` doesn't break and when `i` increments over 8 returns true. 
```python
if(nums[i+1]<nums[i]):
```
By doing some experiments, we know that this is just changin the order of `nums[n]` and `nums[n+1]` by running `XOR` 3 times.
```python
nums[n]=operator.xor(nums[n],nums[n+1])
nums[n+1]=operator.xor(nums[n+1],nums[n])
nums[n]=operator.xor(nums[n],nums[n+1])
```
So if we want `check` to return true, we need to make every element in `nums` greater than the previous element in `nums`. Basically in incremental order.
## nums
We need to set nums, but what is nums? Well it's just a variable stored in memory, since we have full access to the memory of the binary, we could use `gdb` and find out the values of `nums`
```bash
> x/24wx nums

0x4060 <nums>:   0x00000001 0x0000000a 0x00000003 0x00000002
0x4070 <nums+16>:0x00000005 0x00000009 0x00000008 0x00000007
0x4080 <nums+32>:0x00000004 0x00000006 Cannot access memory at address 0x4088
```
So we can see that there are `10` elements in `nums` and we could convert the hex to decimal by hand since they are pretty small.
Here's what I got.
```python
nums=[1,10,3,2,5,9,8,7,4,6]
```
What we need to do now is find a series of indexes and swap the element at `i` and `i+1` and ultimately sort the array.
## The Exploit
By keeping track of the array on a piece of paper, I was able to find the set of moves to sort nums and triger `check` to return `true`.
```
I hate my data structures class! Why can't I just sort by hand?
1
2
1
7
6
5
4
3
4
8
7
6
5
8
7
6
8
7
8
10
Well done!

flag{4ft3r_y0u_put_u54c0_0n_y0ur_c011ege_4pp5_y0u_5t1ll_h4ve_t0_d0_th15_57uff}
```