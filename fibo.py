def generate_fibonacci(num_terms):
    """
    Generates the Fibonacci sequence up to a specific number of terms.
    Returns the sequence as a list of numbers.
    """
    if num_terms == 1:
        return [0]
    
    sequence = [0, 1]
    
    # Start the loop from 2 since we already have the first two terms
    for _ in range(2, num_terms):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
        
    return sequence

def main():
    """
    Main function to get user input and print the sequence.
    """
    print("🌀 Fibonacci Sequence Generator 🌀")
    
    while True:
        try:
            terms = int(input("How many terms of the sequence do you want? "))
            if terms <= 0:
                print("Please enter a positive number of terms.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # --- Generate and print the sequence ---
    fib_sequence = generate_fibonacci(terms)
    
    print("\n--- Here is the sequence: ---")
    # Print as a comma-separated string
    print(", ".join(map(str, fib_sequence)))
    print("-----------------------------")

# --- Main execution block ---
if __name__ == "__main__":
    main()
