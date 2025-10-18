def is_leap(year):
    """
    Determines if a given year is a leap year based on the
    Gregorian calendar rules.
    
    A year is a leap year if:
    1. It is divisible by 4
    2. AND it is NOT divisible by 100
    3. UNLESS it IS also divisible by 400
    """
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def main():
    """
    Main function to get user input and print the result.
    """
    print("🗓️  Leap Year Checker 🗓️")
    
    try:
        # Get user input and convert to an integer
        year_input = input("Enter a year (e.g., 2024): ")
        year = int(year_input)
        
        # A year must be a positive number
        if year <= 0:
            print("Please enter a positive year.")
            return

        # --- Check the year and print the result ---
        if is_leap(year):
            print(f"\n✅ Yes, {year} is a leap year.")
        else:
            print(f"\n❌ No, {year}
