import queue
l=queue.Queue(maxsize=2)
l.put(20)
l.put(10)
print(type(l))
print(l.get())
print(l.get())

create 2 stacks of same size
stack1=[]
stack2=[]
def push():
    for i in range(5):
        element = int(input("enter element:"))
        if element%2==0:
            stack1.append(element)
        else:
            stack2.append(element)
def pop_element():
    op=int(input("1 or 2"))
    if op=='1':
        if not stack1:
          print("empty stack")
        else:
            e = stack1.pop()
            print("removed element:", e)
            print(stack1)
    else:
        if not stack2:
          print("empty stack")
        else:
            e = stack2.pop()
            print("removed element:", e)
            print(stack2)
def show():
    what=input("enter choice:")
    if what=='1':
        print(stack1)
    else:
        print(stack2)
while True:
    print("select:1.push 2.pop 3.show 4.quit")
    choice=int(input("enter choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        show()
    elif choice==4:
        break
    else:
        print("enter correct choice")
