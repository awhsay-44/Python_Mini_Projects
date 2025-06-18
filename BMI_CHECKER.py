def get_bmi(weight_kg, height_m):
    """Calculate BMI using weight and height."""
    bmi_value = weight_kg / (height_m ** 2)
    return round(bmi_value, 2)

def interpret_bmi(bmi):
    """Return a description of the BMI category."""
    if bmi < 16:
        return "Severely Underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Healthy Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obese (Class I)"
    elif 35 <= bmi < 39.9:
        return "Obese (Class II)"
    else:
        return "Extremely Obese (Class III)"

def run_bmi_check():
    print("🧮 Welcome to Yashwanthi's BMI Calculator 💖")
    try:
        weight = float(input("👉 Enter your weight (kg): "))
        height = float(input("👉 Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("⚠️ Please enter values greater than zero.")
            return

        bmi = get_bmi(weight, height)
        result = interpret_bmi(bmi)

        print("\n🎉 Calculation Complete!")
        print(f"📌 Your BMI is: {bmi}")
        print(f"📋 Category: {result}")

    except ValueError:
        print("❌ Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    run_bmi_check()
