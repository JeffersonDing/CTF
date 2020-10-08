nums=[1,10,3,2,5,9,8,7,4,6]
P=False
import operator
def check():
    i=0
    while(True):
        if(8<i):
            return True
        if(nums[i+1]<nums[i]):
            break
        i+=1
    return False



while(True):
    n=int(input())
    if(n>8):
        break
    nums[n]=operator.xor(nums[n],nums[n+1])
    nums[n+1]=operator.xor(nums[n+1],nums[n])
    nums[n]=operator.xor(nums[n],nums[n+1])
    print(nums)
    P=check()
if(P):
    print("got it")
else:
    print("nope")
