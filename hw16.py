
# Функционал:
# • Определение таблиц для товаров, категорий, поставщиков и заказов на
# поставку
# • Простые операции, такие как добавление/удаление/редактирование
# товаров/поставщиков/заказов/категорий, вывод информации о
# товаре/поставщике/заказе/категории по имени/названию
# • Создание отчетов о состоянии склада и истории движения товаров
# • Сложные операции, такие как поиск товара по категории, поиск
# товара/поставщика/whatever по частичному совпадению имени

import dbhw16



def print_menu():
    print("Выберите нужную команду:")
    print("0. Выход")
    print("1. Показать список товаров")
    print("2. Показать список поставщиков")
    print("3. Показать список заказов")
    print("4. Показать детальную информацию по id товара (поставщик и заказ)")
    print("5. Добавить товар")
    print("6. Поиск товара по названию")


def app():
    dbhw16.init_db()
    print("Таблицы успешно созданы!")

    print("Вас приветствует, Онлайн Магазин!")
    while True:
        print_menu()
        cmd = int(input("Введите номер команды: "))

        if cmd == 0:
            print("До скорой встречи!)")
            break
        elif cmd == 1:
            print("=" * 20)
            print("Список товаров:")
            products = dbhw16.get_all_products()
            for product in products:
                print(f"ID: {product[0]} - Название: {product[1]}.")
            print("=" * 30)
        elif cmd == 2:
            print("=" * 30)
            print("Список поставщиков:")
            suppliers = dbhw16.get_all_suppliers()
            for supplier in suppliers:
                print(f"ID: {supplier[0]} - Поставщик: {supplier[1]}.")
            print("=" * 30)
        elif cmd == 3:
            print("=" * 30)
            print("Список заказов:")
            supply_order = dbhw16.get_all_supply_orders()
            for supply_order in supply_orders:
                print(f"ID: {supply_order[0]} - Заказ: {supply_orders[1]}.")
            print("=" * 30)
        elif cmd == 4:
            print("=" * 30)
            product_id = int(input("Введите ID товара по которому хотите получить информацию: "))
            product_details = dbhw16.get_product_full_info_by_id(product_id)
            if product_details is None:
                print("Нет такого товара!")
            else:
                product_info = product_details["product_info"]
                print(f'ID: {product_info[0]} - Название: {product_info[1]}')

                categories = product_details["categories"]
                print("Категории:")
                for categories in categories:
                    print(categories[0], end=" | ")

                suppliers = product_details["products"]
                print("\nТовары:")
                for product in products:
                    print(product[0], end=" | ")
                print()

            print("=" * 30)
        elif cmd == 5:
            print("=" * 20)
            print("Добавление нового товара:")
            full_name = input("Введи название товара: ")
            try:
                dbhw16.create_product(full_name)
                print("Товар успешно создан!")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
            print("=" * 30)
        elif cmd == 6:
            print("=" * 30)
            query = input("Введите название и часть названия товара: ")
            products = dbhw16.search_product(query)
            for product in products:
                print(f"ID: {product[0]} - Название: {product[1]}.")
            print("=" * 30)
        else:
            print("Вы ввели несуществующею команду. Попробуйте еще раз!")
app()

