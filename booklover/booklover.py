from numpy import isin
import pandas as pd
from pprint import pprint

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0,
        book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list.copy()

    def add_book(self, book_name, rating):
        if not isinstance(book_name, str):
            raise TypeError('book_name must be a string')
        
        if not isinstance(rating, int):
            raise TypeError('rating must be an integer')
        
        if not (rating >= 0 and rating <= 5):
            raise ValueError('rating must be between 0 and 5')

        if self.book_list.book_name.isin([book_name]).any():
            raise IndexError("Book already in list")

        new_book = pd.DataFrame({'book_name':[book_name], 'book_rating':[rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

    def has_read(self, book_name):
        return book_name in self.book_list.book_name.values

    def num_books_read(self):
        return len(self.book_list) + self.num_books

    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]


if __name__ == '__main__':
    bl = BookLover('Katherine', 'kat@books.com', 'fiction')

    books = [("Jane Eyre", 4),
             ("Fight Club", 3),
             ("The Divine Comedy", 5),
             ("The Popol Vuh", 5)]

    for book in books:
        bl.add_book(book[0], book[1])

    print(bl.has_read('The Great Gatsby'))