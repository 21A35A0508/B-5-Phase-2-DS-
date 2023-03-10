n=int(input("enter size"))
a=list(map(int,input().split(" ")))[n:] #indexing for position
sum=0
for i in a:
    #print(i,end=" ")
    sum = sum + i
print(sum)
