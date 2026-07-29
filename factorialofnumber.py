def fact(num):
    if num==0|num==1:
        return num
    return num*fact(num-1)
print(fact(5))
print(fact(8))
print(fact(9))