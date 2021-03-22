import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


encrypted = "lejjlnjmjndkmjinkilbmlljjkmnakmmighhocmllojhjmaijpiohnlojmokjkja"


def find_char(character):
    output = []
    # look for d
    output.append(chr(ALPHABET.index(character) - 3 + 97))
    # look for g
    output.append(chr(ALPHABET.index(character) - 6 + 97))
    return output


possible = [[], [], [], [], [], [], [], [], []]
for i in range(0, 9):
    if(i % 2 == 0):
        d = find_char(encrypted[i])
        g = find_char(encrypted[i+18])
        list1_as_set = set(d)
        intersection = list1_as_set.intersection(g)
        intersection_as_list = list(intersection)
        possible[i].extend(intersection_as_list)
    else:
        d = find_char(encrypted[i+9])
        g = find_char(encrypted[i+27])
        list1_as_set = set(d)
        intersection = list1_as_set.intersection(g)
        intersection_as_list = list(intersection)
        possible[i].extend(intersection_as_list)

for x in range(len(possible)):
    possible[x] = list(set(possible[x]))

print(find_char('a', 'c'))
