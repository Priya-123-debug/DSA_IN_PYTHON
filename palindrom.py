def fucn(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return fucn(s,left+1,right-1)
s="aabbaad"
t=fucn(s,0,len(s)-1)
print(t)
