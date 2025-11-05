import datetime

def get_date_from_user(prompt):
    """
    Gets valid date input (Y, M, D) from the user and returns a date object.
    """
    print(prompt)
    while True:
        try:
            year = int(input("  Enter the year (YYYY): "))
            month = int(input("  Enter the month (1-12): "))
            day = int(input("  Enter the day (1-31): "))
            
            # This will raise a ValueError for invalid dates (e.g., Feb 30)
            date_obj = datetime.date(year, month, day)
            return date_obj
        except ValueError:
            print("❌ Error: That is not a valid date. Please try again.")

def main():
    """
    Main function to calculate the difference between two dates.
    """
    print("📅 Date Difference Calculator 📅")
    print("Enter two dates to find the number of days between them.")
    
    # --- Get the two dates ---
    date1 = get_date_from_user("\n--- Enter the Start Date ---")
    date2 = get_date_from_user("\n--- Enter the End Date ---")
    
    # --- Calculate the difference ---
    # The result is a 'timedelta' object.
    # We ensure the difference is always positive.
    if date2 > date1:
        time_delta = date2 - date1
    else:
        time_delta = date1 - date2
        
    # Extract the number of days from the timedelta
    num_days = time_delta.days
    
    # --- Display the Result ---
    print("\n" + "="*40)
    print("           Calculation Result")
    print("="*40)
    print(f"  From: {date1.strftime('%B %d, %Y')}")
    print(f"  To:   {date2.strftime('%B %d, %Y')}")
    print(f"\n  ✨ Total Days Between: {num_days} days")
    print("="*40)

# --- Main execution block ---
if __name__ == "__main__":
    main()
