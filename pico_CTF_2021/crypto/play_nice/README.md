# Play Nice

I've use a brute-force approach to solve this problem, but I'm sure there is an intended way to solve it.

## Method

The mechanism encryptes messages statically, that means that if I encrypted the character `a`, the output will always be the same. If the input length is odd, it will add `l` as padding but the encrypted flag seems to map to an even number. This means that a certain combination of 2 letters will always result in the desired letters in the ciphertext.

## Script

I used a nested for loop to iterate through all 2 letter combinations and encrypt that using the algorithm. If it matches the corresponding chunk on the ciphertext, we found the original characters, which we could use to build up the flag.
