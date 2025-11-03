import random

def play_game():
    """
    Main function to run the Rock, Paper, Scissors game.
    """
    
    player_score = 0
    computer_score = 0
    WINNING_SCORE = 5  # <-- ADDED
    
    print("🪨📄✂️ Welcome to Rock, Paper, Scissors! 🪨📄✂️")
    print(f"First to {WINNING_SCORE} points wins!")  # <-- ADDED
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' or 'exit' to end the game.")

    while True:
        # --- Get User Input ---
        user_choice = input("\nYour move: ").lower()

        if user_choice in ['quit', 'exit']:
            break # <-- MODIFIED

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
            continue

        # --- Get Computer's Choice ---
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")

        # --- Determine the Winner ---
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("🎉 You win this round!")
            player_score += 1
        else:
            print("🤖 The computer wins this round!")
            computer_score += 1
            
        # --- Display Current Score ---
        print(f"Score -> You: {player_score} | Computer: {computer_score}")

        # --- Check for Game Winner ---  <-- ADDED BLOCK
        if player_score == WINNING_SCORE:
            print("\n🎉 You are the grand winner! 🎉")
            break
        elif computer_score == WINNING_SCORE:
            print("\n🤖 The computer is the grand winner! 🤖")
            break

    # --- This code runs AFTER the loop breaks (for any reason) --- <-- ADDED
    print("\n--- Final Score ---")
    print(f"You: {player_score}  |  Computer: {computer_score}")
    print("Thanks for playing! Goodbye.")

# --- Main execution block ---
if __name__ == "__main__":
    play_game()

