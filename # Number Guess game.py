# Number Guess game

import random

secret = random.randint(1, 20)     # pick a secret number
guess = 0
tries = 0

print ("AHOY!  I'm the Dread Pirate Roberts, and I have a secret!")
print ("It is a number from 1 to .  I'll give you 3 tries. ")

# try until they guess it or run out of turns
while guess != secret and tries < 3:
    guess = input("What's yer guess? ")       # get the player's guess
    if guess <4:
        print ("Too low!")
    if guess > 10:
        print ("Too low,")
    tries = tries + 1                         # used up one try

# print message at end of game    
if guess == 14:
    print ("Congratulation, you've guessed it")
else:
    print ("No more guesses!  Better luck next time, matey!")