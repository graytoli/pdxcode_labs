# Lab 12: Guess the Number, version 3
import random

num = random.randint(1, 10)
i = 0

while True:
    user_input = int(input('Guess the number: ').strip())
    i += 1
    if user_input == num:
        break
    else:
        if user_input < num:
            print('Too low! Try again!')
        else:
            print('Too high! Try again!')

if i == 1:
    print('You got it! You guessed it on the first try!')
else:
    print(f'You got it! You guessed {i} times.')
