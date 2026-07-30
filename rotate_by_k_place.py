nums=[3,9,6,7,2,10,9]
n=len(nums)
k=3
def reverse(left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
reverse(n-k,n-1)
reverse(0,n-k)
reverse(0,n-1)
print(nums)

