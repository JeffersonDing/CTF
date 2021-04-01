# No Padding No Problem

[Attacking RSA for fun and CTF points – part 1](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-1/)

The provided netcat connection gives the public modulus `n` and public exponent `e` as well as the `ciphertext`. This is also a Oracle because we can provide come ciphertext and the program will decrypt it for us.  
Reading Bitsdeep's article on RSA Oracle, we could multiply the ciphertext my another cipher text `c2` which me know the plain text of and recover the decrypted `c1` ciphertext. Heres how the math works: `C = c*c_2 = M^e*2^e = 2M^e`. So we just need to divide the returned plaintext by 2 to get the deciphered flag.

## Script

Using `pwntools` we could easily store and manipulate given data as well as enter data to the `nc` connection.
