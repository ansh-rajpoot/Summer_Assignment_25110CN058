# Write a program to Create number guessing
# game.
import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a secret number between 1 and 100.")
    
    while True:
        user_guess = int(input("\nEnter your guess: "))
        attempts += 1
        
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\nCONGRATULATIONS! You guessed it in {attempts} attempts.")
            break

guess_the_number()
