import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_input = int(input("Please enter 0 For 'Rock', 1 for 'Paper' and 2 for 'Scissors' \n"))
OPTIONS = [rock, paper, scissors]

player_choice = OPTIONS[player_input]
print(f"You chose {player_choice}")

computer_choice = random.choice(OPTIONS)
print(f"Computer chose{computer_choice}")

WINNING_MOVES = {
    rock : scissors,
    scissors : paper,
    paper : rock
}

if player_choice == computer_choice:
    print("It's a draw!")
elif WINNING_MOVES[player_choice] == computer_choice:
    print("You win!")
else:
    print("You lose!")
