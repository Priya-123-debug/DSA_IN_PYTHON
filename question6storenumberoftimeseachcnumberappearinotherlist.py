nums = [5, 7, 5, 1, 7, 7, 9]
queries = [7, 5, 2, 9] 
freq={}
for i in range(len(nums)):
    freq[nums[i]]=freq.get(nums[i],0)+1
ans=[]
for i in range(len(queries)):
    print(freq.get(queries[i],0))
    ans.append(freq.get(queries[i],0))
print(ans)