import sqlite3

bank=sqlite3.connect('first_bank.db')
cursor=bank.cursor()

cursor.execute("CREATE TABLE people (name text,  age integer, email text)")

cursor.execute("INSERT INTO people VALUES('jason',40,'jason_13@gmail.com')")

bank.commit()
