import os
os.system("cls")
class User:
	def __init__(self , login , password):
		self.login = login
		self.password = password
	def register(self):
		os.system("cls")
		file = open("accounts.txt" , "r")
		for log in file:
			if self.login in log.split(":")[0]:
				print("Пользователь с таким именем уже существует!")
				break
		else:
			file = open("accounts.txt" , "a")
			file.write(self.login + ": " + self.password + "\n")
			file.close()
			print("Регистрация прошла успешно .")
			print("Логин -",self.login,"Пароль -",self.password)
		file.close()
	def autorize(self):
		os.system("cls")
		file = open("accounts.txt", "r")
		for log in file:
			if self.login == log.split(": ")[0] and self.password == log.rstrip("\n").split(": ")[1]:
				print("Вход выполнен .")
				self.magazin()
				break
		else:
			os.system("cls")
			print("Ползователь не найден .")
			print("1) авторизироваться повторно\n2) зарегистрироваться")
			choise = input()
			if choise == "1":
				self.autorize()
			elif choise == "2":
				self.register()
			else:
				print("Нипанятна")
		file.close()
	def magazin(self):
		file = open("tovari.txt" , "r")
		print("Список товаром :")
		print("|Название|     |Цена|")
		for prod in file:
			print(prod)
		file.close()

user = User(input("Введите логин : ") , input("Введите пароль : "))
user.autorize()