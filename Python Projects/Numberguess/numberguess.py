import random

def main():
    min = 1
    max = get_max()
    rand = get_rand(min, max)
    user_guess(rand, max)
    print(f"Well done! You correctly guessed the random number was {rand}")
    guess = comp_guess(min)
    print(f"The computer correctly guessed your number, which was {guess}")

def get_max():
    return int(input("Pick a number to guess up to: "))

def get_rand(min, max):
    return random.randint(min, max)

def user_guess(rand, max):
    print(f"The computer has generated a random number between 1 and {max}")
    guess = 0
    while guess != rand:
        guess = int(input("Enter your guess: "))
        if guess > rand:
            print("Sorry too high. Guess again.")
        elif guess < rand:
            print("Sorry too low. Guess again")

def comp_guess(min):
    print("This time the computer will guess your number")
    max = get_max()
    feedback = ""
    while feedback != "c":
        guess = get_rand(min, max)
        feedback = input(f"Is the computer's guess of {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            max = guess - 1
        elif feedback == "l":
            min = guess + 1
    return guess

    
if __name__ == "__main__":
    main()
