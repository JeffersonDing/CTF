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
