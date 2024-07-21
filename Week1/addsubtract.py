# Function defined to perform addition and subtraction
def add_subtract(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    return addition, subtraction

# Prompt user for input
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

# Perform the desired calculations
addition_result, subtraction_result = add_subtract(num1, num2)

# Output results from the calculations
print(f"Addition of {num1} and {num2}: {addition_result}")
print(f"Subtraction of {num1} from {num2}: {subtraction_result}")
