nums=[5,10,-3,-1,-10,6] 
n=len(nums)
result=[0]*n 
posind=0
negind=1
for i in range(0,n):
    if nums[i]>=0:
        result[posind]=nums[i]
        posind+=2
    else:
        result[negind]=nums[i]
        negind+=2
print(result)
    