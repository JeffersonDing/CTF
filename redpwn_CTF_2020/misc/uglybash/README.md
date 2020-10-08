# uglybash
This challenge gives us a bash that is encoded in a wired way. No human readable stuff.
I couldn't run the script at first because I was using `zsh`. By asking the author, I was able to run the script using `bash` itself.
## Script
The script is simple, it echo's out a line that has the flag, but it is not displaying since it's in the comments. What we need to do here is try to show the verbose version of bash running, like running `gdb` but for bash.
## Solution
Im not to familiar with bash so I looked up `bash debug` and I found that we could use the flag `-x` to enter the mode.
The program spits out quite some junk but I found these lines pretty interesting
```bash
...
+++ printf %s h
+++ printf %s o
...
```
These are probably the flag contest as the `format string` function is taking in a `%s` string and the input should be the letter after it. 
I didn't want to write a script so I just coppied the input and did a `regex` replace and got the lines together to form the flag.
```
First REGEX Replace:

    ^((?!printf %s .).)*$
to  empty

Second REGEX Replace:

    \+\+\+ printf %s 
to  empty

Third REGEX Replace:
    \n
to  empty
```
# Flag
```
OUTPUT:
echo' 'dont' 'just' 'run' 'it,' 'dummy' ''#'' 'flag'{'us3_zsh,_dummy'}''
```


