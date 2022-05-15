

import random

print ("Number Guessing Game")

#randint = function to generate random numbers between the range
number = random.randint(1,9)

chances = 0

print ("Guess a Number (between 1 and 9):")

while chances <5 :

    guess = int(input ("Enter Your Guess:-"))

    if guess == number:
        print ("CONGRATULATIONS YOU WON!!!")
        #break = break from loop (loop control statement)
        break

    elif guess < number:
        print ("Your guess is too low: Guess a higher number than", guess)
    
    else guess > number:
        print ("Your guess is too high: Guess a lower number than", guess)

    chances += 1

    if not chances < 5:
        print ("YOU LOSE! The number is", number)