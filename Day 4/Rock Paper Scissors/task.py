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
images = [rock, paper, scissors]
random_num_for_computer = random.randint(0, len(images) - 1)
computer_choice = images[random_num_for_computer]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
user_image = images[user_choice]
print(computer_choice)
print("Computer chose:")
print(user_image)
print("User chose:")

if random_num_for_computer == 0 and user_choice == 1:
    print("You win!")
elif random_num_for_computer == 1 and user_choice == 2:
    print("you win")
elif random_num_for_computer == 2 and user_choice == 0:
    print("you win")
elif random_num_for_computer == user_choice:
    print("Draw")
else:
    print("You lose")