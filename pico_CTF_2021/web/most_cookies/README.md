# Most Cookies
This challenge uses `flask` as the backend framework to set user cookies which we know is prone to forgery attacks.
## Intuition
Looking at the source code, we see that the cookie generation secret key is just a random choice out of a small set of strings. This means that we could easily brute-force the cookie by trying every key on our desired payload.
## Method
[flask-session-cookie-manager](https://github.com/noraj/flask-session-cookie-manager) provides a complete set of scripts to encode and decode cookies. By grabbing those, we are able to create cookies programmatically with python. Using requests, we send those cookies off and monitor the returning webpage.
