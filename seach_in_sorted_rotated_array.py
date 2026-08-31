nums=[17,18,20,1,3,4,5,7,8,10,11,13,14,16]
n=len(nums)
low,high=0,n-1
ans=-1
target=14
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        ans=mid
    if nums[mid]<=nums[high]:

        if nums[mid]<=target<=nums[high]:
            low=mid+1
        else:
            high=mid-1
    else:
         if nums[low]<=target<=nums[mid]:
                    high=mid-1

         else:
    
    
            high=mid-1
print(ans)

    
    
