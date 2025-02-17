import random
'''1 for rock
-1 for paper
0 for scissor'''
while True:
    com=random.choice([1,0,-1])
    youstr=input("Enter your choice: ")
    youdict={"rock":1,"paper":-1,"scissor":0}
    you=youdict[youstr]

    if(you==1 and com==-1):
        print("You choose rock")
        print("Computer choose paper")
        print("You lost")
    elif(you==1 and com==0):
        print("You choose rock")
        print("Computer choose scissor")
        print("You won")
        break
    elif(you==-1 and com==1):
        print("You choose paper")
        print("Computer choose rock")
        print("You won")
        break
    elif(you==-1 and com==0):
        print("You choose paper")
        print("Computer choose scissor")
        print("You lost")
    elif(you==0 and com==1):
        print("You choose scissor")
        print("Computer choose rock")
        print("You lost")
    elif(you==0 and com==-1):
        print("You choose scissor")
        print("Computer choose paper")
        print("You won")
        break
    elif(you==com):
       print("Draw")
    else:
        print("Invalid Error")