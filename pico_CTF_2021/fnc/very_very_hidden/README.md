# Very Very Hidden
> Credit goes to @ZeroDayTea

Given a `.pcapng` we were able to recover a several `http` files. We find two `duck` images.  
## Intuition
Looking at the traffic, we see a lot of references to `powershell` so after extensive research, a tool called `Extract-PSImage` was found and it could extract powershell scripts from images.
## Method
By running the tool on the `evil_duck` image we were able to recover a script that will output the flag.
