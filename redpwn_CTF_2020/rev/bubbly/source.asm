0x00000000000011d9 <+0>:     push   rbp
0x00000000000011da <+1>:     mov    rbp,rsp
0x00000000000011dd <+4>:     sub    rsp,0x10
0x00000000000011e1 <+8>:     mov    rax,QWORD PTR [rip+0x2eb8]        # 0x40a0 <stdout@@GLIBC_2.2.5>
0x00000000000011e8 <+15>:    mov    esi,0x0
0x00000000000011ed <+20>:    mov    rdi,rax
0x00000000000011f0 <+23>:    call   0x1040 <setbuf@plt>
0x00000000000011f5 <+28>:    mov    rax,QWORD PTR [rip+0x2eb4]        # 0x40b0 <stdin@@GLIBC_2.2.5>
0x00000000000011fc <+35>:    mov    esi,0x0
0x0000000000001201 <+40>:    mov    rdi,rax
0x0000000000001204 <+43>:    call   0x1040 <setbuf@plt>
0x0000000000001209 <+48>:    mov    rax,QWORD PTR [rip+0x2eb0]        # 0x40c0 <stderr@@GLIBC_2.2.5>
0x0000000000001210 <+55>:    mov    esi,0x0
0x0000000000001215 <+60>:    mov    rdi,rax
0x0000000000001218 <+63>:    call   0x1040 <setbuf@plt>
0x000000000000121d <+68>:    lea    rdi,[rip+0xdf4]        # 0x2018
0x0000000000001224 <+75>:    call   0x1030 <puts@plt>
0x0000000000001229 <+80>:    mov    BYTE PTR [rbp-0x1],0x0
0x000000000000122d <+84>:    lea    rax,[rbp-0xc]
0x0000000000001231 <+88>:    mov    rsi,rax
0x0000000000001234 <+91>:    lea    rdi,[rip+0xe1d]        # 0x2058
0x000000000000123b <+98>:    mov    eax,0x0
0x0000000000001240 <+103>:   call   0x1060 <__isoc99_scanf@plt>
0x0000000000001245 <+108>:   mov    DWORD PTR [rbp-0x8],eax
0x0000000000001248 <+111>:   mov    eax,DWORD PTR [rbp-0xc]
0x000000000000124b <+114>:   cmp    eax,0x8
0x000000000000124e <+117>:   ja     0x134d <main+372>
0x0000000000001254 <+123>:   mov    eax,DWORD PTR [rbp-0xc]
0x0000000000001257 <+126>:   mov    eax,eax
0x0000000000001259 <+128>:   lea    rdx,[rax*4+0x0]
0x0000000000001261 <+136>:   lea    rax,[rip+0x2df8]        # 0x4060 <nums>
0x0000000000001268 <+143>:   mov    edx,DWORD PTR [rdx+rax*1]
0x000000000000126b <+146>:   mov    eax,DWORD PTR [rbp-0xc]
0x000000000000126e <+149>:   add    eax,0x1
0x0000000000001271 <+152>:   mov    eax,eax
0x0000000000001273 <+154>:   lea    rcx,[rax*4+0x0]
0x000000000000127b <+162>:   lea    rax,[rip+0x2dde]        # 0x4060 <nums>
0x0000000000001282 <+169>:   mov    eax,DWORD PTR [rcx+rax*1]
0x0000000000001285 <+172>:   mov    esi,DWORD PTR [rbp-0xc]
0x0000000000001288 <+175>:   mov    ecx,edx
0x000000000000128a <+177>:   xor    ecx,eax
0x000000000000128c <+179>:   mov    eax,esi
0x000000000000128e <+181>:   lea    rdx,[rax*4+0x0]
0x0000000000001296 <+189>:   lea    rax,[rip+0x2dc3]        # 0x4060 <nums>
0x000000000000129d <+196>:   mov    DWORD PTR [rdx+rax*1],ecx
0x00000000000012a0 <+199>:   mov    eax,DWORD PTR [rbp-0xc]
0x00000000000012a3 <+202>:   add    eax,0x1
0x00000000000012a6 <+205>:   mov    eax,eax
0x00000000000012a8 <+207>:   lea    rdx,[rax*4+0x0]
0x00000000000012b0 <+215>:   lea    rax,[rip+0x2da9]        # 0x4060 <nums>
0x00000000000012b7 <+222>:   mov    edx,DWORD PTR [rdx+rax*1]
0x00000000000012ba <+225>:   mov    eax,DWORD PTR [rbp-0xc]
0x00000000000012bd <+228>:   mov    eax,eax
0x00000000000012bf <+230>:   lea    rcx,[rax*4+0x0]
0x00000000000012c7 <+238>:   lea    rax,[rip+0x2d92]        # 0x4060 <nums>
0x00000000000012ce <+245>:   mov    eax,DWORD PTR [rcx+rax*1]
0x00000000000012d1 <+248>:   mov    ecx,DWORD PTR [rbp-0xc]
0x00000000000012d4 <+251>:   lea    esi,[rcx+0x1]
0x00000000000012d7 <+254>:   mov    ecx,edx
0x00000000000012d9 <+256>:   xor    ecx,eax
0x00000000000012db <+258>:   mov    eax,esi
0x00000000000012dd <+260>:   lea    rdx,[rax*4+0x0]
0x00000000000012e5 <+268>:   lea    rax,[rip+0x2d74]        # 0x4060 <nums>
0x00000000000012ec <+275>:   mov    DWORD PTR [rdx+rax*1],ecx
0x00000000000012ef <+278>:   mov    eax,DWORD PTR [rbp-0xc]
0x00000000000012f2 <+281>:   mov    eax,eax
0x00000000000012f4 <+283>:   lea    rdx,[rax*4+0x0]
0x00000000000012fc <+291>:   lea    rax,[rip+0x2d5d]        # 0x4060 <nums>
0x0000000000001303 <+298>:   mov    edx,DWORD PTR [rdx+rax*1]
0x0000000000001306 <+301>:   mov    eax,DWORD PTR [rbp-0xc]
0x0000000000001309 <+304>:   add    eax,0x1
0x000000000000130c <+307>:   mov    eax,eax
0x000000000000130e <+309>:   lea    rcx,[rax*4+0x0]
0x0000000000001316 <+317>:   lea    rax,[rip+0x2d43]        # 0x4060 <nums>
0x000000000000131d <+324>:   mov    eax,DWORD PTR [rcx+rax*1]
0x0000000000001320 <+327>:   mov    esi,DWORD PTR [rbp-0xc]
0x0000000000001323 <+330>:   xor    edx,eax
0x0000000000001325 <+332>:   mov    ecx,edx
0x0000000000001327 <+334>:   mov    eax,esi
0x0000000000001329 <+336>:   lea    rdx,[rax*4+0x0]
0x0000000000001331 <+344>:   lea    rax,[rip+0x2d28]        # 0x4060 <nums>
0x0000000000001338 <+351>:   mov    DWORD PTR [rdx+rax*1],ecx
0x000000000000133b <+354>:   mov    eax,0x0
0x0000000000001340 <+359>:   call   0x1165 <check>
0x0000000000001345 <+364>:   mov    BYTE PTR [rbp-0x1],al
0x0000000000001348 <+367>:   jmp    0x122d <main+84>
0x000000000000134d <+372>:   nop
0x000000000000134e <+373>:   cmp    BYTE PTR [rbp-0x1],0x0
0x0000000000001352 <+377>:   je     0x136c <main+403>
0x0000000000001354 <+379>:   lea    rdi,[rip+0xd00]        # 0x205b
0x000000000000135b <+386>:   call   0x1030 <puts@plt>
0x0000000000001360 <+391>:   mov    eax,0x0
0x0000000000001365 <+396>:   call   0x11bf <print_flag>
0x000000000000136a <+401>:   jmp    0x1378 <main+415>
0x000000000000136c <+403>:   lea    rdi,[rip+0xcf3]        # 0x2066
0x0000000000001373 <+410>:   call   0x1030 <puts@plt>
0x0000000000001378 <+415>:   mov    eax,0x0
0x000000000000137d <+420>:   leave
0x000000000000137e <+421>:   ret