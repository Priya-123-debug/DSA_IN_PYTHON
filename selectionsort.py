def selectionsort(arr):
    n=len(arr)
    for i in range(n-1):
        minin=i
        for j in range(i+1,n):
            if arr[j]<arr[minin]:
                minin=j
        arr[i],arr[minin]=arr[minin],arr[i]
    return arr 
arr=[64,25,12,22,11]
print(arr)
selectionsort(arr)
print(arr)