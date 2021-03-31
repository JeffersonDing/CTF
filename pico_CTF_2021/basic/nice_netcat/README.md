# Nice Netcat

This is quite a simple challenge, given a `netcat` connection we can see that the connection prints out many numbers.  
Looking at these numbers we can see that they all fall in the decimal representation of ASCII printable characters and true enough, the first couple numbers correspond to `pic` which is the flag format.

# Script

We could potentially manually take these numbers and convert them into ASCII but we could also use `pwntools` to automate this process. To do so, I received all the output from the connection and split it by new line characters and used the python `chr` function to convert integers so it's ASCII representation.
