nums=[1,2,3,3,3,3,3,3,5,6,7,8,9,9,10]
n=len(nums)-1
target=3 
low=0
high=n-1
f=-1
l=n
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        f=mid
        high=mid-1
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
low=0
high=n-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        l=mid
        low=mid+1
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
print("smallest index",f)
print("largest index",l)

