import mysql.connector as mys
import numpy as np
from colorama import init, Fore, Back, Style


class style:
    BOLD = "\033[1m"
    END = "\033[0m"
    UNDERLINE = '\033[4m'


mydb = mys.connect(user="root", password="bgsps", database="sakila")
cursor = mydb.cursor()
cursor.execute("SELECT * FROM actor")
myresult = cursor.fetchall()

lens = np.max([[len(str(xi)) for xi in x] for x in myresult], axis=0)
myformat = Fore.MAGENTA + " | " + f" {Fore.MAGENTA} | ".join([Fore.BLUE + "{}" + style.END] * len(lens)) + Fore.MAGENTA + " | " + style.END

for col in myresult:
    print(myformat.format(*map(str.ljust, map(str, col), lens)))
