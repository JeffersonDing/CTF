from pwn import *


def integer_to_bytes(integer, _bytes):
    output = bytearray()
    for byte in range(_bytes):
        output.append((integer >> (8 * (_bytes - 1 - byte))) & 255)
    return output


conn = remote('mercury.picoctf.net', 60368)
conn.recvuntil("n: ")
n = int(conn.recvline().decode('utf-8'))
conn.recvuntil("e: ")
e = int(conn.recvline().decode('utf-8'))
conn.recvuntil("ciphertext: ")
c = int(conn.recvline().decode('utf-8'))
#plaintext = "helloworld"
#plaintext = "".join([str(ord(c)) for c in plaintext])
#encrypted = str(pow(int(plaintext), e, n)).encode('utf-8')
# print(plaintext)
evil = pow(2, e, n)
encrypted = str(evil * c)
conn.sendline(encrypted.encode('utf-8'))
conn.recvuntil("go: ")
p = int(conn.recvline().decode('utf-8')) // 2
print(bytes.fromhex(hex(p)[2:]).decode('utf-8'))
