def get_valid_number(prompt, allow_zero=True):
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            if not allow_zero and number == 0:
                print("Error: The divisor cannot be zero. Please try again.")
                continue
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

# Get validated inputs
num1 = get_valid_number("Enter the dividend (first number): ")
num2 = get_valid_number("Enter the divisor (second number): ", allow_zero=False)

# Perform calculations
standard_div = num1 / num2
floor_div = num1 // num2
remainder = num1 % num2

# Display results
print(f"\nStandard Division ({num1} / {num2}): {standard_div}")
print(f"Floor Division ({num1} // {num2}): {floor_div}")
print(f"Remainder ({num1} % {num2}): {remainder}")
