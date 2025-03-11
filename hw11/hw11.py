# ПчёлоСлон
# Экземпляр класса инициализируется двумя целыми числами,
# первое относится к пчеле, второе – к слону. Класс реализует
# следующие методы:
# ● fly() – возвращает True, если часть пчелы не меньше части
# слона, иначе – False
# ● trumpet() – если часть слона не меньше части пчелы,
# возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
# ● eat(meal, value) – может принимать в meal только ”nectar”
# или “grass”. Если съедает нектар, то value вычитается из
# части слона, пчеле добавляется. Иначе – наоборот. Не
# может увеличиваться больше 100 и уменьшаться меньше 0.

class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        return False

    def trumpet(self):
        if self.bee <= self.elephant:
            return 'tu-tu-doo-doo!'
        return 'wzzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            self.bee += value
            self.elephant -= value
        elif meal == 'grass':
            self.bee -= value
            self.elephant += value
        if self.elephant > 100:
            self.elephant = 100
        elif self.elephant < 0:
            self.elephant = 0
        if self.bee > 100:
            self.bee = 100
        elif self.bee < 0:
            self.bee = 0
        return 'nectar'

    def get_parts(self):
        return (self.bee, self.elephant)

be = BeeElephant(6, 4)
print(be.fly())
print(be.trumpet())
be.eat('grass', 6)
print(be.get_parts())

be = BeeElephant(17, 97)
print(be.fly())
print(be.trumpet())
be.eat('nectar', 80)
print(be.get_parts())

# Класс «Товар» содержит следующие закрытые поля:
# ● название товара
# ● название магазина, в котором подаётся товар
# ● стоимость товара в рублях
# Класс «Склад» содержит закрытый массив товаров.
# Обеспечить следующие возможности:
# ● вывод информации о товаре со склада по индексу
# ● вывод информации о товаре со склада по имени товара
# ● сортировка товаров по названию, по магазину и по цене
# ● перегруженная операция сложения товаров по цене


class Goods:
   def __init__(self, title, shop, price):
       self.__title = title
       self.__shop = shop
       self.__price = price

   def get_info(self):
       return f"Товар: {self.__title}, Магазин: {self.__shop}, Цена: {self.__price} руб."

   def get_title(self):
       return self.__title

   def get_price(self):
       return self.__price


class Store:
   def __init__(self):
       self.__goods = []

   def add_goods(self, goods):
       self.__goods.append(goods)

   def get_goods_by_index(self, index):
       if 0 <= index < len(self.__goods):
           return self.__goods[index].get_info()
       else:
           return "Товар не найден."

   def get_goods_by_name(self, name):
       for goods in self.__goods:
           if goods.get_name() == name:
               return goods.get_info()
       return "Товар не найден."

   def sort_goods_by_name(self):
       self.__goods.sort(key=lambda x: x.get_name())

   def sort_goods_by_shop(self):
       self.__goods.sort(key=lambda x: x.get_shop())

   def sort_goods_by_price(self):
       self.__goods.sort(key=lambda x: x.get_price())

   def __add__(self, other):
       if isinstance(other, Goods):
           total_price = sum(goods.get_price() for goods in self.__goods) + other.get_price()
           return total_price

if __name__ == "__main__":
   store = Store()

   product1 = Goods("Яблоко", "Магазин 1", 50)
   product2 = Goods("Банан", "Магазин 2", 30)
   product3 = Goods("Апельсин", "Магазин 1", 40)

   store.add_goods(product1)
   store.add_goods(product2)
   store.add_goods(product3)

   print(store.get_goods_by_index(1))

   store.sort_goods_by_price()
   for goods in store._Store__goods:
       print(goods.get_info())

# Класс «Автобус». Класс содержит свойства:
# ● скорость
# ● максимальное количество посадочных мест
# ● максимальная скорость
# ● список фамилий пассажиров
# ● флаг наличия свободных мест
# ● словарь мест в автобусе
# Методы:
# ● посадка и высадка одного или нескольких пассажиров
# ● увеличение и уменьшение скорости на заданное значение
# ● операции in, += и -= (посадка и высадка пассажира по
# фамилии)

# class Bus:
#     def __init__(self, speed, maxseat, maxspeed, emptyseat, dictseat):
#         self.speed = 0
#         self.maxseat = maxseat
#         self.maxspeed = maxspeed
#         self.passengername = [ ]
#         self.emptyseat = emptyseat
#         self.dictseat = dictseat
#     @property
#     def
