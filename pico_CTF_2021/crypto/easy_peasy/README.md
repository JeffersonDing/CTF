# Easy Peasy

This challenge is vulnerable due to it's OTP generation algorithm. Taking a closer look at the source we see that after a certain amount of characters inputted, we are able to cycle back to the beginning of the start of the key thus leaking it.

## Method

The important observation is here

```python
 if stop >= KEY_LEN:
        stop = stop % KEY_LEN
```

we see that if our user input is greater than the `KEY_LEN` variable, we will be able to redefine the starting point of the next encryption. If we make sure that we input the same amount of characters up till the `KEY_LEN` we can cycle back to 0.  
I tried to send the buffer all at once to overflow it back to 0, but the terminal couldn't handle it thus I split it up into chunks of `4000` or `2000` characters and encrypted it using `65` which is `A`. This means that after I overflow back to 0, I just need to leak the first 32 characters of the flag with our known key `A` and XOR decrypt it programmatically.

## Notes

Encrypted

```
5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c
```

Flag_length = 32

leaked bytes

```
2366681f041d3979761d3927761d3923741d392571221d3979271d3922771d39
```

2020202023202020222020202520202024202020272020202620202029202020
