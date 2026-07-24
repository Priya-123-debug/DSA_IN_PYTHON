#armstrong digit power of digit is same as no of digit 
# 132 is 1*3+3*3+2*3 
def armstrong(num):
    total=0
    ln=len(str(num))
    while num>0:
        id=num%10
        total=total+(id**ln)
        num=num//10
    return total==num


for i in range(5000,5020):
    print(armstrong(i))


#time complexity is logbase10 (n)
#base depends on by which we divide 


