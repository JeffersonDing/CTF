import string
import itertools

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
    # (t1+t2)%16 = 11
    # d --> l is shift 8 and g --> l is shift 5


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


def run(flag, key):
    assert all([c in "abcdef0123456789" for c in flag])
    assert all([k in ALPHABET for k in key]) and len(key) < 15
    b16 = b16_encode(flag)
    enc = ""
    for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
    return(enc)


encrypted = "lejjlnjmjndkmjinkilbmlljjkmnakmmighhocmllojhjmaijpiohnlojmokjkja"

target = splitStr(4, encrypted)

payload = "abcdef0123456789"

possible = [['i'], ['a'], ['g'], ['g'], ['i'],
            ['f', 'c'], ['d', 'g'], ['e'], ['g']]

possible_keys = list(itertools.product(*possible))

for i in range(len(possible_keys)):
    possible_keys[i] = "".join(possible_keys[i])


output = []
for key in possible_keys:
    for goal in target:
        for test in payload:
            for test2 in payload:
                for test3 in payload:
                    res = run(test+test2+test3, key)
                    if(goal == res):
                        print(key)
print("\n")
print("".join(output))
