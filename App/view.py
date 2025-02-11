import App.logic as lg


def new_catalog():
    catalog = lg.new_catalog()
    return catalog


def load_books(catalog, file):
    lg.load_books(catalog, file)
    return catalog


def print_menu():
    print("=== Menu Options ===")
    print("1. Load books")
    print("2. Load tags")
    print("3. Load book tags")
    print("4. Search book by title")
    print("5. Search book by author")
    print("6. Search book by tag")
    print("7. Exit")
    print("Enter your choice: ")


def opt_selection(catalogue):
    opt = input("Select an option:\n")
    opt = int(opt)
    if opt == 1:
        print("Loading books...")
        booksfile = "books-small.csv"
        catalogue = load_books(catalogue,
                               booksfile)
    elif opt == 2:
        print("Loading tags...")
        tagsfile = "tags.csv"
        catalogue = lg.load_tags(catalogue,
                                 tagsfile)

    elif opt == 3:
        print("Loading book tags...")
        booktagsfile = "book_tags-small.csv"
        catalogue = lg.load_book_tags(catalogue,
                                      booktagsfile)


def main(catalogue):
    working = True
    while working:
        print_menu()
        opt_selection(catalogue)
        print()


if __name__ == '__main__':
    cat = new_catalog()
    main(cat)
