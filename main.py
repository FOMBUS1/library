from library import Library

lib = Library()

while True:
    print('''
        1: добавить новую книгу
        2: удалить книгу
        3: найти книгу (по title, author, year)
        4: изменить статус книги
        5: загрузить библиотеку из json файла
        6: вывести все книги в библиотеке
        7: узнать количество книг в библиотеке
        8: сохранить библиотеку в json файл
          ''')
    command = int(input())
    if command == 1:
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Year: "))
        lib.add(title, author, year)

    elif command == 2:
        bid = int(input("ID книги: "))
        lib.remove(bid)

    elif command == 3:
        title = input("Title (Enter если не нужен):")
        author = input("Author (Enter если не нужен):")
        year = input("Year (Enter если не нужен):")

        title = title if title != '' else None
        author = author if author != '' else None
        year = int(year) if year != '' else None

        lib.find(title, author, year)

    elif command == 4:
        bid = input("ID книги: ")
        status = input("Новый статус: ")

        lib.set_status(bid, status)

    elif command == 5:
        path = input("Путь к json файлу: ")
        lib = Library.load_from_json()

    elif command == 6:
        lib.print()

    elif command == 7:
        print(len(lib))

    elif command == 8:
        path = input("Путь для сохранения json файла: ")
        lib.save(path)