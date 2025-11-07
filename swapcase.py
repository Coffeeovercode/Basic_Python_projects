def main():
    """
    Takes a string from the user and swaps the case of all letters.
    """
    print("🔁 Swap Case Tool 🔁")
    print("Enter a string to swap its case (e.g., 'Hello' -> 'hELLO').")
    
    original_string = input("\nEnter your string: ")
    
    swapped_list = []
    # I am implementing the logic using ASCII value manipulation but there are a myriad different ways of doing this
    for char in original_string:
        if 'a' <= char <= 'z':
            swapped_list.append(chr(ord(char) - 32))
        elif 'A' <= char <= 'Z':
            swapped_list.append(chr(ord(char) + 32))
        else:
            swapped_list.append(char)
    swapped_string = "".join(swapped_list)
    
    print("\n" + "="*40)
    print(f"  Original:  {original_string}")
    print(f"  Swapped:   {swapped_string}")
    print("="*40)

if __name__ == "__main__":
    main()
