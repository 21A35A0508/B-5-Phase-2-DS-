queue=[]
def enqueue():
    element=input("enter element")
    queue.append(element)
    print(element,"is added,to queue")
def dequeue():
    if not queue:
        print("empty")
    else:
        e=queue.pop(0)
        print("removed:",e)
def display():
    print(queue)
while True:
    print("select choice 1.enqueue 2.dequeue 3.display 4.quit")
    choice=int(input("enter choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter right choice.")
