# Get input from the user
num1 = float(input("Enter the dividend (first number): "))
num2 = float(input("Enter the divisor (second number): "))

# Check for division by zero to prevent a crash
if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    # Standard division (returns a float/decimal)
    standard_div = num1 / num2
    
    # Floor division (returns the whole number quotient)
    floor_div = num1 // num2
    
    # Modulo (returns the remainder)
    remainder = num1 % num2

    print(f"Standard Division ({num1} / {num2}): {standard_div}")
    print(f"Floor Division ({num1} // {num2}): {floor_div}")
    print(f"Remainder ({num1} % {num2}): {remainder}")
