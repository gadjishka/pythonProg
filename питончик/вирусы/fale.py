import os
def deleting2():
    filename = input("Введите путь к файлу: ")
    if os.path.exists(filename):
        print("Указанный файл существует")
    else:
        print("Файл не существует")
