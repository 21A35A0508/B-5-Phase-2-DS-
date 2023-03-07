class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single:
    def __init__(self):
        self.head=None
    def insert_at_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
          temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while (temp):
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=Single()
n1=Node(10)
obj.head=n1
n2=Node(12)
n1.next=n2
n3=Node(13)
n2.next=n3
obj.display()
print(" ")
obj.insert_at_position(2,100)
obj.display()
