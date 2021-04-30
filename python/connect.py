import sqlite3

banco=sqlite3.connect('first_bank.db')
cursor=banco.cursor()

cursor.execute("CREATE TABLE people (name text,  age integer, email text)")

cursor.execute("INSERT INTO people VALUES('jason',40,'jason_13@gmail.com')")

banco.commit()
