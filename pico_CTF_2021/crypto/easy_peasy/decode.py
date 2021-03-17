leaked = "70761d3979787705361d3923221d392523631d39797974016816201d3978761d"
flag_e = "5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c"


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


leaked = splitStr(2, leaked)
flag_e = splitStr(2, flag_e)


for i in range(len(leaked)):
    print(chr((int(leaked[i], 16) ^ 65) ^ (int(flag_e[i], 16))), end='')
