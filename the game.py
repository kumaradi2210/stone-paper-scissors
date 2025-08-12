import random

print("Welcome to Stone Paper Scissors Game!")
print("Enter your choice: stone, paper, or scissors")

user_choice = input("Your choice: ").lower()
choices = ["stone", "paper", "scissors"]
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "stone" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "stone") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
elif user_choice in choices:
    print("You lose!")
else:
    print("Invalid input. Please choose stone, paper, or scissors.")