def average_batting_average():
    years = int(input("Enter the number of years: "))
    total_months = years * 12
    total_batting_average = 0.0

    for year in range(1, years + 1):
        print(f"Year {year}:")
        for month in range(1, 13):
            batting_average = float(input(f"Enter the batting average for month {month}: "))
            total_batting_average += batting_average

    average_batting_average = total_batting_average / total_months
    print(f"\nTotal number of months: {total_months}")
    print(f"Total batting average: {total_batting_average}")
    print(f"Average batting average per month: {average_batting_average:.3f}")

# Call the function to execute the program
average_batting_average()