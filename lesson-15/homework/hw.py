import sqlite3


conn = sqlite3.connect("school.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")


conn.commit()


conn.close()

print("Roster jadvali muvaffaqiyatli yaratildi!")

import sqlite3

# Bazaga ulanamiz
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Jadvalga ma'lumot qo‘shamiz
data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

cursor.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", data)

conn.commit()
conn.close()

print("3 ta yozuv muvaffaqiyatli qo‘shildi!")


import sqlite3

# Bazaga ulanish
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Ma'lumotni yangilash
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

conn.commit()
conn.close()

print("Jadzia Dax ismi Ezri Dax ga yangilandi!")


import sqlite3

# Bazaga ulanish
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Bajoranlarni chiqarish
cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()

# Natijani ekranga chiqarish
for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")

conn.close()


