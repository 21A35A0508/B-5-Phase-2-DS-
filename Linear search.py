pos=-1
def linear(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
list=[100,40,20,10]
n=20
if linear(list,n):
    print("found at index:",pos+1)
else:
    print("not found")
