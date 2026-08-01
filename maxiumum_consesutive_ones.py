nums=[1,1,1,0,0,1,1,1,1,0,1,1]
count=1
maxec=0
l=len(nums)
i=1
while i<l:
    if  nums[i-1]==nums[i]:
        count+=1
        i+=1
    else:
        maxec=max(maxec,count)
        count=1
        i+=1


print(max(count,maxec))

