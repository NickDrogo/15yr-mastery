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
            self.status == "read"
            print(f"\n{self.title} already marked as read")

    def unmark_read(self):
            self.status == 'unread'
            print(f"\n{self.title} already marked as unread")








    