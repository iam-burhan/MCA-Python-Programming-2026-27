import random
target = random.randint(1, 100)
guess = None

print("Guess the number between 1 and 100!")

while guess != target:
    guess = int(input("Enter your guess: "))
    if guess < target:
        print("Too Low! Try again.")
    elif guess > target:
        print("Too High! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")