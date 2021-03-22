from z3 import *

encrypted_flag = []
enc = "\x18j|a\x118i7[H~Jh^Ko\x1f]\x5cw4kP\x15pO?\x5cEo\x14\x06\x05}>=\x04\x16.\x12L"

# determine flag length
# print(len(enc))
for i in enc:
    encrypted_flag.append(ord(i))


'''
pseudocode

input -> user input
flag -> [0]*len(flag) -> [0]*41
    flag[i] = input[i] XOR 20
    IF i > 0
    ...flag[i] XOR flag[i-1]
    IF i>2
    ...flag[i] XOR flag[i-3]
    flag[i] XOR i % 10

    IF i IS EVEN
    ...flag[i] XOR 8
    ELSE
    ...flag[i] XOR 9

    IF i IS DEVISIBLE BY 3:
    ...IF REMAINDER = 1
    ......flag[i] XOR 6
    ...ELSE
    ......flag[i] XOR 5
    ELSE
    ...flag[i] XOR 7

'''


def check_flag(flag):
    flag_buffer = [0]*41

    input_index = 0
    while True:
        if input_index >= 41:
            # move on to next char
            break
        flag_buffer[input_index] = flag[input_index] ^ 20
        # bit wise XOR with 20
        if input_index > 0:
            flag_buffer[input_index] ^= flag_buffer[input_index - 1]
            # the current char bitwise XOR with prev
        if input_index > 2:
            flag_buffer[input_index] ^= flag_buffer[input_index - 3]
            # current char bitwise XOR with curr-3
        flag_buffer[input_index] ^= input_index % 10
        # current char bitwise XOR with index % 10
        if input_index % 2 != 0:
            flag_buffer[input_index] ^= 8
            # current char bitwise XOR with 8
        else:
            flag_buffer[input_index] ^= 9
            # current char bitwise XOR with 9
        if input_index % 3 != 0:
            if input_index % 3 == 1:
                # current char bitwise XOR with index 6
                flag_buffer[input_index] ^= 6
            else:
                # current char bitwise XOR with index 5
                flag_buffer[input_index] ^= 5
        else:
            # current char bitwise XOR with index 7
            flag_buffer[input_index] ^= 7
        input_index += 1
        # next character

    # check flag validity
    flag_indx = 0
    while True:
        if flag_indx >= input_index:
            break
        if flag_indx % 2 == 0:
            if flag_indx + 1 < input_index:
                # swap flag index and flag index+1
                flag_buffer[flag_indx], flag_buffer[flag_indx +
                                                    1] = flag_buffer[flag_indx + 1], flag_buffer[flag_indx]
        flag_indx += 1

    return flag_buffer


# initialize output flag
flag = [ord('a')]*41
for i in range(len(flag)):
    flag[i] = BitVec(f'flag{i}', 8)
    # prepare flag for z3, Bv(flag{i},8) --> flag[i]
s = Solver()

for i in range(41):
    s.add(check_flag(flag)[i] == encrypted_flag[i])

try:
    if s.check() == sat:
        model = s.model()
        for i in flag:
            c = model[i].as_long()
            print(chr(c), end='')
except:
    pass
print()
