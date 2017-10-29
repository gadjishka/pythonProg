print("Игрок 1 - Чайка            Игрок 2 - Ниво")
print("          speed: 5                   speed: 3")
print("          fuel: 25                   fuel: 35")
print("          spend: 2                   spend: 3")
print("          nitro: 8                   nitro: 11")
def ride(car):
    car["distanse"] += car["speed"]
    car["fuel"] -= car["spend"]

def faster(car):
    car["speed"] += 2
    car["spend"] += 2

def nitro(car):
    car["distanse"] += car["nitro"]
    car["fuel"] -= car["spend"] * 3

def car_info(car):
    print("\n Текущее состояние: ",
        "Топливо: " + str(car["fuel"]),
        "Скорость: " + str(car["speed"]),
        "Проехали: " + str(car["distanse"]) #+ "/" + str(track))
        )

print("1 - ехать")
print("2 - прибавить скорости , но ты не едешь и увеличивается расход топлива")
print("ничего не выбрано - нитро, большой расход топлива ,но больше проезжаешь")


def race_step(car):
    print(" ")
    choose = input("Твой ход, " + car["name"] + " Что будем делать дальше: ")

    if choose == "1":
        ride(car)
    elif choose == "2":
        faster(car)
    else:
        nitro(car)
    car_info(car)

    # input()

car1 = {
    "name": "Чайка",
    "speed": 5,
    "fuel": 25,
    "spend": 2,
    "nitro": 8,
    "distanse": 0
}
car2 = {
    "name": "Ниво",
    "speed": 3,
    "fuel": 35,
    "spend": 3,
    "nitro": 11,
    "distanse": 0
}
# car3 = {
#     "name": "Шиха",
#     "speed": 6,
#     "fuel": 30,
#     "spend": 5,
#     "nitro": 10,
#     "distanse": 0
# }

track = 40
while True:
    race_step(car1)
    race_step(car2)
    if car1["fuel"] <=0:
        print("Игрок с машиной",car1["name"]," проигрывает гонку!.","Игрок с машиной",car2["name"]," выигрывает гонку!!")
        break
    elif car1["distanse"] >= track:
        print("Игрок с машиной",car1["name"]," выигрывает гонку!!")
        break
    if car2["fuel"] <=0:
        print("Игрок с машиной",car2["name"]," проигрывает гонку!.","Игрок с машиной",car1["name"]," выигрывает гонку!!")
        break
    elif car2["distanse"] >= track:
        print("Игрок с машиной",car2["name"]," выигрывает гонку!!")
        break
