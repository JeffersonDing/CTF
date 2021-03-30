#-------------------------------------Original-------------------------------------------#

input = "input.txt"
# 101010 101010 101010 ...\r\n (264 6-bit binary numbers, 5 lines)
# 101010 101010 101010 ...\r\n
# 101010 101010 101010 ...\r\n
# 101010 101010 101010 ...\r\n
# 101010 101010 101010 ...\r\n


total = 264
t = (total + 1) * 5
numLength = (total * 30) + t


def Random_Gen():
    list1 = []
    for i in range(1, total+1):
        y = (((i * 327) % 681) + 344) % 313
        list1.append(y)
    return list1


def Scramble(block, seed):
    raw = "".join(block)
    print(raw)
    bm = ["10"]*len(raw)
    for i in range(len(raw)):
        y = (i * seed) % len(raw)
        n = bm[y]
        while (n != "10"):
            y = (y + 1) % len(raw)
            n = bm[y]
        if (raw[i] == "1"):
            n = "11"
        else:
            n = "00"
        bm[y] = n
    raw2 = "".join(bm)
    print(raw2)
    b = int(raw2, 2)
    return b


seeds = []
for i in range(1, total+1):
    seeds.append((i * 127) % 500)

randoms = Random_Gen()
output_file = ""
result = 0

# with open("output.txt", "w") as f:
#    f.write(output_file)

#----------------------------------------------------------------------------------------#

#--------------------------------------Solution------------------------------------------#

#result[i] = Scramble[blocks[i],seeds[i]] ^ result[i-1] ^ randoms[i]
#Scramble[blocks[i], seeds[i]] = result[i] ^ result[i-1] ^ randoms[i]
#blocks[i] = unscramble(result[i]^result[i-1]^randoms[i], seeds[i])


def findPos(seed, pos):
    raw = "000000000000000000000000000000"
    raw = raw[:pos] + "1" + raw[pos+1:]
    bm = ["10"]*len(raw)
    for i in range(len(raw)):
        y = (i * seed) % len(raw)
        n = bm[y]
        while (n != "10"):
            y = (y + 1) % len(raw)
            n = bm[y]
        if (raw[i] == "1"):
            n = "11"
        else:
            n = "00"
        bm[y] = n
    raw2 = "".join(bm)[::2]
    index = raw2.find("1")
    return index


def unscramble(b, seed):
    raw2 = "{0:b}".format(b).zfill(60)[::2]
    block = ""
    for i in range(30):
        block += raw2[findPos(seed, i)]
    return block


def getBlocks(results):
    blocks = []
    for i in range(len(results)):
        if i == 0:
            blocks.append(unscramble(
                results[i] ^ randoms[i], seeds[i % len(seeds)]))
        else:
            blocks.append(unscramble(
                results[i] ^ results[i-1] ^ randoms[i % len(randoms)], seeds[i % len(seeds)]))
    return blocks


def solve(blocks):
    rows = [""]*5
    for block in blocks:
        b = [block[i:i+6] for i in range(0, 30, 6)]
        for i in range(len(b)):
            if i == 263:
                rows[i] += b[i]
            else:
                rows[i] += b[i] + " "
    out = ""
    for row in rows:
        out += row + "\n"
    #chrs = [chr(int(out[i:i+8],2)) for i in range(0, len(out), 8)]
    return out

#----------------------------------------------------------------------------------------#


with open("output_orig.txt", "r") as f:
    results = f.read().splitlines()
    results = [int(integer) for integer in results]


with open("flag.txt", "w") as f:
    f.write(solve(getBlocks(results)))
