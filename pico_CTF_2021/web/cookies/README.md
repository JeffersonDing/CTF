# Cookies
Looking at the website provided, if we try and enter an arbitrary input, it would prompt us that the input is invalid. However, if we use the placeholder text `snickerdoodle` we see that it gives us a page where the text is set to `I love snickerdoodle cookies!`.

## Method
Looking at the cookie set after entering `snickerdoodle` we see that it has a value of 0. By testing around and changing the cookie value to `1`, `2` etc. we see that it outputs a different name. My guess is that a certain cookie value will return us the flag.
### Script
This script uses python requests to loop through `1-20` and set that as our cookie. Then we send the post request and see what it returns. If something unusual(does not contain `I love`), we found our flag.