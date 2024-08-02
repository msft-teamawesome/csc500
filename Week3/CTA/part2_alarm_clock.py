# Part 2: Alarm Clock

# Get the current time from the user
current_time = int(input("Enter the current time (0-23): "))

# Get the number of hours to wait for the alarm
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the future time
future_time = (current_time + wait_hours) % 24

# Display the future time
print(f"The time when the alarm goes off will be: {future_time}:00")