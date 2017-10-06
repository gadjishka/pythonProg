avengers = ["Арамен","человек шашлык","тор"]
print(avengers)
avengers.insert(2,"Халк")
print(avengers)
del avengers[1]
print(avengers)
antiavengers = ["Локти","Ник Фура","Капитан Ледышка"]
print(antiavengers)
antiavengers.remove("Ник Фура")
print(antiavengers)
avengers += antiavengers
print(avengers)
