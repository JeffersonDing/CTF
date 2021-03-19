#!/usr/bin/python3 -u
import signal
import string

SQUARE_SIZE = 6


def generate_square(alphabet):
    assert len(alphabet) == pow(SQUARE_SIZE, 2)
    matrix = []
    for i, letter in enumerate(alphabet):
        if i % SQUARE_SIZE == 0:
            row = []
        row.append(letter)
        if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
            matrix.append(row)
    return matrix


def get_index(letter, matrix):
    for row in range(SQUARE_SIZE):
        for col in range(SQUARE_SIZE):
            if matrix[row][col] == letter:
                return (row, col)
    print("letter not found in matrix.")
    exit()


def encrypt_pair(pair, matrix):
    p1 = get_index(pair[0], matrix)
    p2 = get_index(pair[1], matrix)

    if p1[0] == p2[0]:
        return matrix[p1[0]][(p1[1] + 1) % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1) % SQUARE_SIZE]
    elif p1[1] == p2[1]:
        return matrix[(p1[0] + 1) % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1) % SQUARE_SIZE][p2[1]]
    else:
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]


def encrypt_string(s, matrix):
    result = ""
    if len(s) % 2 == 0:
        plain = s
    else:
        plain = s + "lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9"[0]
    for i in range(0, len(plain), 2):
        result += encrypt_pair(plain[i:i + 2], matrix)
    return result


# https://en.wikipedia.org/wiki/Playfair_cipher

def run(alphabet, msg):
    m = generate_square(alphabet)
    enc_msg = encrypt_string(msg, m)
    return(enc_msg)


def test(alphabet, msg):
    m = generate_square(alphabet)
    enc_msg = encrypt_string(msg, m)
    print(enc_msg)
    return enc_msg


alphabet = "lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9"
payload = alphabet


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


message = "1x5hqlod8x7oa88h0de1b5r6xja5sd"


def exploit():
    encrypted = splitStr(2, message)
    for goal in encrypted:
        for i in payload:
            for j in payload:
                m = run(alphabet, i+j)
                if(m == goal):
                    print(i+j, end='')


exploit()
