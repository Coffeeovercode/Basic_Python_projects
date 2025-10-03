import csv
import os

def analyze_csv():
    """
    Reads a CSV file and calculates basic statistics for a user-selected column.
    """
    print("📊 Basic CSV Data Analyzer 📊")
    
    # --- Get User Input ---
    file_path = input("Enter the path to your CSV file: ")

    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' was not found.")
        return

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            
            # --- Column Selection ---
            print("\nAvailable columns:")
            for i, col_name in enumerate(header):
                print(f"  {i}: {col_name}")
            
            while True:
                try:
                    col_index = int(input("\nEnter the index of the numeric column to analyze: "))
                    if 0 <= col_index < len(header):
                        break
                    else:
                        print("Invalid index. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")

            # --- Data Processing ---
            numbers = []
            for row in reader:
                try:
                    # Add the number from the selected column to our list
                    value = float(row[col_index])
                    numbers.append(value)
                except (ValueError, IndexError):
                    # Skip rows where the column is not a valid number or is missing
                    continue
            
            if not numbers:
                print("No valid numeric data found in the selected column.")
                return

            # --- Calculate Statistics ---
            total = sum(numbers)
            count = len(numbers)
            average = total / count
            maximum = max(numbers)
            minimum = min(numbers)

            # --- Display Results ---
            print("\n" + "="*30)
            print(f"  Analysis for column: '{header[col_index]}'")
            print("="*30)
            print(f"  Total Count: {count}")
            print(f"  Sum:         {total:,.2f}")
            print(f"  Average:     {average:,.2f}")
            print(f"  Maximum:     {maximum:,.2f}")
            print(f"  Minimum:     {minimum:,.2f}")
            print("="*30 + "\n")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    analyze_csv()
