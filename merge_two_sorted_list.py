nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,4,6,7,8,9,10]
i=0
j=0
m=len(nums1)
n=len(nums2)
ans=[]
while i<m and j<n:
    if not ans:
        ans.append(nums1[i])
        i+=1
    elif nums1[i]<=nums2[j]:
        if ans[-1]!=nums1[i]:

            ans.append(nums1[i])
        i+=1
    elif nums2[j]<nums1[i]:
        if ans[-1]!=nums2[j]:
            ans.append((nums2[j]))
        j+=1
while i<m:
    if ans[-1]!=nums1[i]:

        ans.append(nums1[i])
    i+=1
while j<n:
    if ans[-1]!=nums2[j]:
        ans.append(nums2[j])
    j+=1
print(ans)
