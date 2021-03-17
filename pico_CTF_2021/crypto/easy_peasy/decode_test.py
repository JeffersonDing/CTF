string = "2366681f041d3979761d3927761d3923741d392571221d3979271d3922771d39"
flag_e = "5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c"


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


flag = splitStr(2, flag_e)
leaked = splitStr(2, string)
for i in range(len(leaked)):
    key = int(leaked[i], 16) ^ 65
    p = int(flag[i], 16)
    print(chr(p ^ key), end='')
