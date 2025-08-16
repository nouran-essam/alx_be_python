from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)          # calls __str__
    print(repr(my_book))    # calls __repr__
    del my_book             # calls __del__

if __name__ == "__main__":
    main()
