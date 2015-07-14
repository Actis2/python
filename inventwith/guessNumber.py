# This is a guess the number game.

import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 50)
print('Well,'+ myName + ', I am thinking of a number between 1 and 50.')

while guessesTaken < 10:
    print('Take a guess.') 
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') 

    if guess > number:
        print('You guess is too high.')

    if guess == number:
        break

if guess == number and guessesTaken == 1:
    print('Holy-moly you guessed it on the first try!')
    
if guessesTaken == str(guessesTaken) and guessesTaken > 1:#casting string
    print('Good job,' + myName + '! You guessed my number in ' + str(guessesTaken) +' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
