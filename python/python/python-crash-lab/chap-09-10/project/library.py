from books import Books
import json

class Library:
    def __init__(self, filename='project/library.json'):
        self.books = []
        self.filename = filename


    def add_book(self, book):
        for b in self.books:
            if b.title == book.title:
                print(f"The book {book.title} already exists in the library")
                return

            
        self.books.append(book)
        print(f"The Book {book.title} has been added to the libray")
        

    
    def list_books(self):
        if not self.books:
            print(f"The library is empty.")
        
        else:
            print("\nBooks in the library:")
            for b in self.books:
                result = f"{b.display_info()}"
            
            return result
    
    def update_status(self, title, status):
        for b in self.books:

            if b.title.lower() == title.lower():
                if status.lower() == 'read':
                    b.mark_read()
                elif status.lower() == 'unread':
                    b.unmark_read()
                return
            
        print(f"The book '{title}' not found in the library")


        
    def remove_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                self.books.remove(b)
                print(f"The book '{title}' has been removed from the library.")
            return
            
        print(f"Book '{title}' is not found in the library")


            
    def save_library(self):
        data = []
        for b in self.books:
            data.append({
                "title":b.title,
                "author":b.author,
                "year":b.year,
                "status":b.status,
                "genre":b.genre

            })

            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        print(f"Library saved to {self.filename}")





    def load_library(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for item in data:
                    book = Books(
                        item["title"],
                        item["author"],
                        item["year"],
                        item["status"],
                        item["genre"]
                    )
    
              
            self.books.append(book)
            print(f"Library loaded from '{self.filename}' ")
        except FileNotFoundError:
            print(f"No saved library found at '{self.filename}, starting fresh.'") 


my_book = Books("Python crash course", "Eric Matthes", 2019, "read", "Tech")
my_book1 = Books("Think and Grow Rich", "Napoleon", 2019, "read", "Self Growth")
my_library = Library()
my_library.add_book(my_book)
my_library.add_book(my_book1)
my_library.list_books()
my_library.update_status("Think and Grow Rich", "unread")
my_library.remove_book("python crash course")
my_library.remove_book("think and grow rich")
my_library.save_library()
my_library.load_library()
