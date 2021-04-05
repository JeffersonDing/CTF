# Ancient History
The js variable `_0x24f7` outputs the following JS array
```
526768ZtfrvX
Hello World!
78163aRzYSF
457jWohGf
3gwbXxs
240229GBlwom
164587EeZQxF
157219qCggfo
5sPeoBz
223cFkxrK
2333MZMsti
log
1pWuugQ
564uktHRc
```

I suspect that this is URL path names but I cant seem to access any.

## Prettfied JS

```html
window.history.pushState()
```
# Method
Turns out after discovering the `pushState()` function, I realized that the JS pushes a lot of states to the user DOM. We can use `window.history.back()` to go back in the history tree and recover the flag.
# Flag
```
picoCTF{th4ts_k1nd4_n34t_3bed1170}
```
