def book_club_points():
    books_purchased = int(input("Enter the number of books purchased this month: "))

    if books_purchased == 0:
        points = 0
    elif books_purchased == 1 or books_purchased == 2:
        points = 5
    elif books_purchased == 3 or books_purchased == 4:
        points = 15
    elif books_purchased == 5 or books_purchased == 6:
        points = 30
    elif books_purchased == 7 or books_purchased >= 8:
        points = 60

    print(f"Points awarded: {points}")

# Call the function to execute the program
book_club_points()