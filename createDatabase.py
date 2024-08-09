import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE balance (balance TEXT)')
print("Created table successfully!")

conn.close()
