# Scrambled RSA

The questions provides a netcat connection and provides a ciphered `flag` the public modulus `n` and the public exponent `e`. The program also allows you to provide input in which it will output the encrypted form.

## Testing

Credits to `@ers123` I was able to find a pattern when encrypting different strings. First tried to encrypt `1` then `12` then `123`. You will see that the output of each contains the previous which means that the flag is simply composed of the flag characters encrypted but scrambled.

## The Method

The method is to store the flag in a string and brute force each character of the flag. First, we send every printable character to the program and check which one is in the flag, that would be the first character. Then, we add on to that "leaked" flag by adding another character and by removing the previously found character(encrypted integer) we can then compare that number to the flag string. By doing this repeatedly, we end up with a flag.
