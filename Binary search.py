pos=-1
def binary(list,n):
    l=0
    h=len(list)-1
    while l<=h:
        mid=(l+h)//2
        if(list[mid])==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                h=mid-1
    return False
list=[5,10,15,100]
n=100
if binary(list,n):
    print("found")
else:
    print("not found")
