from pwn import *
context.log_level = 'error'
def BinaryToDecimal(binary): 

	string = int(binary, 2) 
	return string 

def Bin2Str(bin):
    str_data =' ' 
    for i in range(0, len(bin), 7): 
    	temp_data = bin[i:i + 7] 
    	decimal_data = BinaryToDecimal(temp_data) 
    	str_data = str_data + chr(decimal_data) 
    return str_data


ans=['0']*301
host,port='2020.redpwnc.tf',31284
for i in range(1,300):
    print("Getting Every "+str(i+1)+" Bits")
    s = remote(host,port)
    s.sendline(str(i))
    s.sendline(str(i+1))
    res=s.recvline()
    res=list(str(res).replace("b'Enter an integer i such that i > 0: Enter an integer j such that j > i > 0: Ciphertext: ","").replace("\\n'",''))
    for j in range(len(res)):
        if(j%(i+1)==0):
            ans[j]=str(int(res[j])^1)
    print(Bin2Str(''.join(ans)))
print(''.join(ans))
