import random

while True:
    user_input=input("Chooses any one (rock,paper,scissors) or 'exit' to stop:").lower()
    choices=["rock","paper","scissors"]
    if (user_input=="exit"):
        print ("Thanks For Playing")
        break
    elif(user_input not in choices):
        print ("Invaild choice")
        break
    else:
        computer_choice=random.choice(choices)
        print(f"computer choice is {computer_choice}")
        if (user_input =="rock" and computer_choice=="scissors")or(user_input =="scissors" and computer_choice=="paper")or (user_input =="paper" and computer_choice=="rock"):
            print("player will win")
        elif (user_input == computer_choice):
            print ("match is tie")
        else:
            print ("computer will win")