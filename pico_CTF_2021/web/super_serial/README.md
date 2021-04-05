# Super Serial
Theres actually 2 ways of solving this challenge in which the second one is probably the intended way but the first one is extremely easy to execute. 
## Method 1
> Credits to @ZeroDayTea

Looking at the hint we see that the flag is located at `../flag` all we need to do is url encode `../flag` and append that to the URL, basically performing a path traversal attack.

## Object Serialization
This is probably the intended way since the name of the challenge hints so.  
By looking at the `robots.txt` file we get a hint that `.phps` files exist, and true enough, appending `s` so all pages we see the source php code.  
Looking at the code we can see something interesting in this block:
```php
if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}
```
We see that we are trying to deserialize user provided data which could lead to some sort of exploit, more, we see that if it errors, we print the object on the screen.  
Taking a deeper look we see that the `access_log` class has a magic function `_toString` which reads any file that you input. This means that if we get the try block to error, the `die` statement will try and call the `_toString` method of a `access_log` object will give us access to `../flag`
### Payload
Set the cookie to `TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9`.
This is a access log object pointing to `../flag` after serialization, base64 encoding and url encoding.