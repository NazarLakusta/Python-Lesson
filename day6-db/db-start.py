import sqlite3

# створення бази даних
conn = sqlite3.connect("my_database.db")

# створення курсора для виконання запитів
cursor = conn.cursor()


# створення таблиці
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER NOT NULL CHECK (age >= 0 AND age <= 100),
email TEXT UNIQUE NOT NULL 
)
""")


# # INSTERT INTO - добавити інформацію у таблицю
# cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
#                ("vasya", 19, "vasya1919@gmail.com")
#                )
#
# # підтвердити зміни
# conn.commit()


# SELECT - дістати список даних
cursor.execute("SELECT * FROM users")

# дістати інформацію з запиту
rows = cursor.fetchall()

# показую результат  запиту
print("SELECT * FROM users")
for row in rows:
    print(row)


# SELECT - дістати список даних вік яких більше за 20
cursor.execute("SELECT * FROM users WHERE age > 20 ")

# дістати інформацію з запиту
rows = cursor.fetchall()

# показую результат  запиту
print("SELECT * FROM users WHERE age > 20")
for row in rows:
    print(row)


# UPDATE - оновити інформацію в табличці
cursor.execute("""
UPDATE users
SET age = ?
WHERE name = ?
""", (25, "Nazar"))

conn.commit()


# DELETE - видалити дані з таблиці
cursor.execute("DELETE FROM users WHERE id = ?", (1,))

conn.commit()