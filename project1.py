'''
rules: of project is rock ,seizers, paper:
rock->0
seizers->1
paper->2
OPERATION :

user enter                     computer choice
0                                 0 draw 
0                                 1 user win 
0                                 2 computer win

1                                 0   computer wins 
1                                 1    draw
1                                 2   user wins

2                                 0   user  wins 
2                                 1   computer wins
2                                 2  draw

condition 
if user<computer or(user==2 and computer==0)---user wins 
elif user>computer or(user==0 and computer==2)---computer wins
elif(user==computer)---- match draw 

 
'''
import random
while True:
    user_choice=int(input("enter the choice 0 for rock and 1 for seizers and 2 for paper: "))
    computer_choice=random.randint(0,2)
    print("Computer choise is :{}".format(computer_choice))
    if user_choice== computer_choice:
        print("MATCH DRAWS ")
    elif user_choice==2 and computer_choice==0:
        print('YOU WINS')
    elif user_choice==0 and computer_choice==2:
        print("COMPUTER WINS")
    elif user_choice<computer_choice:
        print("YOU WINS ")
    elif user_choice>computer_choice:
        print("COMPUTER WINS")
    else:
        print("enter valid input!")