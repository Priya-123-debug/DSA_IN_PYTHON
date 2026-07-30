arr=[5,8,1,6,9,2,4] 
# adjacent swap  
l=len(arr)
def bubble_sort(num):
    for i in range(0,l-1):
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
bubble_sort(arr)
print(arr)

# tc o(n2)


