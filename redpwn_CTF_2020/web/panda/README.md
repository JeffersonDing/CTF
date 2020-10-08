# panda facts
We were given a nodejs backend to work with and our goal is to make the token's `member` field to true so that we could access the flag.
## Source Code
We really just need to focus on the token generation function since that where we want to exploit.
```js
async function generateToken(username) {
    const algorithm = 'aes-192-cbc'; 
    const key = Buffer.from(process.env.KEY, 'hex'); 
    // Predictable IV doesn't matter here
    const iv = Buffer.alloc(16, 0);

    const cipher = crypto.createCipheriv(algorithm, key, iv);

    const token = `{"integrity":"${INTEGRITY}","member":0,"username":"${username}"}`

    let encrypted = '';
    encrypted += cipher.update(token, 'utf8', 'base64');
    encrypted += cipher.final('base64');
    return encrypted;
}
```
You can see the token is made by a `js` object and encoded. Without any sanitation on the input, we could easily run something on the `${username}` so that we alter the results.
## Alter `${username}`
What we could do here is escape the username key and creat a new key in the object. The decrypt function will render out a token that has 2 member keys and the latter one counts.
```js
const token = `{"integrity":"${INTEGRITY}","member":0,"username":"     random","member":"1         "}`
```
See what I did here? I escape the username filed with `"` and created a new `member` key.
So our input to the webpage should be 
```
random","member":"1
```
## The flag
Sure enough, if I enter the payload, the webpage says `hello random` instead of the full username since we escaped the username field.
When I click on the member only part, we get the flag
```
flag{1_c4nt_f1nd_4_g00d_p4nd4_pun}
```