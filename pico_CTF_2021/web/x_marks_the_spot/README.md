# X Marks the Spot
Looking at the hint we see that it's a `XPATH` injection challenge. 
Starting from [PATT](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XPATH%20Injection) we see that we can actually leak the flag character by character by using the `contains()` function in the injection.
## Method
The script uses the python requests module and loops through the characters to build out the flag. 