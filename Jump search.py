import math
def jump(arr,x,n):
    step=math.sqrt(n)
    prev=0
    a=arr[int(min(step,n)-1)]
    print("a:",a)
    while arr [int(min(step,n)-1)]<x:
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
        while arr[int(prev)]<x:
            prev+=1
            if prev == min(step,n):
                return -1
            if arr[int(prev)]==x:
                return prev
            return -1
arr=[0,1,1,2,4,5,9,13,21,34,55,89,144,300,377,710]
x=21
n=len(arr)
index=jump(arr,x,n)
print("number",x,"is at index","%.0f" %index)
