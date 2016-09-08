import random

secretNumber = random.randint(1,20)
print('guess a number between 1 and 20')

for guessesTaken in range(1,7):
    print('your guess:')
    guess = int(raw_input())

    if guess < secretNumber:
        print('too low')

    elif guess > secretNumber:
        print('too high')

    else:
        break

if guess == secretNumber:
    print('You guessed it in ' + str(guessesTaken) + ' guesses')

else:
    print('The number was ' + str(secretNumber))
