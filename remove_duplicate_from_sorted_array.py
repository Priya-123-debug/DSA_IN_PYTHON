nums = [1, 1, 1, 2, 3, 4, 4, 5, 4, 5, 7, 8, 9, 10]
ans = []
n = len(nums)
i = 0

while i < n:
    # If ans is empty, safely add the first element
    if not ans:
        ans.append(nums[i])
    # If the current number matches the last added number, skip it
    elif ans[-1] == nums[i]:
        pass  # Do nothing, just move to the next index
    # Otherwise, it's a new unique number, so add it
    else:
        ans.append(nums[i])
        
    i += 1  # Always move the index forward to avoid infinite loops

print(ans)
