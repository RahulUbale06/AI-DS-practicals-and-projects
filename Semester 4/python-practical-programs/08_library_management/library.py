# 8. Write a Python program to manage library books using
# dictionaries with options to add, search, and remove books.

# Library Management System using Dictionary and While Loop

library_books = {}

print("*" * 40)
print("      LIBRARY MANAGEMENT SYSTEM")
print("*" * 40)

# Initial book entries
num_of_books = int(input("\nEnter number of books: "))

for i in range(num_of_books):

    print("\n" + "*" * 20)
    print(f"Enter details for Book {i+1}")
    print("*" * 20)

    name = input("Enter book name: ")
    author = input("Enter book author: ")

    library_books[name] = author

# Menu-driven loop
while True:

    print("\n" + "=" * 40)
    print("1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display Library")
    print("5. Exit")
    print("=" * 40)

    operation = input("\nEnter operation number: ")

    # Add Book
    if operation == "1":

        name = input("\nEnter book name: ")
        author = input("Enter book author: ")

        library_books[name] = author

        print("\nBook added successfully.")

    # Search Book
    elif operation == "2":

        name = input("\nEnter book name to search: ")

        if name in library_books:

            print("\nBook Found")
            print(f"Book Name : {name}")
            print(f"Author : {library_books[name]}")

        else:
            print("\nBook not found.")

    # Remove Book
    elif operation == "3":

        name = input("\nEnter book name to remove: ")

        if name in library_books:

            del library_books[name]

            print(f"\n{name} removed successfully.")

        else:
            print("\nBook not found.")

    # Display Library
    elif operation == "4":

        if len(library_books) == 0:

            print("\nLibrary is empty.")

        else:

            print("\n" + "*" * 40)
            print("         LIBRARY BOOKS")
            print("*" * 40)

            for name, author in library_books.items():

                print(f"\nBook Name : {name}")
                print(f"Author : {author}")

    # Exit
    elif operation == "5":

        print("\nThank you for visiting library.")
        break

    # Invalid Input
    else:
        print("\nInvalid operation. Please try again.")