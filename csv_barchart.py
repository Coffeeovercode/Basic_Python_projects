import csv
import matplotlib.pyplot as plt

def generate_bar_chart():
    """
    Reads a 2-column CSV and generates a bar chart image.
    """
    print("📊 Simple CSV Bar Chart Generator 📊")
    
    file_path = input("Enter the path to your CSV file: ")

    labels = []
    values = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader) # Skip the header row
            
            x_label = header[0]
            y_label = header[1]
            
            for row in reader:
                labels.append(row[0])
                values.append(int(row[1])) # Convert value to integer

        # --- Create the Bar Chart ---
        plt.figure(figsize=(10, 6)) # Set the figure size
        plt.bar(labels, values, color='skyblue')
        
        # --- Add Labels and Title ---
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(f'{y_label} by {x_label}')
        plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better fit
        plt.tight_layout() # Adjust layout to prevent labels overlapping

        # --- Save and Show the Chart ---
        output_filename = 'barchart.png'
        plt.savefig(output_filename)
        print(f"\n✅ Success! Chart saved as '{output_filename}'")
        
        plt.show()

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    generate_bar_chart()
