# Binary Gauntlet 1

Throwing the program into `Ghidra` we can see the decompiled main function. It's functionality is quite simple. By running the binary, we see that it prints out a hex value and looking at the source, we see that it's actually an address for a variable we use later. Then the program expects 2 inputs and we see that we are able to overflow to `RAX` and due the the `strcpy()` function, we will inject shellcode to the address leaked in the first line.

## Method

Using `pwntools` we can easily assemble the shellcode but we need to determine the offset to overwrite RAX. Using the `pwn cyclic` tool we can generate a piece of string as input and use GDB to find the correct offset. After that, we just need to remove the length of the shellcode from the buffer and send that off to the binary.
