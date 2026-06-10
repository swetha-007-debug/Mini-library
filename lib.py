import json

FILE_NAME = "books.json"


class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "issued": False
        }

        self.books.append(book)
        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nLibrary Books")
        print("-" * 50)

        for book in self.books:
            status = "Issued" if book["issued"] else "Available"
            print(
                f"ID: {book['id']} | "
                f"Title: {book['title']} | "
                f"Author: {book['author']} | "
                f"Status: {status}"
            )

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book["id"] == book_id:
                if book["issued"]:
                    print("Book already issued.")
                else:
                    book["issued"] = True
                    self.save_books()
                    print("Book issued successfully.")
                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book["id"] == book_id:
                if not book["issued"]:
                    print("Book is already available.")
                else:
                    book["issued"] = False
                    self.save_books()
                    print("Book returned successfully.")
                return

        print("Book not found.")


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.issue_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()