b=[]
def ss(a):
    k=0
    for i in range(0,len(a)):
        k=min(a)
        b.append(k)
        a.remove(k)
a=[3,20,2,5,50]
ss(a)
print(b)
