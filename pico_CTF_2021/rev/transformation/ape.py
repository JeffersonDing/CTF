import string
def encode(flag):
    return ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
goal = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
flag_length = 38

payload = string.ascii_uppercase + string.ascii_lowercase + string.digits + "\{\}_"



for x in goal:
    for i in payload:
        for j in payload:
            if(encode(i+j) == x):
                print(i,end='')
                print(j, end='')
