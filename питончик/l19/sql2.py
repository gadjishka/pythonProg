import sqlite3

conn = sqlite3.connect("csgamers.db")
bd_cur = conn.cursor()

bd_cur.execute("SELECT * FROM cs_gamers")
info = bd_cur.fetchall()
print(info)

conn.commit()

bd_cur.close()
conn.close()