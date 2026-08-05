nums = [1,99,101,98,2,5,3,99,100]

count = 1
i = 1
n = len(nums)
maxe = 1

while i < n:

    while i < n and nums[i] - nums[i-1] == 1:
        count += 1
        i += 1

    maxe = max(maxe, count)
    count = 1
    i += 1

print(maxe)