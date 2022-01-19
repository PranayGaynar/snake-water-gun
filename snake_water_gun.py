import random
print("1 for snake,2 for water, 3 for gun")
user=int(input("Enter a value: "))
if user==1:
    print("snake")
elif user==2:
    print("water")
if user==3:
    print("gun")
comp=random.randint(1,3)
if comp==1:
    print("snake")
elif comp==2:
    print("water")
elif comp==3:
    print("gun")
def result(x,y):
        
    if x==1:
        if y==1:
            print("game is tied!!") 
        elif y==2:
            print("you win") 
        elif y==3:
            print("you loose") 
    elif x==2:
        if y==1:
            print("you loose")
        elif y==2:
            print("game is tied!!")
        elif y==3:
            print("you win")
    elif x==3:
        if y==1:
            print("you win!!")
        elif y==2:
            print("you loose")
        elif y==3:
            print("game is tied!!")
result(user,comp)
# this code created by pranay gaynar!!