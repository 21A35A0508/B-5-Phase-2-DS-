class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
         if self.head is None:
              print("empty")
         else:
              temp=self.head
              while(temp):
                  print(temp.data,"-->",end=" ")
                  temp=temp.next
obj=SLL()
n1=Node(100)
obj.head=n1
n2=Node(200)
n1.next=n2
n3=Node(300)
n2.next=n3
print("beforensertion")
obj.display()
print(" ")
print("afternsertion of 70")
obj.insert(70)
obj.display()
print(" ")
print("afternsertion of 50")
obj.insert(50)
obj.display()
