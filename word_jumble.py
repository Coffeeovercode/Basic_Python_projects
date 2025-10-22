import random

def play_word_jumble():
    """
    Main function to run the Word Jumble game.
    """
    word_list = ["python", "github", "developer", "terminal", "jumble", "random"]
    secret_word = random.choice(word_list)
    
    # --- Scramble the word ---
    jumbled_word = "".join(random.sample(secret_word, len(secret_word)))
    
    print("🧠 Word Jumble Game 🧠")
    print("\nI've jumbled a word for you. Can you guess what it is?")
    print(f"The jumbled word is: {jumbled_word}")
    
    guess_count = 0
    
    while True:
        guess = input("\nYour guess (or type 'quit' to exit): ").lower()
        guess_count += 1
        
        if guess == 'quit':
            print(f"The word was '{secret_word}'. Thanks for playing!")
            break
        elif guess == secret_word:
            print(f"\n✨ Correct! You guessed the word in {guess_count} attempts.")
            break
        else:
            print("❌ Nope, that's not it. Try again!")

    # --- Ask to play again ---
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        play_word_jumble()
    else:
        print("Goodbye!")

# --- Main execution block ---
if __name__ == "__main__":
    play_word_jumble()
