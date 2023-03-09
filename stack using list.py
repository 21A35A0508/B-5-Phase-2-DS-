stack=[]
def push():
    element =int(input("enter element:"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("empty stack")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
while True:
    print("select:1.push 2.pop 3.quit")
    choice=int(input("enter choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        quit()
    else:
        print("enter correct choice")
