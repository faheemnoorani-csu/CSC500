def calculate_book_club_points():
    books_purchased = int(input("Enter the number of books purchased this month: "))

    if books_purchased >= 8:
        points = 60
    elif books_purchased >= 6:
        points = 30
    elif books_purchased >= 4:
        points = 15
    elif books_purchased >= 2:
        points = 5
    else:
        points = 0

    print(f"Points awarded: {points}")

if __name__ == "__main__":
    calculate_book_club_points()
