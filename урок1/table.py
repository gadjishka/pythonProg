import random
print("реши пример!!!")
number1 = random.randint(0, 10)
number2 = random.randint(0, 10)
answer =int(input("умножь " + str(number1)\
    + " на " + str(number2) + " : "))
if (answer == number1 * number2):
    print("Мужиг!!!")
    print(" Гордость нации ")
else:
    print("Позор , стыд , расстрел")
