
# Создайте класс EmailValidator с методом is_valid(email), который проверяет, содержит ли email символ '@' и точку '.'.*
class EmailValidator:
    def __init__(self, email):
        self.email = email


    def is_valid(self):
        return "@" in self.email and "." in self.email

e1 = EmailValidator('test.com')
print(e1.is_valid())
