import datetime

def find_day_of_week():
    """
    Asks the user for a date (year, month, day) and
    prints the corresponding day of the week.
    """
    print("🗓️  Day of the Week Calculator 🗓️")
    print("Enter any date to find out what day it was.")

    try:
        # --- Get User Input ---
        year_str = input("Enter the year (e.g., 1990): ")
        month_str = input("Enter the month (1-12): ")
        day_str = input("Enter the day (1-31): ")
        
        # --- Convert to integers ---
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
        
        # --- Create the date object ---
        # This will automatically raise a ValueError for
        # invalid dates (e.g., February 30th).
        date_obj = datetime.date(year, month, day)
        
        # --- Find the day of the week ---
        # %A is the format code for the full weekday name
        day_of_week = date_obj.strftime("%A")
        
        # --- Display the Result ---
        # %B is the full month name, %d is the day
        formatted_date = date_obj.strftime("%B %d, %Y")
        
        print("\n" + "="*40)
        print(f"  📅 Date: {formatted_date}")
        print(f"  ✨ Day of the Week: {day_of_week}")
        print("="*40)

    except ValueError:
        print(f"\n❌ Error: Invalid input. '{year_str}-{month_str}-{day_str}' is not a real date.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    find_day_of_week()
