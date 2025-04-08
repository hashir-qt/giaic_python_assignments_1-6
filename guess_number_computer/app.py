import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry! guess again. Number is too low")
        elif guess > random_number:
            print("Sorry! guess again. Number is too high")
    print(f"Yay! Congrats you guessed the number {random_number} correctly")

guess(10)