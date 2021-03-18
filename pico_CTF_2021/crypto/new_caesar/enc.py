import string
given = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")
payload = string.printable


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


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
    return(enc)


#flag = "xovSU7UjYSH_cOnE9Q_JsgX5wAqE59eJ7HBJaWK"
#key = "b"
#given = run(flag, key)
# print(flag)
print(given)
target = splitStr(2, given)
output = []
for key in ['n']:
    for goal in target:
        for test in payload:
            res = run(test, key)
            if(goal == res):
                print(key, end='')
                output.append(test)
print("\n")
print("".join(output))
