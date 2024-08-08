# Python code
valid_input = False
while not valid_input:
    user_input = input("Enter a number between 1 and 10: ")
    if user_input.isdigit() and 1 <= int(user_input) <= 10:
        valid_input = True
        print("Valid input received")
    else:
        print("Invalid input, please try again")