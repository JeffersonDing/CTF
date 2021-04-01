# New Caesar

I use a brute force script to complete the challenge due to the small alphabet size.

## Method

Since the key of this cipher is only 1 character long and the flag is encrypted statically(each character is encrypted independently) we are able to simply try all keys and printable characters and see which one matches the desired output. By keeping a count of how many times the key worked, we know that only the the key that worked for all 39 characters in the flag is the real key thus giving us the output.
Due to a small alphabet size, the script runs almost instantly.
