from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Mila")

    def test_init_attributes(self):
        self.assertEqual("Mila", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ""
        self.assertEqual('Name cannot be empty string!', str(ex.exception))

    def test_add_book_with_new_author(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Martin King", "No Time to die")
        self.assertEqual({"Martin King": ["No Time to die"]}, self.library.books_by_authors)

    def test_add_book_with_existing_author(self):
        self.library.books_by_authors = {"Martin King": ["No Time to die"]}
        self.assertIn("Martin King", self.library.books_by_authors)
        self.library.add_book("Martin King", "Today or Never")
        self.assertEqual({"Martin King": ["No Time to die", "Today or Never"]}, self.library.books_by_authors)

    def test_add_book_with_existing_author_and_title(self):
        self.library.books_by_authors = {"Martin King": ["No Time to die"]}
        self.assertIn("No Time to die", self.library.books_by_authors["Martin King"])
        self.library.add_book("Martin King", "No Time to die")
        self.assertEqual({"Martin King": ["No Time to die"]}, self.library.books_by_authors)

    def test_add_new_reader(self):
        self.assertEqual({}, self.library.readers)
        self.library.add_reader("Pesho")
        self.assertEqual({"Pesho": []}, self.library.readers)

    def test_add_existing_reader(self):
        self.library.readers = {"Pesho": []}
        self.assertIn("Pesho", self.library.readers)
        result = self.library.add_reader("Pesho")
        self.assertEqual("Pesho is already registered in the Mila library.", result)

    def test_rent_book_with_not_register_reader(self):
        self.library.books_by_authors = {"Martin King": ["No Time to die"]}

        self.library.readers = {"Pesho": []}
        self.assertIn("Pesho", self.library.readers)

        result = self.library.rent_book("Goran", "Martin King", "No Time to die")
        self.assertEqual("Goran is not registered in the Mila Library.", result)

    def test_rent_book_with_existing_reader_and_not_existing_author(self):
        self.library.books_by_authors = {"Martin King": ["No Time to die"]}
        self.library.readers = {"Pesho": []}
        result = self.library.rent_book("Pesho", "Victor Hugo", "Les Miserables")
        self.assertEqual("Mila Library does not have any Victor Hugo's books.", result)

    def test_rent_book_with_existing_reader_author_and_not_title(self):
        self.library.books_by_authors = {"Victor Hugo": ["Les Miserables"]}
        self.library.readers = {"Pesho": []}
        result = self.library.rent_book("Pesho", "Victor Hugo", "Notre Dame de Paris")
        self.assertEqual("""Mila Library does not have Victor Hugo's "Notre Dame de Paris".""", result)

    def test_rent_book(self):
        self.library.books_by_authors = {"Victor Hugo": ["Les Miserables"]}
        self.library.readers = {"Pesho": []}
        self.library.rent_book("Pesho", "Victor Hugo", "Les Miserables")
        self.assertEqual({"Pesho": [{"Victor Hugo": "Les Miserables"}]}, self.library.readers)
        self.assertEqual({"Victor Hugo": []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
