# ropes
Running `file` on ropes we get
```
 Mach-O 64-bit x86_64 executable
 ```
 And currently, there is no `Mach-O` loader on linux and I don't want to pull out my Mac. So I just ran `strings` on the binary and I found the flag.
 # strings
 Strings in in the shell prints out all the readable bytes in a file. 
 ```bash
 strings ropes
__PAGEZERO
__TEXT
__text
__TEXT
__stubs
__TEXT
__stub_helper
__TEXT
__cstring
__TEXT
__unwind_info
__TEXT
__DATA
__nl_symbol_ptr
__DATA
__la_symbol_ptr
__DATA
__LINKEDIT
/usr/lib/dyld
/usr/lib/libSystem.B.dylib
Give me a magic number:
First part is: flag{r0pes_ar3_
Second part is: just_l0ng_str1ngs}
@dyld_stub_binder
@_printf
@_puts
@_scanf
_mh_execute_header
!main
__mh_execute_header
_main
_printf
_puts
_scanf
dyld_stub_binder
```
There you see it the parts of the flag.