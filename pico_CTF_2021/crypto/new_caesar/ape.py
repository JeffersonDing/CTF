import string

flag = ['']*39
ALPHABET = string.ascii_lowercase[:16]

for key in ALPHABET:
    for j in range(len(flag)):
        for k in ALPHABET:
            res = run(k, key)
