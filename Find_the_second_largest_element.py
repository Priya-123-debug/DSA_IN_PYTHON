nums=[1,2,3,4,5,6,8]
largest=nums[0]
second=nums[0]
n=len(nums)
for i in range(1,n):
    if nums[i]>largest:
        second=largest
        largest=nums[i]

    elif nums[i]<largest and nums[i]>second:
        second=nums[i]
print(largest,second)
    

