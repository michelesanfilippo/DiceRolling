# 24/03/2020 Michele Sanfilippo
# Simple python project about dice rolling

import random
from PIL import Image

print("Let's Roll the dice. . .")

while True:
    user_decision = input("Want to roll? YES or NO : ")
    if user_decision  == "no":
        print("Ending. . .")
        break
    if user_decision == "yes":
        number = random.randint(1,6)
        if number == 1:
            image = Image.open("dices/dice1.png")
            print("Number extracted: " + str(number))
            image.show()
        if number == 2:
            image = Image.open("dices/dice2.png")
            print("Number extracted: " + str(number))
            image.show()
        if number == 3:
            image = Image.open("dices/dice3.png")
            print("Number extracted: " + str(number))
            image.show()
        if number == 4:
            image = Image.open("dices/dice4.png")
            print("Number extracted: " + str(number))
            image.show()
        if number == 5:
            image = Image.open("dices/dice5.png")
            print("Number extracted: " + str(number))
            image.show()
        if number == 6:
            image = Image.open("dices/dice6.png")
            print("Number extracted: " + str(number))
            image.show()



