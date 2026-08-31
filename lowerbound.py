nums=[1,1,1,2,3,4,5,6,7,8,9,12,12,13] 
n=len(nums)
lb=0 
low=0
high=n-1 
target=1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(lb)
