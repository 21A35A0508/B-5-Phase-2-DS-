def bubble(list):
    for i in range(len(list)-1,0,-1):
        print("i value:",i)
        for j in range(i):
            print(j)
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
list=[200,-2,0,7,5]
bubble(list)
print(list)
