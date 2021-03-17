#!/usr/bin/env python3
import string
def encode(msg):
    output = ''

    for i in range(len(msg)):
        temp = ord(msg[i]) * 0x40
        temp = temp >> 4
        if 0xc0 <= temp < 0xe8:
            output = str(int(msg[i]) * 0x1234) + output
        else:
            output = chr(ord(msg[i]) * 0x10) + output

    return output


def decode(msg):
    out = ''
    for i in msg:
        flag=False
        for j in range(0,200):
            if(encode(chr(j))==i):
                out=out+str(chr(j))
                flag=True
                break
        if(flag==False):
            out+='*'
    
    return out


def shift(msg):
    j = len(msg) - 1
    output = ''

    for i in range(len(msg)//2):
        output += msg[i] + msg[j]
        j -= 1

    return output

def unshift(msg):
    out = ['']*1000

    for i in range(0,len(msg)-1,2):
        out[i]=msg[i]
        out[55-(i)]=msg[i+1]
    return(''.join(out))


if __name__ == '__main__':
    hashed = '4660۠ܰ4660ڀ٠װװސ23300۰ސݐ18640ܠݰװۀڠ18640۰ްؠѠȐՀȐа4660ѠȐѠߐА'
    print(decode(hashed))


