import string
import itertools

ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


def b16_decode(enc):
    first = ALPHABET.index(enc[0])
    second = ALPHABET.index(enc[1])
    first_binary = f"{first:04b}"
    second_binary = f"{second:04b}"
    return chr(int(first_binary+second_binary, 2))


enc = "lejjlnjmjndkmjinkilbmlljjkmnakmmighhocmllojhjmaijpiohnlojmokjkja"
possible = [['i'], ['n'], ['g'], ['g'], ['i'],
            ['f', 'c'], ['d', 'g'], ['e'], ['g']]

possible_keys = list(itertools.product(*possible))


for i in range(len(possible_keys)):
    possible_keys[i] = "".join(possible_keys[i])

potential = []
for key in possible_keys:
    decrypt = ""
    for i, c in enumerate(enc):
        decrypt += shift(c, key[i % len(key)])
    potential.append([key, decrypt])

for p in potential:
    answer = ""
    for i in range(0, len(p[1]), 2):
        answer += b16_decode(p[1][i:i+2])
    if all([c in "abcdef0123456789" for c in answer]):
        print("Key: {} | Potential: {} | Flag: {}".format(p[0], p[1], answer))
