def fibonaci(num):
    if num==0 or num==1:
        return num
    return fibonaci(num-1)+fibonaci(num-2)
print(fibonaci(2))