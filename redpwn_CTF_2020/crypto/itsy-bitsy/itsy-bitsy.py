#!/usr/bin/env python3

from Crypto.Random.random import randint

def str_to_bits(s): #convert str to 7 bits
    bit_str = ''
    for c in s:
        i = ord(c)
        bit_str += bin(i)[2:]
    return bit_str
print("str_to_bits of 'a': "+str_to_bits('a'))


def recv_input():
    i = input('Enter an integer i such that i > 0: ')
    j = input('Enter an integer j such that j > i > 0: ')
    try:
        i = int(i)
        j = int(j)
        if i <= 0 or j <= i:
            raise Exception
    except:
        print('Error! You must adhere to the restrictions!')
        exit()
    return i,j


def generate_random_bits(lower_bound, upper_bound, number_of_bits):
    bit_str = ''
    while len(bit_str) < number_of_bits:
        r = randint(lower_bound, upper_bound)
        bit_str += bin(r)[2:]
    print("gen_rand_bits of (0,2,2) before cut: "+bit_str)    
    return bit_str[:number_of_bits]
print("gen_rand_bits of (0,2,2) after cut: "+generate_random_bits(0,2,2))


def bit_str_xor(bit_str_1, bit_str_2):
    xor_res = ''
    for i in range(len(bit_str_1)):
        bit_1 = bit_str_1[i]
        bit_2 = bit_str_2[i]
        xor_res += str(int(bit_1) ^ int(bit_2))
    return xor_res
print("bit_str_xor of (110,101): "+bit_str_xor('110','101'))

def main():
    with open('flag.txt','r') as f:
        flag = f.read()
    for c in flag:
        i = ord(c)
        assert i in range(2**6,2**7)
    flag_bits = str_to_bits(flag)
    i,j = recv_input()
    
    lb = 2**i

    ub = 2**j - 1
    n = len(flag_bits)
    random_bits = generate_random_bits(lb,ub,n)
    encrypted_bits = bit_str_xor(flag_bits,random_bits)
    print(f'Ciphertext: {encrypted_bits}')


#if __name__ == '__main__':
    #main()