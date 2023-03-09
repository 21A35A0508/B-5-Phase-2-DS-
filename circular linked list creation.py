class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    def add(self,data):
        new=Node(data)
        if self.head.data is None:
            self.head=new
            self.tail=new
            new.next=self.head
        else:
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
    def display(self):
            current=self.head
            if self.head is None:
                print("empty")
                return
            else:
                print("nodes of circular linked list")
                print(current.data,"-->")
                while(current.next!=self.head):
                    current=current.next
                    print(current.data,"-->")
class Circular:
    c = cll()
    c.add("p")
    c.add("a")
    c.add("v")
    c.add("a")
    c.add("n")
    c.add("i")
    c.display()
