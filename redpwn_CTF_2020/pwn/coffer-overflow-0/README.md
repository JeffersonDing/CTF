# coffer-overflow-0
This is a typical first `buffer overflow` question. We were given a biary, the source code and a remote server to connect to.
## By Experienc
If you often attend CTF's I would probably guess that this is just a plain `buffer overflow` so I just jammed the netcat server with quite some `A`'s and surely it gave me a shell to cat out the `flag.txt`
## The source
The exploit here it the `gets()` function. The `gets()` function doesn't care about how many it's taking it, it just throws it on the stack, so if we have a long enought input for gets, we could overflow the constant `code` and change it's value.
```cpp
long code = 0;
char name[16];
puts("Welcome to coffer overflow, where our coffers are overfilling with bytes ;)");
puts("What do you want to fill your coffer with?");
gets(name);
```
## The Flag
We get a remote shell when the exploit is done, and by running `ls` we can see that there is a `flag.txt`. We could just `cat` out the file.
```bash
cat flag.txt
flag{b0ffer_0verf10w_3asy_as_123}
```