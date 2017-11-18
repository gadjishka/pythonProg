class MyError(Exception):
    pass
class Calculat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def summ(self):
        return self.x + self.y

    def diff(self):
        return self.x - self.y

    def multiplicat(self):
        return self.x*self.y

    def division(self):
        return self.x / self.y
try:
    my_list = [1,2,3]
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    if x == 13 or y ==13:
        raise MyError("SMS")
    number = Calculat(x,y)
    print(number.division())
    print("hh.ru")
except ZeroDivisionError as word:
    print("Возникла следущая ошибка", word)
except IndexError as word:
    print("Выход за границы списка", word)
except (TypeError, ValueError) as word:
    print("Неправильное приведение типов", word)
except MyError as word:
    print("Возникла наша ошибка", word)
except:
    print("возникла неизвестная ошибка")
