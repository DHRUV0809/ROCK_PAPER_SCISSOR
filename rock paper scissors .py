import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")
    
    return winner

def rock_paper_scissors():
    user_score = 0
    computer_score = 0
    rounds_played = 0
    
    while True:
        rounds_played += 1
        print(f"\n--- Round {rounds_played} ---")
        
        winner = play_round()
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    rock_paper_scissors()
