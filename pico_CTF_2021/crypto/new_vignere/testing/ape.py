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

# tools


def intersection(list1, list2):
    list1_as_set = set(list1)
    intersection = list1_as_set.intersection(list2)
    intersection_as_list = list(intersection)
    return intersection_as_list


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


def b16_decode(enc):
    first = ALPHABET.index(enc[0])
    second = ALPHABET.index(enc[1])
    first_binary = f"{first:04b}"
    second_binary = f"{second:04b}"
    return chr(int(first_binary+second_binary, 2))


def run(flag, key):
    assert all([k in ALPHABET for k in key]) and len(key) < 15
    assert all([c in "abcdef0123456789" for c in flag])
    b16 = b16_encode(flag)
    enc = ""
    for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
    return(enc)


flag = "abc0123456def789"
key = "a"
possible_key = ALPHABET
possible_flag = "abcdef0123456789"
given = "lejjlnjmjndkmjinkilbmlljjkmnakmmighhocmllojhjmaijpiohnlojmokjkja"


def find_key(char1, char2):
    out_chr1 = []
    out_chr2 = []
    for i in possible_key:
        res = shift('d', i)
        if(res == char1 or res == char2):
            out_chr1.append(i)
        res = shift('g', i)
        if(res == char1 or res == char2):
            out_chr2.append(i)
    if(len(out_chr1) == 1 or len(out_chr2) == 1):
        out_chr1.extend(out_chr2)
        return out_chr1
    else:
        return intersection(out_chr1, out_chr2)


def get_possible_keys(column_data):
    possible = [[], [], [], [], [], [], [], [], []]
    for i, c in enumerate(column_data):
        if(i % 2 == 0):
            possible[i].extend(find_key(c[0], c[1]))
        else:
            possible[i].extend(find_key(c[0], c[1]))
    possible_keys = list(itertools.product(*possible))
    for i in range(len(possible_keys)):
        possible_keys[i] = "".join(possible_keys[i])
    return(possible_keys)


column_data = [
    ['l', 'o'],
    ['d', 'a'],
    ['j', 'm'],
    ['m', 'j'],
    ['l', 'o'],
    ['i', 'i'],
    ['j', 'j'],
    ['h', 'k'],
    ['j', 'm'],
]


def exploit(given, possible_keys):
    given = splitStr(2, given)
    output = []
    for i in given:
        output.append([])
    for key in possible_keys:
        for i, goal in enumerate(given):
            for payload in possible_flag:
                res = run(payload, key)
                if(res == goal):
                    output[i].append(key)
    print(output)


possible_keys = get_possible_keys(column_data)
print(len(possible_keys))
print(run('abced', "inggifgeg"))
