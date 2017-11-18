file = open("New_File.txt", "r")
print("У нас в файле хранится следующая информация:", file.read())
file.close()
file = open("New_File.txt", "a")
name_list = ["Гаджи", "Адам", "Залимхан"]
i = 1
for name in name_list:
	file.write("\n" + str(i) + ": " + name)
	i += 1
file.close()
file = open("New_File.txt", "r+")
print("Состав группы: ")
print("!!!" + file.readline())
file.close()