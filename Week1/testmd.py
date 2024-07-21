# Function defined to perform multiplication and division
def multiply_divide(num1, num2):
    multiplication = num1 * num2
    division = num1 / num2
    return multiplication, division

# Prompt user for input
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

# Perform the desired calculations
multiplication_result, division_result = multiply_divide(num1, num2)

# Output results from the calculations
print(f"Multiplication of {num1} and {num2}: {multiplication_result}")
print(f"Division of {num1} by {num2}: {division_result}")
