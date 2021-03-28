gogo procedure

1. Load it into binary ninja and we see that there are two byte arrays of length 32 bytes that are XORed with each other to give us the password
2. One of them is referred elsewhere. This gives you password 1
3. Then, the program will execute another function and you need to convert the byte array to ascii
4. It is a MD5 hash and cracking the hash will give you the second password.
5. Enter both of them one by one when prompted and you get the flag.
