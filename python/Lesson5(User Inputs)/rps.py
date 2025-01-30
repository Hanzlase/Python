# val=input('Please enter a value :')
# print(val)
import sys
import random
from enum import Enum

class rps(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

print(rps(2))
print(rps.ROCK)
print(rps['ROCK'])
print(rps.ROCK.value)
# sys.exit()

print("")
plyr_ch=input("Enter...\n1 for Rock\n2 for paper\n3 for Scissors\n" )
ch=int(plyr_ch)
if ch<1 or ch>3:
    sys.exit("You must Enter 1,2 or 3.")
    
computerch=random.choice("123")
computer=int(computerch)

print("")
print("You choose "+str(rps(ch)).replace('rps.',' ')+".")
print("Python choose "+str(rps(computer)).replace('rps.',' ') +".")
print("")


if ch==1 and computer==3:
    print("🥳You Win")
elif ch==2 and computer==1:
    print("🥳You Win")
elif ch==3 and computer==2:
    print("🥳You Win")
elif ch==computer:
    print("😲Draw")
else:
    print("🐍python Wins")