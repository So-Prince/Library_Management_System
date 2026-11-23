import json
import datetime

FILE_NAME = "lms.json"
class Lms:
    def __init__(self):
        try:
            # data = []

            with open(FILE_NAME, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("This file doesn't exit")
            a = []

        self.data = data

    def save_file(self):
        with open(FILE_NAME, 'w') as file:
            json.dump(self.data, file, indent=3)
    
    def add_books(self):

        field = input("What field/course is the book? ").strip().capitalize()
        book_name = input("What is the name of the book? ").strip().capitalize()
        author = input("Who is/are the author(s)? ").strip().title()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        detail = {
                'Field': field,
                'Book_name': book_name,
                'Author(s)': author,
                'Borrowed': False,
                'DateAdded': date
            }
        self.data.append(detail)
        self.save_file()
        print("Book added successfully.\n")
        
    def remove_books(self):
        if not self.data:
            print("There's nothing to delete.")
            return
        
        for i, books in enumerate(self.data, start=1):
            print(f"{i}. {books}")
        # while True:
        try: 
                delete = int(input("What are you deleting? "))
                if delete < 1 or delete > len(self.data):
                    print("Index out of range. Try again!")
                    return

                # if delete:
                self.data.pop(delete - 1)
                # self.save_file()
                print("Book removed successfully.\n")
        except ValueError:
                print("Invalid datatype. Use integers.")

    def search_books(self):
        if not self.data:
            print("There's nothing to search.")
            return
        
        for i, books in enumerate(self.data, start=1):
            print(f"{i}. {books}")

        search = input("What are you searching for? Type 'field', 'book_name' or 'author(s)' ").strip().capitalize()
        if search == 'Field':
            print(f"Search by field:")
            for item in self.data:
                print(f"{item['Field']}")
        elif search == 'Book_name':
            print(f"Search by book name:")
            for item in self.data:
                print(f"{item['Book_name']}")
        elif search == 'Author(s)':
            print(f"Search by author:")
            for item in self.data:
                print(f"{item['Author(s)']}")
        else:
            print("You didn't search with the key words.")
        print()

    def borrow_books(self):
        if not self.data:
            print("Nothing to borrow.")
            return

        for i, books in enumerate(self.data, start=1):
            print(f"{i}. {books}")

        borrow = int(input("Which book are you borrowing? "))
        picked = self.data[borrow - 1]
        if borrow:
            picked['Borrowed'] = True
            self.save_file()
            print("Book has been borrowed successfully.\n")
        else:
            picked['Borrowed'] = False

    def return_books(self):
        if not self.data:
            print("Nothing to return here.")
            return

        for i, books in enumerate(self.data, start=1):
            print(f"{i}. {books}")

        returned = int(input("Which book are you returning? "))
        returned_bk = self.data[returned - 1]
        if returned and returned_bk['Borrowed'] == True:
            returned_bk['Borrowed'] = False
            self.save_file()
            print(f"{returned_bk['Book_name']} book has been returned\n")
        else:
            print("Not returned.")

    def view_available_book(self):
        if not self.data:
            print("Nothing available to view")
            return

        for i, books in enumerate(self.data, start=1):
            if books['Borrowed'] == False:
                print(f"{i}. {books['Book_name']} is available.")
                print()
            elif books['Borrowed'] == True:
                print(f"{i}. {books['Book_name']} is not available.")
                print()
            else:
                print('This data does not exit.\n')

    def view_borrowed_books(self):
        if not self.data:
            print("Empty file. Nothing to view.\n")
            return
        for books in self.data:
            if books['Borrowed'] == True:
                print(books)
                print()

user = Lms()

print("-"*50)
print("WELCOME TO OUR LIBRARY MANAGEMENT SYSTEM".center(50))
print("-"*50)
print()

while True:
    print("Pick a number to perform such activity.")
    print('''
    1. Add a book
    2. Remove a book
    3. Search for book
    4. Borrow a book
    5. Return a book
    6. View available books
    7. View borrowed books
    8. Exit program
    ''')

    try:
        activity = int(input("What will you like to do? "))

        # action = action.get(activity)
        if activity == 1:
            user.add_books()
        elif activity == 2:
            user.remove_books()
        elif activity == 3:
            user.search_books()
        elif activity == 4:
            user.borrow_books()
        elif activity == 5:
            user.return_books()
        elif activity == 6:
            user.view_available_book()
        elif activity == 7:
            user.view_borrowed_books()
        elif activity == 8:
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("You need to pick int 1 - 8.\n")
    except ValueError:
        print("Wrong input\n")

        
