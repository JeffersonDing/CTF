from struct import unpack


def splitStr(n, string):  # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return split_string


def getTable():
    found_table = "a5e08208683816fdbdad147eab1eeba6"\
        "cf3637cce9884f3ac3065daf950fb358"\
        "92fc8ce5602bc2696622b80def845fa0"\
        "d76e2acb462cf1b1a9ded5b7ce3962e8"\
        "700c21c6647dbbc1982002ff7f556b6c"\
        "f454f056c9579dd0c5814367dff847b5"\
        "799f3c1f9c18809a8d30d9942f425035"\
        "74118e4ec404b0e15c3d72c7196a4d49"\
        "031591991a05c0e7528b6f59f985d3bc"\
        "25cdb6dbec5b7bf6aa731dfe26413ea3"\
        "53ed5a34eaac1790103363a7d276f7be"\
        "834a7a0adc45d648ee24f24412311c32"\
        "da5e232da8a4001b4078657c71d887dd"\
        "013b4bbf27616d0ba1e3d1519ed4fbae"\
        "faf3b40eca9309c8b997754ce4963f9b"\
        "77e6291307b22e8928e2a28f8a86f5ba"\
        "690264134bd2e4f584ecc0e148125b94"\
        "b58bed6557d00f3e3788d3e034e82d9b"\
        "ad462a1f592e6cc80ede6ab679872297"\
        "c51419ddc1b79042b3ebe7174d55fe0d"\
        "f633c6e66de2b10347f326fc161bc228"\
        "0760ac768d6f61cb6b809d15af38b0d1"\
        "d4583d83fba61aa3737824e541eacc3f"\
        "f98fbe9f6e4449bba74c40b2f231cad7"\
        "e9b872b954325cd5c74a1108ba75dcbd"\
        "7d186227918a74cd35987b05c343a5f1"\
        "29ff71e34e522551c42f1e95ab665692"\
        "7f0a20da93d6b439109ed8bc04ce5d8e"\
        "8c3aa900dffa3b6768537aa2454f7c06"\
        "a4811c89d9a02c2196a15f77ae86829c"\
        "aaf4dbcfbfa863f80b093cc9eff02b5a"\
        "ee990130855e7e361dfd50700c9a23f7"\
        "ce6aebc54716e8dc8c39afb31fc3687e"\
        "fd10da3c1e1557a3e3a84e050a7674e0"\
        "9777939f7b7131f53bacb49bc65e9a37"\
        "2201d49987e4ada76b24146462ea527c"\
        "385cccfc2354482509952eb134e1ff17"\
        "3aefc9503efb72d04d2a4ba6f485ca00"\
        "30c16c4635dd84942f56e96d55068b36"\
        "9e5dd53f906067f688b079d8a1fa028d"\
        "49f18182b94369ee5b04e2610eb7c0f0"\
        "28a973831cbe4c1375911bcdbd7f0c86"\
        "1aa4d28af74445ab3242cfde198e4f6f"\
        "6ec7b8eda541c8290d965963d6baf83d"\
        "db9d789826a2fe2cbc27890351d311d9"\
        "65e7e6330f92b59cbfcb1870c407ae7d"\
        "b22d8fc220f2aa40d7121db6585aa02b"\
        "4af30bf95f08df7aec66bbe553d12180"\
        "11834d6f1a0a91355f3e8014a9daf655"\
        "d4e001ae770921659baa56a27010be86"\
        "f11375191e6707f295257c69effe440f"\
        "71c3edee6aa7d0b24c592ce32f967fe2"\
        "a5e9cc2b0c76c89449bb1702ec8c640b"\
        "04cbbaa61b4f1579978241bd744bb962"\
        "e6c7c0545093f7a000e7ac03dc5ae5c1"\
        "1d7e3c2a4ad66cd9dbb3a3475120065b"\
        "ff9929fdc4a1fb85b1de28dd66345824"\
        "c58deac660f3e19fcf23af2e405c7d18"\
        "c273cdad438190225e2db5f5f09826d3"\
        "f96bb4d51c1f399eb69c8845d23da852"\
        "d14616caf46e7868083889c9920dabb0"\
        "36df3a63fa27bca4b8324e0e7b726d53"\
        "5dd78e37573087eb42129abf3be8e4b7"\
        "3f61ce05d8fcf831849d338b7a8f488a"\
        "7372632f6d61696e2e72730000000000"
    table = []
    found_table = bytearray.fromhex(found_table)
    for i in found_table:
        tmp = i.to_bytes(1, byteorder='little')
        # unpack to unsigned char, its only one chr so endian doesn't matter
        table.append(unpack('B', tmp)[0])
    return(table)


def getArr2():
    found_arr2 = "0b000000000000000400000000000000"\
        "13000000000000000d00000000000000"\
        "09000000000000001d00000000000000"\
        "18000000000000001c00000000000000"\
        "0c000000000000001400000000000000"\
        "10000000000000001900000000000000"\
        "0f000000000000000000000000000000"\
        "0a000000000000000500000000000000"\
        "1a000000000000000100000000000000"\
        "0e000000000000000600000000000000"\
        "1e000000000000000300000000000000"\
        "08000000000000001b00000000000000"\
        "02000000000000001f00000000000000"\
        "15000000000000001100000000000000"\
        "16000000000000001200000000000000"\
        "17000000000000000700000000000000"\
        "1c000000000000001000000000000000"\
        "1f000000000000000800000000000000"\
        "1b000000000000001a00000000000000"\
        "00000000000000001100000000000000"\
        "19000000000000001500000000000000"\
        "09000000000000000200000000000000"\
        "12000000000000001800000000000000"\
        "07000000000000001600000000000000"\
        "1e000000000000000b00000000000000"\
        "0a000000000000001700000000000000"\
        "14000000000000001300000000000000"\
        "05000000000000000400000000000000"\
        "0d000000000000000c00000000000000"\
        "01000000000000000300000000000000"\
        "0e000000000000000f00000000000000"\
        "1d000000000000000600000000000000"\
        "07000000000000000200000000000000"\
        "12000000000000000b00000000000000"\
        "11000000000000000500000000000000"\
        "18000000000000000000000000000000"\
        "1f000000000000001300000000000000"\
        "01000000000000000300000000000000"\
        "1d000000000000000e00000000000000"\
        "1e000000000000001600000000000000"\
        "1b000000000000001500000000000000"\
        "04000000000000001000000000000000"\
        "1c000000000000000a00000000000000"\
        "0c000000000000001900000000000000"\
        "0d000000000000000800000000000000"\
        "14000000000000000600000000000000"\
        "09000000000000001700000000000000"\
        "0f000000000000001a00000000000000"\
        "12000000000000000d00000000000000"\
        "14000000000000000500000000000000"\
        "0c000000000000001d00000000000000"\
        "17000000000000000000000000000000"\
        "0f000000000000000900000000000000"\
        "02000000000000000100000000000000"\
        "04000000000000000600000000000000"\
        "08000000000000001800000000000000"\
        "0b000000000000001600000000000000"\
        "10000000000000000a00000000000000"\
        "1c000000000000000e00000000000000"\
        "11000000000000001500000000000000"\
        "1e000000000000001b00000000000000"\
        "1a000000000000001900000000000000"\
        "13000000000000000700000000000000"\
        "03000000000000001f00000000000000"
    arr2 = []
    found_arr2 = splitStr(16, found_arr2)
    for i in found_arr2:
        temp = bytes.fromhex(i)
        # unpack into unsigned long long in little endian
        arr2.append(unpack('<Q', temp)[0])
    return(arr2)


def recoverGeneratedArr_x(dstArr, x):
    x = x << 8
    recoverArr = [0]*32
    table = getTable()
    indexArr = getArr2()

    stack = [0]*32
    for i in range(0, 32):
        tmp = stack[indexArr[x//8 + i]] = dstArr[i]
        for j in range(0, 256):
            if table[x+j] == tmp:
                recoverArr[indexArr[x//8 + i]] = j
                break
    return recoverArr


def main(target):

    generatedArr3 = target
    generatedArr2 = recoverGeneratedArr_x(generatedArr3, 3)
    generatedArr1 = recoverGeneratedArr_x(generatedArr2, 2)
    generatedArr0 = recoverGeneratedArr_x(generatedArr1, 1)
    userInput = recoverGeneratedArr_x(generatedArr0, 0)

    res = ''
    for i in userInput:
        res += chr(i)
    print(res)


def find_target():
    target = [0xe6, 0x1f, 0xf9, "t", "\"", 'h', 0xf9, 0xc7, 0x8d, '\"',
              '{', ':', 0xae, 'H', '1', 0xcb, 0xcb, '\"', 'F', 0x05, 0xce, '>', 0xcd, '+', 0x12, ' ', '{', 'P', 0x83, 0xb8, 0xcf, '{']

    order = ["local_c7",
             "local_e0",
             "local_d2",
             "local_cd",
             "local_c9",
             "local_df",
             "local_c3",
             "local_c5",
             "local_c6",
             "local_d4",
             "local_c1",
             "local_da",
             "local_d6",
             "local_d1",
             "local_c2",
             "local_d9",
             "local_d5",
             "local_db",
             "local_ca",
             "local_d0",
             "local_cb",
             "local_dd",
             "local_cc",
             "local_d8",
             "local_c4",
             "local_d3",
             "local_cf",
             "local_de",
             "local_d7",
             "local_dc",
             "local_c8",
             "local_ce"]

    out = []
    for i in target:
        if(isinstance(i, str)):
            out.append(ord(i))
        else:
            out.append(i)
    tmp = []
    for i in range(len(order)):
        tmp.append((order[i], out[i]))
    tmp.sort(reverse=True)
    out = []
    for i in tmp:
        out.append(i[1])
    return(out)


def exploit():
    main(find_target())


exploit()
