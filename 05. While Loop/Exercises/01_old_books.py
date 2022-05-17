favourite_book = input()
count_book = 0
current_book = input()
book_is_found = False

while current_book != "No More Books":
    if current_book == favourite_book:
        book_is_found = True
        break
    count_book += 1
    current_book = input()#garantee that while will work and end
if book_is_found:
    print(f"You checked {count_book} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {count_book} books.")
