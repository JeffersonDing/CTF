import string

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
"""for i in range(len(enc)):
    if i%2:
        print(enc[i],"--> _")
    else:
        possible = [0,0]
        for key in ALPHABET:
            decrypt = shift(enc[i], key)
            if decrypt=='d':
                possible[0] = key
            elif decrypt=='g':
                possible[1] = key
        print(enc[i],"-->",possible[0],"/",possible[1])
#from the above code, manual analysis reveals key length of 9. 1st --> o, 2nd --> e, 3rd --> d/a, 4th --> f/c, 5th --> f/c, 6th --> m/j, 7th --> d/a, 8th --> e/b, 9th --> b/e"""
key_start = "inggi"
key_end = 'eg'
possible_keys = []
for k3 in ['f', 'c']:
    for k4 in ['g', 'd']:
        possible_keys.append(
            key_start+k3+k4+key_end)

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
        print(p[0], ":", p[1], "-->", answer)
