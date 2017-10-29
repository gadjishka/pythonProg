import os
import delet
import deleting
import rename
import fale
# путь относительно текущего скрипта
os.mkdir("hello")
print("Что делать дальше ?   1 - удалить созданную папку;2 - проверить существ\
ует ли файл gadji.py ;3 - удалить файл gadji.py; 4 - переименовать файл \
gadji.py в fales.py  ")
a = int(input("Введите число: "))
if a == 1:
    delet.deleting1()
elif a == 2:
    fale.deleting2()
elif a == 3:
    deleting.deleting3()
elif a == 4:
    rename.deleting4()
