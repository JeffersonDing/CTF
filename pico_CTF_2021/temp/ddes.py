from Crypto.Cipher import DES
from collections import defaultdict
import binascii
from pwn import *

encryption_results = defaultdict(lambda: False)


def intersection(list1, list2):
    list1_as_set = set(list1)
    intersection = list1_as_set.intersection(list2)
    intersection_as_list = list(intersection)
    return intersection_as_list


def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()


def find_key(ciphertext, plaintext):
    plaintext = pad(binascii.unhexlify(plaintext.rstrip()).decode())
    potential_keys = []
    log.info("********Starting Encryption*********")
    for i in range(999999):
        key = str(i).rjust(6, '0').ljust(8, ' ').encode()
        cipher1 = DES.new(key, DES.MODE_ECB)
        encrypted = binascii.hexlify(cipher1.encrypt(plaintext)).decode()
        encryption_results[encrypted] = key
    log.info("********Starting Decryption*********")
    for i in range(999999):
        key = str(i).rjust(6, '0').ljust(8, ' ').encode()
        cipher2 = DES.new(key, DES.MODE_ECB)
        decrypted = binascii.hexlify(cipher2.decrypt(
            binascii.unhexlify(ciphertext.rstrip()))).decode()
        if(encryption_results[decrypted] != False):
            potential_keys.append((encryption_results[decrypted], key))
    return(potential_keys)


def double_decrypt(cipher, key1, key2):
    cipher = binascii.unhexlify(cipher.encode())
    try:
        cipher2 = DES.new(key2, DES.MODE_ECB)
        decrypted_msg = cipher2.decrypt(cipher)
        cipher1 = DES.new(key1, DES.MODE_ECB)
        decrypted = cipher1.decrypt(decrypted_msg)
        return decrypted.decode()
    except:
        return("key error")


r = remote("mercury.picoctf.net", int(input("Enter port number:")))
r.recvline()
flag = r.recvline(keepends=False).decode()
r.sendafter('? ', b'41\n')
str_a = r.recvline(keepends=False).decode()
r.sendafter('? ', b'42\n')
str_b = r.recvline(keepends=False).decode()
r.sendafter('? ', b'43\n')
str_c = r.recvline(keepends=False).decode()
log.info("Encrypted Flag:{}".format(flag))
log.info("Plaintext Input: 41 | Ciphertext Output:{}".format(str_a))


res_a = find_key(str_a, '41')
#res_b = find_key(str_b, '42')
#res_c = find_key(str_c, '43')

#keys = intersection(res_a, intersection(res_b, res_c))

out = []
for pair in res_a:
    out.append(double_decrypt(flag, pair[0], pair[1]))

log.info("Flag:{}".format('\n'.join(list(set(out)))))
