import pyfiglet
import random

def generate_ascii_art():
    """
    Generates and displays ASCII art from user input using a random font.
    """
    print("🎨 ASCII Art Generator 🎨")
    
    # --- Get User Input ---
    user_text = input("Enter the text you want to convert: ")

    if not user_text:
        print("No text entered. Exiting.")
        return

    # --- Get a list of available fonts and choose one randomly ---
    try:
        available_fonts = pyfiglet.FigletFont.getFonts()
        random_font = random.choice(available_fonts)
        
        print(f"\n(Using random font: '{random_font}')\n")

        # --- Generate and Print the ASCII Art ---
        ascii_art = pyfiglet.figlet_format(user_text, font=random_font)
        print(ascii_art)
        
    except pyfiglet.FontNotFound:
        # Fallback in the rare case the chosen font is somehow invalid
        print("Could not generate art with the chosen font. Using default.")
        ascii_art = pyfiglet.figlet_format(user_text)
        print(ascii_art)


# --- Main execution block ---
if __name__ == "__main__":
    generate_ascii_art()
