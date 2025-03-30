from dbhw16 import init_dbhw16, get_all_products, get_all_suppliers, get_all_categories, get_product_full_info_by_id, create_product


def print_menu():
    print("Выберите нужную команду:")
    print("0. Выход")
    print("1. Показать список книг")
    print("2. Показать список авторов")
    print("3. Показать список жанров")
    print("4. Показать детальную информацию по id книги (автор и жанры)")
    print("5. Добавить автора")
    print("6. Поиск книги по названию")


def app():
    init_hw17()
    print("Таблицы успешно созданы!")

    print("Вас приветствует, Онлайн Библиотека!")
    while True:
        print_menu()
        cmd = int(input("Введите номер команды: "))

        if cmd == 0:
            print("До скорой встречи!)")
            break
        elif cmd == 1:
            print("=" * 20)
            print("Список книг:")
            books = get_all_books()
            for book in books:
                print(f"ID: {book.id} - Название: {book.title}.")
            print("=" * 20)
        elif cmd == 2:
            print("=" * 20)
            print("Список авторов:")
            authors = get_all_authors()
            for author in authors:
                print(f"ID: {author.id} - ФИО: {author.full_name}.")
            print("=" * 20)
        elif cmd == 3:
            print("=" * 20)
            print("Список жанров:")
            genres = get_all_genres()
            for genre in genres:
                print(f"ID: {genre.id} - Название: {genre.name}.")
            print("=" * 20)
        elif cmd == 4:
            print("=" * 20)
            book_id = int(input("Введите ID книги, информацию о которой хотите получить: "))
            book_details = get_book_full_info_by_id(book_id)
            if book_details is None:
                print("Нет такой книги!")
            else:
                book_info = book_details["book_info"]
                print(f'ID: {book_info.id} - Название: {book_info.title}')

                genres = book_details["genres"]
                print("Жанры:")
                for genre in genres:
                    print(genre.name, end=" | ")

                authors = book_details["authors"]
                print("\nАвторы:")
                for author in authors:
                    print(author.full_name, end=" | ")
                print()
            print("=" * 20)
        elif cmd == 5:
            print("=" * 20)
            print("Добавление нового автора:")
            full_name = input("Введите ФИО автора: ")
            try:
                create_author(full_name)
                print("Автор успешно создан!")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
            print("=" * 20)
        elif cmd == 6:
            print("=" * 20)
            query = input("Введите название или часть названия книги: ")
            books = search_book(query)
            for book in books:
                print(f"ID: {book.id} - Название: {book.title}.")
            print("=" * 20)
        else:
            print("Вы ввели несуществующую команду. Попробуйте еще раз!")



app()