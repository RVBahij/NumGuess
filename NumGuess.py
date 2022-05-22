import random
import os
import time

def clear():
    os.system("clear")
    print()

x = random.randint(1, 9)

clear()
time.sleep(1)
print("Guess The Number!")
print("Number range 1 > 9\n")
print("You have 4 guess :)\n")


time.sleep(6)


for i in range(1, 5):
    clear()
    y = int(input(f"Enter guess number {i}: "))
    if y == x:
        print("\nGG! You won!\n\n")
        break
    elif y != x:
        print("\nWrong guess...\n\n")
        time.sleep(2)

if x != y:
    clear()
    print("You lost :(\n")
    print(f"The answer was {x}!\n\n")


