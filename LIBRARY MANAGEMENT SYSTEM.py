print("LIBRARY MANAGEMENT SYSTEM")

books = [
    "Introduction to E-Governance",
    "Internet of Things",
    "Information Security",
    "Multimedia Technology",
    "Advanced Computer Networks",
    "Data Science",
    "Data Warehouse and Data Mining"
]

issued = []

while True:

    print("\n1. Book Issue")
    print("2. Book Return")
    print("3. Pay Late Fee")
    print("4. Show Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Book Issue
    if choice == 1:

        print("\nAvailable Books:")

        for i in range(len(books)):
            print(i + 1, books[i])

        book = int(input("Enter book number: "))

        if book >= 1 and book <= len(books):
            name = books.pop(book - 1)
            issued.append(name)

            print("Book Issued Successfully")
            print("Remaining Books:", len(books))
        else:
            print("Invalid Book Number")

    # Book Return
    elif choice == 2:

        if len(issued) == 0:
            print("No Book is Issued")

        else:
            print("\nIssued Books:")

            for i in range(len(issued)):
                print(i + 1, issued[i])

            book = int(input("Enter book number: "))

            if book >= 1 and book <= len(issued):
                name = issued.pop(book - 1)
                books.append(name)

                print("Book Returned Successfully")
                print("Available Books:", len(books))
            else:
                print("Invalid Book Number")

    # Late Fee
    elif choice == 3:

        fee = int(input("Enter Late Fee: "))
        print("Late Fee Paid:", fee)

    # Show Books
    elif choice == 4:

        print("\nAvailable Books:")

        for i in range(len(books)):
            print(i + 1, books[i])

        print("Total Books:", len(books))

    # Exit
    elif choice == 5:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")
