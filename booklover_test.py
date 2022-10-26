import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def scaffold_booklover(self):
        """Scaffold a BookLover object with some books"""

        bl = BookLover('Katherine', 'kat@books.com', 'fiction')
        books = [("Jane Eyre", 4), ("Fight Club", 3), ("The Divine Comedy", 5), ("The Popol Vuh", 5)]

        for book_name, rating in books:
            bl.add_book(book_name, rating)
        return bl

    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        bl = self.scaffold_booklover()

        self.assertTrue(bl.has_read('Jane Eyre'))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl = self.scaffold_booklover()
        with self.assertRaises(IndexError):
            bl.add_book('Jane Eyre', 4)
        self.assertEqual(len(bl.book_list[bl.book_list.book_name == 'Jane Eyre']), 1)

    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        bl = self.scaffold_booklover()
        self.assertTrue(bl.has_read('Jane Eyre'))

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl = self.scaffold_booklover()
        self.assertFalse(bl.has_read('The Great Gatsby'))

    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        bl = self.scaffold_booklover()
        self.assertEqual(bl.num_books_read(), 4)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 

        bl = self.scaffold_booklover()
        fav_books = bl.fav_books()

        ## Test that the number of books in `fav_books` is correct.
        self.assertEqual(len(fav_books), 3)
        ## Test that all the books have a rating > 3 (i.e. there are no books with rating <= 3)
        self.assertEqual(len(fav_books[~ (fav_books.book_rating > 3)]), 0)


if __name__ == '__main__':
    unittest.main(verbosity=3)