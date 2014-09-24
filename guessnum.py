import random

guesses_taken = 0
number = random.randint(1, 20)

while guesses_taken < 6:
    guess = int(input("Guess a number between 1 & 20: "))
    guesses_taken += 1
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Well done, you correctly guessed", number)
        break

print("Game over")
