# Binary Gauntlet 2

This challenge is very similar to the previous but it doesn't give you the address of the variable to inject shellcode anymore. In this case a `printf` vulnerability could be used for the first input to leak the address of that variable on the stack then we could do the same exploit as the previous challenge.

## Method

To leak addresses on the stack we ues `%p` as a decorator. By experimenting with the binary and some GDB debugging, I found that the variable at `%6$p` is the correct address.
