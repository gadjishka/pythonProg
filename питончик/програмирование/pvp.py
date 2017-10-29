import random
print("$" * 30)
print("$$$$$$$$$$-PVP-BATLE-$$$$$$$$$")
print("$" * 30)
print("Первичная настройка персонажей :")
def create_player():
    player = {"Имя" : input("Введите имя игрока : ") , "Здоровье" : 50 , "Урон рукопашного боя" : 0 , "Время после рукопашного боя" : 0 , "Урон огнестрельного оружия" : 0 , "патроны" : 10 , "Время после стрельбы" : 0}
    print("1) Меч Хоббита 2) Хлыст 3) Кувалда 4) Посох 5) Ножик")
    choose1 = input("Выберите оружие ближнего боя :")
    print("1) Калаш 2) Винтовка Мосина 3) Дробовик 4) РПГ ")
    choose2 = input("Выберите оружие дальнего боя :")
    if choose1 == "1":
        player["Урон рукопашного боя"] = 7
        player["Время после рукопашного боя"] = 2
    elif choose1 == "2":
        player["Урон рукопашного боя"] = 5
        player["Время после рукопашного боя"] = 1
    elif choose1 == "3":
        player["Урон рукопашного боя"] = 10
        player["Время после рукопашного боя"] = 4
    elif choose1 == "4":
        player["Урон рукопашного боя"] = 11
        player["Время после рукопашного боя"] = 5
    elif choose1 == "5":
        player["Урон рукопашного боя"] = 9
        player["Время после рукопашного боя"] = 3

    if choose2 == "1":
        player["Урон огнестрельного оружия"] = 21
        player["Время после стрельбы"] = 5
        player["Текущая перезарядка"] = 0
    elif choose2 == "2":
        player["Урон огнестрельного оружия"] = 16
        player["Время после стрельбы"] = 4
        player["Текущая перезарядка"] = 0
    elif choose2 == "3":
        player["Урон огнестрельного оружия"] = 12
        player["Время после стрельбы"] = 3
        player["Текущая перезарядка"] = 0
    elif choose2 == "4":
        player["Урон огнестрельного оружия"] = 8
        player["Время после стрельбы"] = 2
        player["Текущая перезарядка"] = 0
    print(player)
    return player

def attack(attacker , victin):
    print("1) Холодное оружие 2) Огнестрельное оружие")
    print(attacker["Имя"] , "атакует игрока" , victin["Имя"])
    gun = input("Выберите чем будете воевать : ")
    if gun == "1":
        damage = random.randint(attacker["Урон рукопашного боя"]-3,attacker["Урон рукопашного боя"]+3)
        print("Игрок" , victin["Имя"] , "потерял" , damage , "из" , victin["Здоровье"])
        victin["Здоровье"] -= damage
        attacker["Текущая перезарядка"] -= 1
    elif (gun == "2")and(attacker["Текущая перезарядка"] > 0):
        print("Идет перезарядка! Вы можете воевать только в рукопашном бою!")
        damage = random.randint(attacker["Урон огнестрельного оружия"]-3,attacker["Урон огнестрельного оружия"]+3)
        print(attacker["Имя"] , "атакует игрока" , victin["Имя"])
        victin["Здоровье"] -= damage
        print("Игрок" , victin["Имя"] , "потерял" , damage , "из" , victin["Здоровье"])
        attacker["Текущая перезарядка"] -= 1
    elif (gun == "2")and(attacker["патроны"] > 0)and(attacker["Текущая перезарядка"] <= 0) :
        damage = random.randint(attacker["Урон огнестрельного оружия"]-3,attacker["Урон огнестрельного оружия"]+3)
        print("Игрок" , victin["Имя"] , "потерял" , damage , "из" , victin["Здоровье"])
        attacker["Текущая перезарядка"] = attacker["Время после стрельбы"]
        victin["Здоровье"] -= damage
        attacker["патроны"] -= 1
        attacker["Текущая перезарядка"] -= 1

player1 = create_player()
player2 = create_player()

while (player2["Здоровье"] > 0)and(player1["Здоровье"] > 0):
    attack(player1 , player2)
    attack(player2 , player1)
    if player1["Здоровье"] <=0:
        print("Игрок",player1["Имя"],"был убит.")
    elif player2["Здоровье"] <=0:
        print("Игрок",player2["Имя"],"был убит.")
