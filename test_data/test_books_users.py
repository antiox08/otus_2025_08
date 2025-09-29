import csv
import json


def open_books():
    with open('books.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        books = list(reader)
    return books

def open_users():
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.loads(f.read())
    return users

def razdacha_books(books, users):
    num_users = len(users)
    num_books = len(books)
    base = num_books // num_users
    extra = num_books % num_users
    index = 0
    for i, user in enumerate(users):
        if i < extra:
            count = base + 1
        else:
            count = base
        user["books"] = books[index:index + count]
        index += count

    return users

def save_result(users_with_books):
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(users_with_books, f, ensure_ascii=False, indent=4)

# --- основной блок ---
def main():
    books = open_books()
    users = open_users()
    users_with_books = razdacha_books(books, users)
    save_result(users_with_books)

if __name__ == "__main__":
    main()