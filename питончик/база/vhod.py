import os, time
os.system("cls")
class Users():
	def __init__(self, login, password):
		self.login = login
		self.password = password
	def register(self, users_list):
		if self.login in users_list:
			print("Такой пользователь уже существует")
		else:
			users_list[self.login] = self.password
			print("Вы успешно зарегестрировались")

	def aythorize(self, users_list):
		if self.login in users_list:
			print('Успешная авторизация')
		else:
			print('Такой пользователь не существует')
			choice = input('1)Попробовать ещё раз 2)Создать новый аккаунт : ')
			if choice == '1':
				aythorize(users_list)
			elif choice == '2':
				register(users_list)

def work(users_list):
		time.sleep(2)
		os.system("cls")
		print("="*50)
		print("="*50)
		print("="*50)
		exit = 0
		choic = input('1)Войти 2)Регистрация 3)Посмотреть список авторизованных пользователей 4)Выход :')
		if choic == '1':
			os.system("cls")
			print("="*50)
			print("="*23,"Вход","="*21)
			user = Users(input('Введите логин:'), input('Введите пароль:'))
			user.aythorize(users_list)
		elif choic == '2':
			os.system("cls")
			print("$"*50)
			print("$"*19,"Регистрация","$"*18)
			print("$"*50)
			user = Users(input('Введите логин:'), input('Введите пароль:'))
			user.register(users_list)
		elif choic == '3':
			print("#"*70)
			print("#"*17,"Список авторизованных пользователей","#"*16)
			print("#"*70)
			i = 0
			while i < len(users_list):
				print(users_list[i])
				i += 1
			print(users_list)
		elif choic == "4":
			f = open("Users.txt" , "w")
			for i in users_list.keys():
				f.write(i +"-"+ users_list[i])
			exit = 1
			f.close()
		else:
			print("Ты поступаешь плохо")
		return exit
users_list = {}
while True:
	i = work(users_list)
	print(users_list)
	if i == 1:
		break
