def insert(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
arr=[5,99,3,-222,-3,12,50]
insert(arr)
print("sorted:")
for i in range(len(arr)):
    print("%d" %arr[i],end=" ")
