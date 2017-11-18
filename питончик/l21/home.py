import sqlite3
import os
os.system("cls")
class User:
	def __init__(self , login , password):
		self.login = login
		self.password = password
	def register(self):
		os.system("cls")
		file = open("account.txt" , "r")
		for log in file:
			if self.login in log.split(":")[0]:
				print("Пользователь с таким именем уже существует!")
				break
		else:
			file = open("account.txt" , "a")
			file.write(self.login + ": " + self.password + "\n")
			file.close()
			print("Регистрация прошла успешно .")
			print("Логин -",self.login,"Пароль -",self.password)
		file.close()
	def autorize(self):
		os.system("cls")
		file = open("account.txt", "r")
		for log in file:
			if self.login == log.split(": ")[0] and self.password == log.rstrip("\n").split(": ")[1]:
				print("Вход выполнен .")
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


bd = sqlite3.connect("GameShop.db")
bd_cur = bd.cursor()


bd_cur.execute("""CREATE TABLE IF NOT EXISTS GameShop(
		name VARCHAR(16) PRIMARY KEY,
		genre VARCHAR(16),
		rating REAL,
		price REAL
)""")
while True:
	user = User(input("Введите логин : ") , input("Введите пароль : "))
	user.autorize()
	query = "INSERT INTO GameShop VALUES(?, ?, ?, ?)"
	data = input("Введите назване игры: "), input("Введите жанр игры: "), int(input("Введите рейтинг игры: ")), int(input("Введите цену оружия: "))
	bd_cur.execute(query,data)
	if input("Для выхода введите 0: ") == "0":
		break

bd.commit()
bd_cur.close()
bd.close()