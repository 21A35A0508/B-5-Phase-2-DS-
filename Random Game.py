import random
n=random.randrange(1,50)
guess=int(input("enter a number:"))
while n!=guess:
    if guess<n:
        print("low")
        guess=int(input("enter number again:"))
    elif(guess>n):
        print("high")
        guess=int(input("enter number again:"))
    else:
        break
print("correct")
