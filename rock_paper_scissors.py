import random

# The Game layout 
print('===================')
print('Rock Paper Scissors')
print('===================')

print('1) ✊')
print('2) ✋')
print('3) ✌️')

# Keep asking until valid input is given
while True:
    player = int(input('Pick a number (1-3): '))
    if 1 <= player <= 3:
        break
    else:
        print("Invalid input!  choose a number between 1 and 3")

# Show player's choice
if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
else:
    print('You chose: ✌️')

# CPU randomly picks
computer = random.randint(1, 3)

# Show computer's choice
if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
else:
    print('CPU chose: ✌️')

# Determine the winner
if player == computer:
    print("It's a tie!")
elif (player == 1 and computer == 3) or \
     (player == 2 and computer == 1) or \
     (player == 3 and computer == 2):
    print("The player won!")
else:
    print("The computer won!")
