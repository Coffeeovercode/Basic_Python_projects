import random
import re

def play_mad_libs():
    """Main function to run the Mad Libs game."""

    # --- Story Templates with placeholders in {curly_braces} ---
    story1 = ("Today, I went to the zoo. I saw a(n) {adjective} monkey swinging on a "
              "{noun}. It was so {adjective_2} that I almost dropped my {food_item}. "
              "Later, I saw a giant panda {verb_ending_in_ing} on a bamboo stick. "
              "I wish I could {verb} like that all day!")

    story2 = ("The best way to cook a(n) {noun} is to first {verb} it gently. "
              "Then, you should mix it with a(n) {adjective} sauce and three "
              "{plural_noun}. After {number} minutes in the oven, you will have "
              "the most {adjective_2} meal of your life.")

    templates = [story1, story2]
    story = random.choice(templates)

    # --- Find all placeholders in the chosen story ---
    placeholders = set(re.findall(r'{(.*?)}', story))
    user_words = {}
    
    print("🤪 Welcome to Mad Libs! 🤪")
    print("Please provide the following words:")

    # --- Get words from the user ---
    for p in sorted(list(placeholders)):
        # Format the prompt to be more user-friendly
        prompt = p.replace("_", " ").capitalize()
        user_words[p] = input(f"Enter a {prompt}: ")

    # --- Fill in the blanks and print the final story ---
    final_story = story.format(**user_words)
    
    print("\n" + "="*40)
    print("          Your Mad Libs Story!")
    print("="*40)
    print(final_story)
    print("="*40 + "\n")
    
    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
        play_mad_libs()
    else:
        print("Thanks for playing!")

# --- Main execution block ---
if __name__ == "__main__":
    play_mad_libs()
