def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


for x in range(1, 15):
    print("{} *********************".format(x))
    encrypted = "lejjlnjmjndkmjinkilbmlljjkmnakmmighhocmllojhjmaijpiohnlojmokjkja"
    encrypted = splitStr(x, encrypted)
    for i in encrypted:
        print(i)

# Key length is 9
