import json

class Books:
    
    def __init__(self, title, author, year, status, genre):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.genre = genre


    def display_info(self):
        print(f"\nTitle:{self.title}")
        print(f"Author:{self.author}")
        print(f"Year:{self.year}")
        print(f"Genre:{self.genre}")

    def mark_read(self):
            print(f"\n{self.title} already marked as read")

    def unmark_read(self):
            print(f"\n{self.title} already marked as unread")


class Library:
      def __init__(self, filename='practise/library.json'):
            self.books = []
            self.filename = filename



      def add_books(self, books):
            for b in self.books:
                  if b.title == books.title:
                        print(f"The book {books.title} already exists")
                        return
                  
            self.books.append(books)
            print(f"The book {books.title} has been added to the library")


      def list_books(self):
            if not self.books:
                  print(f"The Library is empty")
            else:
                  for b in self.books:
                        result = b.display_info()

                  return result
            
      

      def update_status(self, title, status):
            for b in self.books:
                  if b.title.lower() == title.lower():
                        if status.lower() == 'read':
                              b.mark_read()
                        elif status.lower() == 'unread':
                               b.unmark_read()
                        return 
                  
            
            print(f"The book {title} does not exist in the library")



      def remove_book(self, title):
            for b in self.books:
                  if b.title.lower() == b.title.lower():
                        self.books.remove(b)
                        print(f"The book {b.title} has been removed")
                        return
            print(f"The book '{title}' does not exist")       



      def save_library(self):
            data = []
            for b in self.books:
                  data.append({
                        'title': b.title,
                        'author':b.author,
                        'year':b.year,
                        'status':b.status,
                        'genre':b.genre

                  }) 

                  with open(self.filename, 'w') as f:
                        json.dump(data, f)
            print(f"Library saved to {self.filename} ")



      def load_library(self):
            try:
                  with open(self.filename, 'r') as f:
                       data = json.load(f)
                       for item in data:
                             books = Books(
                                   item['title'],
                                   item['author'],
                                   item['year'],
                                   item['status'],
                                   item['genre']
                             )
                  self.books.append(books)
                  print(f"The Library restored to {self.filename}")
            except FileNotFoundError:
                  print(f"The file {self.filename} does not exist")




my_book = Books("Python crash course", "Eric Matthes", 2019, "read", "Tech")
my_book1 = Books("Think and Grow Rich", "Napoleon", 2019, "read", "Self Growth")
my_library = Library()
my_library.add_books(my_book)
my_library.add_books(my_book1)
my_library.list_books()
my_library.update_status("Think and Grow Rich", "read")
print()
my_library.remove_book("python crash course")
my_library.remove_book("think and grow rich")
print()
my_library.save_library()
my_library.load_library()


                        
                        

            




      



                        
            
            
     





    