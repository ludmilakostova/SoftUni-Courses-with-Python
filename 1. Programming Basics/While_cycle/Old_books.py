preferred_book = input()
count_books = 0
book_name = input()
while book_name != "No More Books":
    if book_name == preferred_book:
        print(f'You checked {count_books} books and found it.')
        break
    count_books += 1
    book_name = input()

if book_name == "No More Books":
    print(f'The book you search is not here!')
    print(f'You checked {count_books} books.')
