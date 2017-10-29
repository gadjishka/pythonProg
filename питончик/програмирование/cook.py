# получить все продукты в холодильнике
# перебрать и приготовить
# дать название нашему блюду - первый буквые буквы ингридиентов
import random
def cooking(*args , major = "Майонез"):
    for product in args:
        making(product)
        food_name(args)
        pass
    print("Обольем сверху "+major)
    print("Наше блюдо -" , food_name(args))
    pass
def making(eda):
    print(random.choice(cook_var) , eda)
    pass
def food_name(ings):
    name = ""
    for ing in ings:
        name += ing[1]
        pass
    return name
    pass
cook_var = ["Пожарим" , "Сожжем" , "Похороним" , "Разгоним до скорости света"]
cooking("яйца" , "кепчук" , "мазик" , "труп кошки" , "ион" , "процессор")
