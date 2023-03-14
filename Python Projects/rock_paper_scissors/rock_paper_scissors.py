import random

def main():
    print(play())

def play():
    while True:
        user = input("Would you like to play rock (r), paper (p), or scissors (s)? ").lower()
        if user in ["r", "p", "s"]:
            break
        else:
            print("Invalid input")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It is a draw"

    if user_win(user, computer):
        return "You won!"
    
    return "You lost"

def user_win(user, computer):
    if (user == "p" and computer == "r") or (user == "r" and computer == "s") or (user == "s" and computer == "p"):
        return True
    
if __name__ == "__main__":
    main()




