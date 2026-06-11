class Book:
    total_books = 0
# Task1: Initialize instance attributes
    def __init__(self, title: str, author: str, genre: str):
        self.title= title
        self.author = author
        self.genre = genre
        self.availabe = True
        # Increment total_books each time a book object is created
        Book.total_books += 1
        

    @classmethod
    def from_dict(cls, data: dict):
        #Task 2: Create a book instance from a dictionary
        return cls(
            title = data["title"],
            author = data["author"],
            genre = data["genre"]
        )
    
    @classmethod
    def get_total(cls):
        #Reruen the total count in the specified format
        return f"Total books registered: {cls.total_books}"
    
    def borrow(self):
        if not self.availabe:
            #Borrow book and raise ValueError if already borrowed
            raise ValueError(f"{self.title} is already borrowed.")
        self.availabe = False

    def return_book(self):
        #Retun book and raise ValueError if not borrowed
        if self.availabe:
            raise ValueError(F"{self.title} was not currently borrowed.")
        self.available = True

    def __str__(self):
        #Define string represenation with ✅/❌ indicaor
        status = "✅" if self.availabe else "❌"
        return f"[{status}] {self.title} | {self.author} | {self.genre}"

#Interactive user input demonstration

if __name__ == "__main__":
    catalog = {}

    print("--- Welcome to the Library Book Catalogue System ---")
    
    # 1. Taking User Input to Create Books
    try:
        num_books = int(input("How many books would you like to add to the catalog? "))
    except ValueError:
        print("Invalid number. Defaulting to 2 books.")
        num_books = 2

    for i in range(num_books):
        print(f"\n--- Registering Book #{i+1} ---")
        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        genre = input("Enter Genre: ").strip()
        
        # Alternating between standard creation and from_dict creation to test both
        if i % 2 == 0:
            new_book = Book(title, author, genre)
            print(f"-> Created '{title}' using standard constructor.")
        else:
            book_data = {"title": title, "author": author, "genre": genre}
            new_book = Book.from_dict(book_data)
            print(f"-> Created '{title}' using from_dict @classmethod.")
            
        # Store in a dictionary using title as the key for easy retrieval later
        catalog[title.lower()] = new_book

    # 2. Display current status & Total
    print("\n" + "="*40)
    print("CURRENT CATALOGUE:")
    for book in catalog.values():
        print(book)
    print(Book.get_total())
    print("="*40)

    # 3. Interactive Loop for Borrowing and Returning
    while True:
        print("\nWhat would you like to do?")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View catalog")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            breakgit 

        if choice in ("1", "2"):
            target_title = input("Enter the exact book title: ").strip().lower()
            
            if target_title not in catalog:
                print("❌ Error: That book does not exist in this library.")
                continue
                
            book = catalog[target_title]

            try:
                if choice == "1":
                    book.borrow()
                    print(f"🎉 Success: You have successfully borrowed '{book.title}'.")
                elif choice == "2":
                    book.return_book()
                    print(f"🎉 Success: Thank you for returning '{book.title}'.")
            except ValueError as e:
                print(f"❌ Custom ValueError caught: {e}")

        elif choice == "3":
            print("\n" + "="*40)
            for book in catalog.values():
                print(book)
            print(Book.get_total())
            print("="*40)
        else:
            print("Invalid selection. Please choose options 1 through 4.")