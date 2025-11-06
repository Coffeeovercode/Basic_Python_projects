import string

def print_rangoli(size):
    """Prints an Alphabet Rangoli of a given size."""
    
    alphabet = string.ascii_lowercase
    letters = alphabet[:size]
    
    # Formula for the total width of the rangoli
    total_width = 4 * size - 3
    
    lines = []

    # This loop builds the lines from the center-most line *out*
    # (e.g., 'c-b-a-b-c', then 'c-b-c', then 'c')
    for i in range(size):
        # Get the letters for the current line
        # i=0 -> 'abc', i=1 -> 'ab', i=2 -> 'a' (for size 3)
        line_letters = letters[0 : size-i] 
        
        # Create the left half (e.g., 'c-b-a')
        left_half = '-'.join(line_letters[::-1])
        # Create the right half (e.g., 'b-c')
        right_half = '-'.join(line_letters[1:])
        
        line_content = left_half
        if right_half: # Add the right half if it exists
            line_content += '-' + right_half
        
        # Center the content and add it to our list
        lines.append(line_content.center(total_width, '-'))

    # --- Print the final rangoli ---
    
    # Print the top half (the list in reverse order)
    for line in reversed(lines):
        print(line)
        
    # Print the bottom half (skipping the center line, which is at index 0)
    for line in lines[1:]:
        print(line)

# --- Main execution block ---
if __name__ == "__main__":
    while True:
        try:
            size = int(input("Enter the rangoli size (an integer 1-26): "))
            if 1 <= size <= 26:
                print_rangoli(size)
                break
            else:
                print("Invalid size. Please enter a number between 1 and 26.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

