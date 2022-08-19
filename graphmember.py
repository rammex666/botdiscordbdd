import matplotlib.pyplot as plt
import sqlite3 as sq
conn=sq.connect("bot.dbs")
c=conn.cursor()

c.execute("""select id from info""")
item=c.fetchall()


x = [0]
ye = 0

for items in item:
  ye = ye + 1
  if ye + 1:
    x.append(ye)


print("Membres : " + str(ye))


plt.plot(x , x, marker = 'o', color = 'red', markersize = 10)
plt.show()