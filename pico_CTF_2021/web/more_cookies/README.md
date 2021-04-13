# More Cookies

> Credits to @ZeroDayTea

Somehow, thats challenge was way harder than the `most cookies` challenge. The important observation that the cookie is encrypted using `AES-CBC` which is this case, is vulnerable to a `bit-flipping` attack.
[Reference](https://dr3dd.gitlab.io/cryptography/2019/01/10/simple-AES-CBC-bit-flipping-attack/)

## Method

By looking at the cookie, we see that it's format is actually `admin = 0` which means that we only need to flip one bit and make that a `1`. We see that every character in the base64 cookie will equal to one byte in the ciphertext which by changing we can modify the plaintext. This is because the cookie is encrypted then base64 encoded.  
Using a bruteforce solution, switching out every byte in the original session cookie will result us in the flag.  
By using `python` multithreading, we get the flag almost instantly.
