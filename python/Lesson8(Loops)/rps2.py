import sys
import random
from enum import Enum

class rps(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(rps(2))
print(rps.ROCK)
print(rps['ROCK'])
print(rps.ROCK.value)

playagain = True

while playagain:
    print("")
    plyr_ch = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissors\n")
    
    try:
        ch = int(plyr_ch)
    except ValueError:
        sys.exit("Invalid input! Please enter a number between 1 and 3.")
    
    if ch < 1 or ch > 3:
        sys.exit("You must enter 1, 2, or 3.")
    
    computer = random.randint(1, 3)
    
    print("\nYou chose " + str(rps(ch)).replace('rps.', '') + ".")
    print("Python chose " + str(rps(computer)).replace('rps.', '') + ".")
    print("")
    
    if (ch == 1 and computer == 3) or (ch == 2 and computer == 1) or (ch == 3 and computer == 2):
        print("🥳 You Win")
    elif ch == computer:
        print("😲 Draw")
    else:
        print("🐍 Python Wins")

    playagain=input("\n Play Agian\n Y for yes \n Q to quit")
    if(playagain.lower()=="y"):
        continue
    else:
        print("Thanks")
        break
sys.exit("Bye")