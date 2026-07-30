nums=[1,0,2,4,3,0,0,3,5,1]
# ans=[]
# for i in range(0,len(nums)):
#     if nums[i]!=0:
#         ans.append(nums[i])
# idx=0
# for i in range(0,len(ans)):
#     nums[idx]=ans[i]
#     idx+=1
# print(ans)
i=0
for i in range(0,len(nums)):
    if nums[i]==0:
        break
for j in range(i,len(nums)):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    
   

print(nums[0:i])