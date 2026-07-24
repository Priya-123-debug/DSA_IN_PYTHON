from math import sqrt
result=[]
def collect(num):
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
        if num//i!=i:
            result.append(i)
    result.sort()
    return result
print(collect(20))