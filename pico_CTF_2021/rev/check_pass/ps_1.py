from struct import unpack
from idc import GetManyBytes


def getTable():
    num = 1024
    size = 1
    address = 0x39560

    table = []
    for i in xrange(0, num, size):
        data = GetManyBytes(address + i, size)
        table.append(unpack('B', data)[0])

    return table


def getArr2():  # Arr2 as Index of stack
    num = 128
    size = 8
    address = 0x39970

    arr2 = []
    for i in range(0, size*128, size):
        data = GetManyBytes(address + i, size)
        arr2.append(unpack('<Q', data)[0])
    return arr2


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


def main():
    target = [31, 153, 80, 194, 184, 34, 58, 203, 69, 167, 174, 203, 158, 32, 207,
              72, 5, 123, 123, 184, 205, 153, 70, 244, 207, 230, 119, 205, 43, 230, 119, 123]

    generatedArr3 = target
    generatedArr2 = recoverGeneratedArr_x(generatedArr3, 3)
    generatedArr1 = recoverGeneratedArr_x(generatedArr2, 2)
    generatedArr0 = recoverGeneratedArr_x(generatedArr1, 1)
    userInput = recoverGeneratedArr_x(generatedArr0, 0)

    res = ''
    for i in userInput:
        res += chr(i)
    print(res)


main()
