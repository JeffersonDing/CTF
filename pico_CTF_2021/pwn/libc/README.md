# Here's a libc

This is a classic `ret2libc` challenge and I have a script to handle it. We just need to find the offset and calculate stack alignment using the leaked `puts` address.

## Method

Using GDB peda and `pwn cyclic` we can easily find the offset of `136`. Then by calling `puts` on `puts` we leak the address of it. Comparing it to the provided `libc.so.6` location of `puts` we can calculate the base address of libc. The we just need to assemble a ROP chain that calls `one gadget` which pops a shell for us.
