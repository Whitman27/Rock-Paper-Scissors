import random
OPTIONS = ("rock", "paper", "scissors")
computer = random.choice(OPTIONS)

def start():
    # Checking the user input
    while True:
        selection = input("Please enter rock, paper or scissors: ").lower()
        if selection in OPTIONS:
            pass
        else:
            print("Please enter a correct selection! ")
            break

    # Printing out the choices
        print(f"Player: {selection}")
        print(f"Computer: {computer}")

    # Checking for winner
        if selection == computer:
            print("It's a tie! Try Again!")
        elif selection == "rock" and computer == "scissors":
            print(f"{selection} beats {computer}, YOU WIN!")
        elif selection == "scissors" and computer == "paper":
            print(f"{selection} beats {computer}, YOU WIN!")
        elif selection == "paper" and computer == "rock":
            print(f"{selection} beats {computer}, YOU WIN!")
        else:
            print(f"{computer} beats {selection}, YOU LOSE!")

if __name__ == '__main__':
    start()
