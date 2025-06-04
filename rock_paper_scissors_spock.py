import random

# Game layout
print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================\n")

print("1) ✊ (Rock)")
print("2) ✋ (Paper)")
print("3) ✌️ (Scissors)")
print("4) 🦎 (Lizard)")
print("5) 🖖 (Spock)\n")

# Keep asking until the player gives valid input
while True:
    player = int(input("Pick a number (1-5): "))
    if 1 <= player <= 5:
        break
    else:
        print("Invalid input! Please choose a number between 1 and 5.\n")

# Show player’s choice
if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")
elif player == 4:
    print("You chose: 🦎")
else:
    print("You chose: 🖖")

# CPU makes a choice
computer = random.randint(1, 5)

# Show computer’s choice
if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
elif computer == 3:
    print("CPU chose: ✌️")
elif computer == 4:
    print("CPU chose: 🦎")
else:
    print("CPU chose: 🖖")

# Winning conditions
if player == computer:
    print("It's a tie!")
elif (player == 1 and (computer == 3 or computer == 4)) or \
     (player == 2 and (computer == 1 or computer == 5)) or \
     (player == 3 and (computer == 2 or computer == 4)) or \
     (player == 4 and (computer == 2 or computer == 5)) or \
     (player == 5 and (computer == 1 or computer == 3)):
    print("The player won!")
else:
    print("The computer won!")

