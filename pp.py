import mysql.connector as mys
import numpy as np

mydb = mys.connect(user="root", password="", database="sakila")
cursor = mydb.cursor()
cursor.execute("SELECT * FROM actor")
myresult = cursor.fetchall()

lens = np.max([[len(str(xi)) for xi in x] for x in myresult], axis=0)
myformat = "|" + "|".join(["{}"] * len(lens)) + "|"

for col in myresult:
    print(myformat.format(*map(str.ljust, map(str, col), lens)))
