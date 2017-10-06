week = ("Monday","Tuesday","Wednesday")  #кортеж
print(week[1])
week2 = "Thursday","Friday"
# week3 = "Saturday",
# print(week3)
# full_week = []
# full_week.append(week)
# print(full_week)
a, b = week2
print(a, b)
x, y, z = "Пн","Вт","Ср"
print(x, y, z)

pupils = {" Карл Маркс","Альберт Эйнштейн","Султанмурад","Чарльз Дарвин"} #множество
print(pupils)
if " Карл Маркс" in pupils:
    print("Карл Маркс победил!!")
else:
    print("Забудь о комуннах")

madteam = {" Карл Маркс","Альберт Эйнштейн","Джон Нэш","Дональд Трамп" \
,"Мальчик-ракета"}
print(pupils & madteam) #пересечение
print(pupils | madteam) #объединение
print(madteam - pupils) #вычитание
print("-" * 50)
films = {
    "Люся": "Люся получет супермозг",
    "Безумный Маркс": "Земля превратилась в пустыню - коммунизм победил",
    "защитники": "Наш ответ Западу!  Медведь, узбек, деваха-невидимка"
}
print(films["защитники"])
films["Люся"] = "Люся теряет костный мозг"
print(films)
films[7] = "Жестокий фильм про семь смертных грехов"
print(films[7])
films["Человек-паук 1", "Второй человек-паук"] = ["позор"]
print(films["Человек-паук 1", "Второй человек-паук"])
for key in films:
    print(key)
    if key == "Люся":
        print("позор")
for description in films.values():
    print(description)

for name, desc in films.items():
    print("Фильм: " + str(name) + " Описание :" + str(desc))
