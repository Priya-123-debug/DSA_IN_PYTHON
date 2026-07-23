
def reverse(num):
    result=0
    while(num>0):

        id=num%10
        result=(result*10)+id
        num=num//10
    return result
n=12321
r=reverse(n)
t= n==r 
if(t):
    print("palindrome")
else:
    print("not palindrome")
