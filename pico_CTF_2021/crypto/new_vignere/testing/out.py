import itertools
import string

ALPHABET = string.ascii_lowercase[:16]

possible = [['f', 'i'], ['a'], ['j', 'g', 'd'], ['j', 'g'], [
    'f', 'i'], ['c', 'f'], ['g', 'd'], ['h', 'b', 'e'], ['j', 'g', 'd']]

possible_keys = list(itertools.product(*possible))

for i in range(len(possible_keys)):
    possible_keys[i] = "".join(possible_keys[i])
    assert all([k in ALPHABET for k in possible_keys[i]])

possible_keys = list(set(possible_keys))
print(possible_keys)
