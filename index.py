# Rock Paper Scissors Game

import random

#game choices

choices = ["rock, paper , scissors"]

#user input

user_choice = input("Choose rock, paper, or scissors: ").lower()

#computer input

computer_choice = random.choice(choices)

#game logic

if user_choice == computer_choice:
    print(f"You chose {user_choice} and the computer chose {computer_choice}. It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")

else:
    print(f"Computer Wins!{computer_choice} beats {user_choice}")