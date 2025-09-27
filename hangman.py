# A classic hangman game with fixed words to guess
# maybe try randomising words based on genre selected by the user in the future

import random

def play_hangman():
    """
    Main function to run the Hangman game.
    """
    # --- Setup ---
    word_list = ["python", "github", "programming", "developer", "terminal", "code", "software"]
    secret_word = random.choice(word_list).lower()
    guessed_letters = []
    lives = 6
    
    # ASCII art for the hangman stages
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]

    print("🎉 Welcome to Hangman! 🎉")

    # --- Game Loop ---
    while lives > 0:
        # Display the current state of the word (e.g., _ p p _ e)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"\nWord: {display_word}")
        print(f"You have {lives} lives left.")
        print(stages[lives-1]) # Display the hangman art

        # Check for win condition
        if "_" not in display_word:
            print(f"✨ Congratulations! You guessed the word: '{secret_word}'")
            break

        # Get user input
        guess = input("Guess a letter: ").lower()

        # --- Input Validation ---
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue
            
        # Add the guess to our list of guessed letters
        guessed_letters.append(guess)

        # --- Check the Guess ---
        if guess not in secret_word:
            lives -= 1
            print(f" Oops! The letter '{guess}' is not in the word.")
        else:
            print(f"Good guess! The letter '{guess}' is in the word.")
            
    # --- End of Game ---
    if lives == 0:
        print(stages[0])
        print("💀 Game Over! You ran out of lives.")
        print(f"The secret word was: '{secret_word}'")

# Start the game
if __name__ == "__main__":
    play_hangman()
