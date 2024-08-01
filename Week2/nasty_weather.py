def is_hot(temp):
    print(f"Checking if temperature {temp} is above 90°F")
    return temp > 90

def is_humid(humidity):
    print(f"Checking if humidity {humidity}% is above 75%")
    return humidity > 75

def is_extremely_hot(temp):
    print(f"Checking if temperature {temp} is above 100°F")
    return temp > 100

def is_extremely_humid(humidity):
    print(f"Checking if humidity {humidity}% is above 90%")
    return humidity > 90

temperature = 50
humidity = 90

# Compound conditional expression with short-circuiting
if (is_hot(temperature) and is_humid(humidity)) or (is_extremely_hot(temperature) or is_extremely_humid(humidity)):
    if is_hot(temperature) and is_humid(humidity):
        print("It is nasty outside today.")
    else:
        print("It is likely to be nasty today.")
else:
    print("It is likely not too nasty outside today.")