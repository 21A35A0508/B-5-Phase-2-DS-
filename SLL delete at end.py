class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
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
print("Delete at end:")
obj.delete_end()
obj.display()
