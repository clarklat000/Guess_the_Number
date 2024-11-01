from random import randint

# Generate a random number between 1 and 10 using randint
random_num = randint(1, 10)

while True:
    # Ask the user for a number using the int and input functions
    guess = int(input("Guess a number between 1 and 10: "))

    if guess > random_num:
        print("Too high! Try again.")
    elif guess < random_num:
        print("Too low! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break