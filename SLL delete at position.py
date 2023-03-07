class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single:
    def __init__(self):
        self.head=None
    def delete_at_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
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
n4=Node(14)
n3.next=n4
obj.display()
print(" ")
print("Delete at a given position:")
obj.delete_at_position(1)
obj.display()
