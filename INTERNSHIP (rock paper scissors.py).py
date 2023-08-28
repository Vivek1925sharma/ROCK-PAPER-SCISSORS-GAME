import random

print("~~~~~~~~~~~~~~~~WELCOME TO ROCK PAPER SCISSORS GAME ~~~~~~~~~~~~~~~~")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here:")
print("""
WINNING RULES:
1. Paper vs Rock --> Paper
2. Rock vs scissors --> Rock
3. scissors vs Paper --> Scissors""")

print("""Choices are:
    1. Rock
    2. Paper
    3. Scissors""")
choice = int(input("enter your choice from 1-3: "))
print()
while choice > 3 or choice < 1:
    choice = int(input("enter valid input"))

if choice == 1:
    user_choice = "Rock"
elif choice == 2:
    user_choice = "Paper"
else:
    user_choice == "Scissors"

print("The user's choice is",user_choice)
print("Now it is Computer's turn")

computer = random.randint(1,3)

if computer == 1:
    comp_choice = "Rock"
elif computer == 2:
    comp_choice = "Ppaer"
else:
    comp_choice = "Scissors"

print("The computer's choice is",comp_choice)

if ((user_choice == "Paper" and comp_choice == "Rock") or(user_choice == "Rock" and comp_choice == "Paper")):
   print("Paper wins")
   result = "Paper"
elif ((user_choice == "Paper" and comp_choice == "Rock") or(user_choice == "Rock" and comp_choice == "Paper")):
   print("Rock wins")
   result = "Rock"
elif (user_choice == comp_choice):
   print("it's a tie")
   result = "Tie"
else:
    print("Scissors wins")
    result = "Scissors"

if result == "Tie":
    ties +=1
elif result == user_choice:
    print("user wins")
    user_choice += 1
else:
    print("computer wins")
    comp_score += 1

print("Scores are")
print(name,"'s score is",user_score)
print("computer's score is", comp_score)
print("ties are",ties)


print("Game Over!")
print('Thanks')



