import random

name = input('Hello! What is your name?')

number = random.randint(1, 20)

print(f'Well, {name}, I am thinking of a number between 1 and 20.')

tries = - 1
cnt = 1

while(number != tries):
    tries = int(input("Take a guess."))
    if(tries == number):
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
    elif(tries > number):
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    cnt = cnt + 1






