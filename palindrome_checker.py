import string

def is_palindrome(text):
    """
    Checks if a string is a palindrome, ignoring case,
    punctuation, and whitespace.
    """
    
    # 1. Remove all punctuation and spaces
    translator = str.maketrans('', '', string.punctuation + ' ')
    cleaned_text = text.translate(translator)
    
    # 2. Convert to lowercase
    cleaned_text = cleaned_text.lower()
    
    # 3. Check if the text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

def main():
    """
    Main function to get user input and print the result.
    """
    print("🔄 Palindrome Checker 🔄")
    
    user_input = input("Enter a word or phrase to check: ")

    if not user_input.strip():
        print("You didn't enter anything.")
        return

    if is_palindrome(user_input):
        print(f"\n✅ Yes, '{user_input}' is a palindrome!")
    else:
        print(f"\n❌ No, '{user_input}' is not a palindrome.")

# --- Main execution block ---
if __name__ == "__main__":
    main()
