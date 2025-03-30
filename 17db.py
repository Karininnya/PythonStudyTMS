from 17hw import init_17hw, get_all_products, get_all_suppliers, get_product_full_info_by_id, create_product, search_product

def print_menu():
   print("Выберите нужную команду:")
   print("0. Выход")
   print("1. Показать список товаров")
   print("2. Показать список поставщиков")
   print("3. Показать детальную информацию по id товара")
   print("4. Добавить товар")
   print("5. Поиск товара по названию")

def app():
   init_17hw()
   print("Таблицы успешно созданы!")
   engine = create_engine(DATABASE_URL)
   Session = sessionmaker(bind=engine)
   session = Session()

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
           products = get_all_products(session)
           for product in products:
               print(f"ID: {product.id} - Название: {product.name}.")
           print("=" * 30)
       elif cmd == 2:
           print("=" * 30)
           print("Список поставщиков:")
           suppliers = get_all_suppliers(session)
           for supplier in suppliers:
               print(f"ID: {supplier.id} - Поставщик: {supplier.name}.")
           print("=" * 30)
       elif cmd == 3:
           print("=" * 30)
           product_id = int(input("Введите ID товара по которому хотите получить информацию: "))
           product = get_product_full_info_by_id(session, product_id)
           if product is None:
               print("Нет такого товара!")
           else:
               print(f'ID: {product.id} - Название: {product.name} - Цена: {product.price} - Остаток: {product.stock_quantity}')
           print("=" * 30)
       elif cmd == 4:
           print("=" * 20)
           print("Добавление нового товара:")
           name = input("Введи название товара: ")
           price = float(input("Введите цену товара: "))
           stock_quantity = int(input("Введите количество товара: "))
           category_id = int(input("Введите ID категории: "))
           supplier_id = int(input("Введите ID поставщика: "))
           try:
               create_product(session, name, price, stock_quantity, category_id, supplier_id)
               print("Товар успешно создан!")
           except Exception as e:
               print(f"Что-то пошло не так! {e}")
           print("=" * 30)
       elif cmd == 5:
           print("=" * 30)
           query = input("Введите название и часть названия товара: ")
           products = search_product(session, query)
           for product in products:
               print(f"ID: {product.id} - Название: {product.name}.")
           print("=" * 30)
       else:
           print("Вы ввели несуществующую команду. Попробуйте еще раз!")

if __name__ == "__main__":
   app()