import csv

FILE_NAME = "library.csv"

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author])

    print("Book added successfully!\n")

def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Book List ---")
            for row in reader:
                print("ID:", row[0], "Title:", row[1], "Author:", row[2])
    except FileNotFoundError:
        print("No file found!\n")

def search_book():
    book_id = input("Enter Book ID to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == book_id:
                    print("Book Found:", row)
                    found = True
                    break
        if not found:
            print("Book not found!\n")
    except FileNotFoundError:
        print("No file found!\n")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    rows = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != book_id:
                    rows.append(row)
                else:
                    found = True

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if found:
            print("Book deleted successfully!\n")
        else:
            print("Book not found!\n")
    except FileNotFoundError:
        print("No file found!\n")

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")