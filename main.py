import random

def print_rules():
    print()
  
    print('''Welcome to Rock-Paper-Scissors! Here are the rules:

1. The game will be played over 3 rounds.
2. Rock breaks scissors (R > S).
3. Scissors cut paper (S > P).
4. Paper covers rock (P > R).
5. If both players choose the same option in a round, it's a tie.
6. The winner is determined based on the number of wins.
7. If one player wins 2 rounds and the other player does not have 2 wins, that player is declared the winner.
8. If neither player wins 2 rounds and there is a tie, the game is declared a tie.''')

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def generate_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "User"
    else:
        return "Computer"

def game():
    print_rules()

    user_score = 0
    computer_score = 0

    for _ in range(3):
        user_choice = get_user_choice()
        computer_choice = generate_computer_choice()

        print("\nUser choice:", user_choice)
        print("Computer choice:", computer_choice)

        winner = compare_choices(user_choice, computer_choice)

        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1

        print("\nScore: User -", user_score, ", Computer -", computer_score)

        # Check if a player has reached a score of 2 or more
        if user_score >= 2:
            print("\nWinner is: User")
            break
        elif computer_score >= 2:
            print("\nWinner is: Computer")
            break

    else:  # This block is executed if the loop completes all iterations (i.e., no one has reached a score of 2 or more)
        if user_score > computer_score:
            print("\nWinner is: User")
        elif computer_score > user_score:
            print("\nWinner is: Computer")
        else:
            print("\nIt's a tie!")

if __name__ == "__main__":
    game()

