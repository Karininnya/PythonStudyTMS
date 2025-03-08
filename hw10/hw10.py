
class Soda:
    def __init__(self, taste=False):
        self.taste = taste

    def __str__(self):
        return f'Газировка и {self.taste}' if self.taste else 'Обычная газировка'


a = Soda()
b = Soda('Клубничный вкус')
print(a)
print(b)

class Math:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def addition(self):
       result = self.a + self.b
       print("Сложение:", result)
   def multiplication(self):
       result = self.a * self.b
       print("Умножение:", result)
   def division(self):
       if self.b != 0:
           result = self.a / self.b
           print("Деление:", result)
       else:
           print("Деление на ноль невозможно.")
   def subtraction(self):
       result = self.a - self.b
       print("Вычитание:", result)
a = float(input("Введите A: "))
b = float(input("Введите B: "))
math_obj = Math(a, b)
math_obj.addition()
math_obj.multiplication()
math_obj.division()
math_obj.subtraction()


class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def car_on(self):
        print('Автомобиль заведен')
    def car_off(self):
        print('Автомобиль заглушен')


    def set_color(self, color):
        self.color = color
        print(f"Цвет: {self.color}")
    def set_type(self, type):
        self.type = type
        print(f"Модель: {self.type}")
    def set_year(self, year):
        self.year = year
        print(f"Год выпуска: {self.year}")
car = Car(color="красный", type="хэтчбэк", year=2020)
car.car_on()
car.car_off()
car.set_color("черный")
car.set_type("универсал")
car.set_year(2002)
