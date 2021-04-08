# Double DES

This is a `meet in the middle` attack on DES. The program allows us to encrypt arbitrary data in which it returns the encrypted data after double DES encryption.

## Intuition

The intuition here is that we know the key size is not that large since the key is only 6 characters long we could simply try every possible key on the input as well as the output. Anything that matches means that this pair of keys is the correct one.

## Method

Initially, I though that we would need many input interactions to narrow it down to a reasonable dictionary size but after only 1 character `A` there were only around 64 valid key pairs left. I just brute forced the flag and it seems like all 64 pairs work to decrypt the ciphertext given.
