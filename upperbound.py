nums=[1,2,3,4,5,6,7,8,8,9,10]
target=5
n=len(nums)
ans=n
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>target:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
