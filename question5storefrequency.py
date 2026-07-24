#there are two methods 
num=[1,2,3,4,2,4,55,6,3,2,34,55,6,7,3,2,1]
#here i used dictionary map 

hashmap = {}
n = len(num)

for i in range(0, n):
 hashmap[num[i]] = hashmap.get(num[i], 0) + 1

print(hashmap[num[0]])
print(hashmap[6])
