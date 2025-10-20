def calculate_bmi():
    """
    Calculates Body Mass Index (BMI) and provides a weight status category.
    """
    print("⚖️  BMI (Body Mass Index) Calculator ⚖️")

    try:
        # --- Get User Input in Metric Units ---
        weight_kg = float(input("Enter your weight in kilograms (kg): "))
        height_cm = float(input("Enter your height in centimeters (cm): "))

        if weight_kg <= 0 or height_cm <= 0:
            print("Weight and height must be positive numbers.")
            return

        # --- Calculate BMI ---
        # Formula: weight (kg) / (height (m))^2
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        # --- Determine the weight status category ---
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"
            
        # --- Display the Result ---
        print("\n" + "="*30)
        print(f"  Your BMI is: {bmi:.2f}")
        print(f"  Category: {category}")
        print("="*30)
        print("\nDisclaimer: This is a general calculation and not medical advice.")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers for weight and height.")
    except ZeroDivisionError:
        print("\nInvalid input. Height cannot be zero.")

# --- Main execution block ---
if __name__ == "__main__":
    calculate_bmi()
