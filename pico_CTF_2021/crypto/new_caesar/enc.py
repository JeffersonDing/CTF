import string
given = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")
payload = string.ascii_letters+string.digits+"_-\{\}?"


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
def exploit():
    target = splitStr(2, given)
    for key in ALPHABET:
        count = 0
        potential = []
        for goal in target:
            for test in payload:
                res = run(test, key)
                if(goal == res):
                    # print(key, "count ", count, " | ", end='')
                    count += 1
                    potential.append(test)
                    if(count == 38):
                        return "".join(potential)


print(exploit())
