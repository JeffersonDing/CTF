# base646464
As the name suggest, you could already tell that this challenge is about decoding base 64 encoded strings.  
We were given a txt file that contains a encoded string, and a generate.js file that shows how the encoding works.
## Experienced CTF Player
If you have participated in CTF games, you might be able to pull off this challenge without even looking at the source code. What I did was run `base64 --decode` a lot of times in `bash` and I was able to get the answer. This might seem abundant, but it's a good way to get a quick flag without writing a script.
```bash
cat cipher.txt | base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode

```
## Examine the Source Code
Here's the source code of the `generate.js`file:
```javascript
const btoa = str => Buffer.from(str).toString('base64');
const fs = require("fs");
const flag = fs.readFileSync("flag.txt", "utf8").trim();
let ret = flag;
for(let i = 0; i < 25; i++) ret = btoa(ret);
fs.writeFileSync("cipher.txt", ret);
```
From the first like, we know that the functino `btoa` uses `base64` encoding to encode the passed in `str` string. Then this functino is calleng `25` times in the for loop. So what we have to do decode the input cipher `25` times in base 64.

## Python Script
We can use the python `base64` module to handle the diciphering. All we need to do is run base64 decode 25 times and we sholud get the flag.
```python
import base64
f = open('cipher.txt', 'r') 
cipher = f.read()
ptxt=cipher
for i in range(25):
    ptxt = base64.b64decode(ptxt)
print(ptxt)
```
Output :
```bash
python3 ape.py
b'flag{l00ks_l1ke_a_l0t_of_64s}'
```
