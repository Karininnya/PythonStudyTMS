
# Создайте класс EmailValidator с методом is_valid(email), который проверяет, содержит ли email символ '@' и точку '.'.*
# class EmailValidator:
#     def __init__(self, email):
#         self.email = email
#
#
#     def is_valid(self):
#         return "@" in self.email and "." in self.email
#
# e1 = EmailValidator('test.com')
# print(e1.is_valid())



# Создайте класс Animal** с методом make_sound(), от него унаследуйте Cat и Dog, переопределив звук.
class Animal:
    def make_sound(self):
        print('sound')

class Cat(Animal):
    def make_sound(self):
        print("meow")
class Dog(Animal):
    def make_sound(self):
        print('rr')
cat = Cat()
dog = Dog()
cat.make_sound()
dog.make_sound()





















