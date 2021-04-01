# New Vignere

This is a new implementation of the Vignere cipher which involves the `b16_encode`. There is a couple of important aspects to notice and overcome in order to solve this challenge.

## Cryptographic Analysis

### Key Length

Looking at the `b16_encode` function of the program, we can see an vulnerability that allows us to not only determine the key length, also the shift that's done to each key.  
If we encrypt all of the characters that could be in the potential flag `abc0123456def789` we see that due to the `b16_encode` function cutting the 8 bit binary data into two pieces, the first part always stays rather consistent where all letters start with `g` and numbers start with `d`.  
This means no matter what the key is, which determines the shift, each encrypted chunk has a pattern of only consisting of no more than 2 distinct characters.  
Using the key_length script we test out all possible key lengths and redirect that into a text file to analyze and at a key length of `9` we see such pattern.

```text
lejjlnjmj
ndkmjinki
lbmlljjkm
nakmmighh
ocmllojhj
maijpiohn
lojmokjkj
a
```

Notice how the first column only has `l` and `o` on odd positions and the second column only has `d` and `a` on even positions? This exactly matches the original `b_16` pattern and we have found our key length.

### Potential Key

To find the potential key, we are able to continue on the vulnerabilyty on the `b_16` function. Since the first column has `l` and `o` we need to find a common shift that makes these two characters into `d` and `g`.  
By collecting the characters from each column we get the following result:

```text
col1: 'l','o'
col2: 'd','a'
col3: 'j','m'
col4: 'm','j'
col5: 'l','o'
col6: 'i'
col7: 'j'
col8: 'h','k'
col9: 'j','m'
```

Notice how some columns only have 1 character, that means it's either only digits(`d`) or characters(`g`) thus we need to try both. Looking at the shift algorithm implemented, we could easily reverse the operation knowing the output(`d` or `g`) and 1 input. We do this for each column and by finding the intersection of the two letters, we find a common shift that satisfies both letters thus giving us the key.

### Final Step

Now we have a list of potential keys, we just need to try each key on the ciphertext given then `b16_decode`, whichever decrypted output satisfies the flag format is the final flag.
