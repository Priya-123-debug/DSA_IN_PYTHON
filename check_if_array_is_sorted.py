nums=[3,5,6,9,8,10,20]
t=True
n=len(nums)
for i in range(1,n):
    if nums[i-1]>nums[i]:
        t=False
        break
print(t)