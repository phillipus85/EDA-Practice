# import python modules
import csv
import sys
import os

# import the modules for data structures
from Src.DataStructs.List.arraylist import Arraylist

# assert the data structures modules
assert Arraylist

# global variables
# data folder
DATA_FLR = "Data"
GOOD_READ_FLR = "Goodreads"


class Catalog:
    def __init__(self):
        self.books = Arraylist()
        self.tags = Arraylist()
        self.book_tags = Arraylist()

    def load_books(self, booksfile) -> None:
        # get the file path for the books
        # fp = os.path.dirname(__file__)
        # print(fp)
        book_fp = os.path.join(DATA_FLR, GOOD_READ_FLR, booksfile)
        with open(book_fp, "r", encoding="utf-8") as book_file:
            reader = csv.DictReader(book_file)
            for row in reader:
                # print(row)
                self.books.add_last(row)
        print("Books loaded successfully")
        print("Total books loaded: ", self.books.size())

    def load_tags(self, tagsfile) -> None:
        # get the file path for the tags
        fp = os.path.dirname(__file__)
        tag_fp = os.path.join(fp, DATA_FLR, GOOD_READ_FLR, tagsfile)
        with open(tag_fp, "r", encoding="utf-8") as tag_file:
            reader = csv.DictReader(tag_file)
            for row in reader:
                # print(row)
                self.tags.add_last(row)
        print("Tags loaded successfully")
        print("Total tags loaded: ", self.tags.size())

    def load_book_tags(self, booktagsfile) -> None:
        # get the file path for the book tags
        fp = os.path.dirname(__file__)
        book_tag_fp = os.path.join(fp, DATA_FLR, GOOD_READ_FLR, booktagsfile)
        with open(book_tag_fp, "r", encoding="utf-8") as book_tag_file:
            reader = csv.DictReader(book_tag_file)
            for row in reader:
                # print(row)
                self.book_tags.add_last(row)
        print("Book tags loaded successfully")
        print("Total book tags loaded: ", self.book_tags.size())


# define the new catalog
def new_catalog():
    catalog = {
        "books": Arraylist(),
        "tags": Arraylist(),
        "book_tags": Arraylist(),
    }
    return catalog


# load books in catalog
def load_books(catalog, booksfile):
    # get the book data structure
    book_lt = catalog.get("books")  # equivalent to catalog["books"]
    # get the file path for the books
    fp = os.path.dirname(__file__)
    print(fp)
    book_fp = os.path.join(fp, DATA_FLR, GOOD_READ_FLR, booksfile)
    with open(book_fp, "r", encoding="utf-8") as book_file:
        reader = csv.DictReader(book_file)
        for row in reader:
            # print(row)
            book_lt.add_last(row)
    print("Books loaded successfully")
    print("Total books loaded: ", book_lt.size())
    return catalog


def load_tags(catalog, tagsfile):
    # get the tags data structure
    tag_lt = catalog.get("tags")  # equivalent to catalog["tags"]
    # get the file path for the tags
    fp = os.path.dirname(__file__)
    tag_fp = os.path.join(fp, DATA_FLR, GOOD_READ_FLR, tagsfile)
    with open(tag_fp, "r", encoding="utf-8") as tag_file:
        reader = csv.DictReader(tag_file)
        for row in reader:
            # print(row)
            tag_lt.add_last(row)
    print("Tags loaded successfully")
    print("Total tags loaded: ", tag_lt.size())
    return catalog


def load_book_tags(catalog, booktagsfile):
    # get the book tags data structure
    book_tag_lt = catalog.get("book_tags")  # equivalent to catalog["book_tags"]
    # get the file path for the book tags
    fp = os.path.dirname(__file__)
    book_tag_fp = os.path.join(fp, DATA_FLR, GOOD_READ_FLR, booktagsfile)
    with open(book_tag_fp, "r", encoding="utf-8") as book_tag_file:
        reader = csv.DictReader(book_tag_file)
        for row in reader:
            # print(row)
            book_tag_lt.add_last(row)
    print("Book tags loaded successfully")
    print("Total book tags loaded: ", book_tag_lt.size())
    return catalog
