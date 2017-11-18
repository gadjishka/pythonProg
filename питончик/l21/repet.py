import sqlite3

db = sqlite3.connect("GunsShop.db")
db_cur = db.cursor()

db_cur.execute("""CREATE TABLE IF NOT EXISTS GunsShop(
	ID INT PRIMARY KEY,
	name VARCHAR(16),
	skin VARCHAR(32),
	MaxAmmo INT,
	Price REAL
)""")
i = 1
while True:
	i +=1
	query = "INSERT INTO GunsShop VALUES(?, ?, ?, ?, ?)"
	data = i, input("Введите назване оружия: "), input("Введите раскраску оружия: "), int(input("Введите максимальный боезапас оружия: ")), int(input("Введите цену оружия: "))
	db_cur.execute(query,data)
	if input("Для выхода введите 0: ") == "0":
		break

db.commit()
db_cur.close()
db.close()