import sqlite3

conn = sqlite3.connect("GunsShop.db")
bd_cur = conn.cursor()

bd_cur.execute("""UPDATE GunsShop
	SET name = "AK-74"
	WHERE name = "rrr"
""")

bd_cur.execute("DELETE FROM GunsShop WHERE price > 10000")

bd_cur.execute("SELECT name, price FROM GunsShop ORDER BY price DESC")
a = bd_cur.fetchall()
print(a)
# for i in a:
# 	print(i)
bd_cur.close()
conn.close()