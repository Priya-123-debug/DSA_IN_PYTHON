nums=[5,9,1,2,4,15,6,3]
target=13
nums.sort()
i=0
j=len(nums)-1
count=0
while i<j:
    if nums[i]+nums[j]==target:
        i+=1
        j-=1
        count+=1
    elif nums[i]+nums[j]<target:
        i+=1
    else:
        j-=1
print(count)
    