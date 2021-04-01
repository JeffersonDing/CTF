# Mini RSA

This mini RSA question is not like previously seen ones where we could simply apply a cube root attack. Due to padding, `m^e` is actually larger than the public modulus.

## Method

Although we cannot run a cube root attack, we do realize that `e` is only `3` and `m^e` is barely larger than `n` we could see brute force the plaintext by just trying to add the public modulus.

```
RSA encryption uses : c = m^e mod n
RSA decryption could use: p = (c+xn)^(1/e)
```

Here, `x` is probably not so large so we can test that theory out. Initially, I used the `decimal` python module but the results were not accurate enough thus not giving me a flag. I move on to use a `sage math` kernel which handles numbers way better than python and it gave me the flag with ease.
