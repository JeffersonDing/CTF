import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def run(flag, key):
    assert all([k in ALPHABET for k in key])
    assert len(key) == 1

    b16 = b16_encode(flag)
    enc = ""
    for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
    print(enc)


val = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
flag = "et_tu_07d5c0892c1438d2b32600e83dc2b0e5"
while True:
    print(flag)
    flag = flag[2:]
    test = input("test: ")
    print(val)
    val = val[4:]
    run(test, "n")
