from pwn import *
a = [
    0x38313638,
    0x31663633,
    0x64336533,
    0x64373236,
    0x37336166,
    0x62646235,
    0x39383338,
    0x65343132,
]
s1 = ''
for i in a:
    s1 += p32(i).decode()
s2 = "\x4a\x53\x47\x5d\x41\x45\x03\x54\x5d\x02\x5a\x0a\x53\x57\x45\x0d\x05\x00\x5d\x55\x54\x10\x01\x0e\x41\x55\x57\x4b\x45\x50\x46\x01"


passwd1 = [chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)]

print("Hashed Key in MD5: {}".format(s1))
print("Recovered Password: {}".format("".join(passwd1)))
