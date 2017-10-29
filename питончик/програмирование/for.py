# def my_sum(a, b):
#     # print(a + b)
#     return a +b
#
# ab_sum =  my_sum(25 ,50) # возвращает сумму
#
# number1 = int(input("введите первое число: "))
# number2 = int(input("введите второе число: "))
# my_sum(number1, number2)
# print(my_sum(number1, number2))

# def my_divided(n, m, l, k, p, o):
#     res = n / m + k / l +p* o
#     return res
#
# print(my_divided(n = 15,m = 5, o = 15, k = 20, p = 40, l = 18))

# def group(name1 = "Саид", name2 = "Саид", name3 = "Саид"):
#     group_list = "в нашей группе есть " + name1 + name2 + name3
#     return group_list
#
# # group("лукман" ,"Гаджи","Камиль","Шамиль","Ахмед","Залик")
# print(group("лукман" , "Гаджи"))

# print(15, 20)
# print(15, 20, sep="\n")
# print(15, 20, sep=" разбить")

def human_list(*args, **kwargs):
    for human in args:
        print(human + "-оглы")
    print(kwargs)


human_list("Адам", "Ева","Кайна","Авель", godfather = "Крестный пахан", hogfather =  "Санта-Хрякус")
