import random 
def get_user_choice():
    user_choice = input("Enter your choice(rock, paper or scissor): ").lower()
    while user_choice not in ["rock", "paper", "scissor"]:
        user_choice = input("Invalid choice, Please choose one from rock, paper, scissor: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", 'paper', 'scissor']
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!!!"
    elif(user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissor" and computer_choice == "paper"):
        return "You Win!!!"
    else:
        return "Computer Wins :("
    
def play_again():
    return input("Do You Want to Play Again (yes/no): ").lower() == "yes"

def main():
    print("Welcome to Rock Paper Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
        result = winner(user_choice, computer_choice)
        print(result)
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
