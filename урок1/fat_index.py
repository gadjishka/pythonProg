weight = int(input(" введи свой вес, dude: "))
print(weight)
if (weight == 20):
    print("тебя сдувает ветром ")
elif (weight < 20):
    print("лифт не реагирует на тебя")
elif (weight > 20 and weight < 30):
    print(" можешь кататься на кошках")
elif (weight > 30 and weight < 40):
    print(" Тебя выдержит собака")
elif (40 < weight < 50):
    print(" ты король ящериц")
elif (weight == 66 or weight > 300):
    print(" ты исщадие ада")
elif (weight >= 70 and weight != 75):
    print(" ты турникмен")
else:
    print("Ты Шварц!!")
