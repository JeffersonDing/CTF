import string

alphabet = "lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9"
message = "1x5hqlod8x7oa88h0de1b5r6xja5sd"
payload = string.printable


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


encrypted = splitStr(2, message)
