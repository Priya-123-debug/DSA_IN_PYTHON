nums=[7,7,7,7,7,7,7,7,1,2,3,4,5,7,7]
n=len(nums)
low,high=0,n-1
target=5
ans=False
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        ans=True
    if nums[mid]==nums[low]==nums[high]:
        low+=1
        high-=1
        continue
    if nums[mid]<=nums[high]:
         if nums[mid]<=target<=nums[high]:
             low=mid+1
         else:
             high=mid-1
    else:
         if nums[mid]<=target<=nums[high]:
                     high=mid-1
         else:
                     low=mid+1



print(ans)

        


        