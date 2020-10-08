import base64
f = open('cipher.txt', 'r') 
cipher = f.read()
ptxt=cipher
for i in range(25):
    ptxt = base64.b64decode(ptxt)
print(ptxt)