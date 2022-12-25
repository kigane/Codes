import sqlite3

conn = sqlite3.connect('sqlite/test.db')

cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE test(
#         ID INT,
#         Name text,
#         email text
#     );
# """)

lst = [
    (2, 'link', 'zelda@nintendo.com'),
    (3, 'ash', 'darksouls@fromsoftware.com'),
    (4, 'sekiro', 'sekiro@fs.com'),
]

# cursor.execute("INSERT INTO test VALUES(1, 'mario', 'mario@nintendo.com')")
# cursor.executemany("INSERT INTO test VALUES(?, ?, ?)", lst)

cursor = cursor.execute("SELECT * from test")

for row in cursor:
    print(row)

cursor.execute("UPDATE test set name='guda' where id=3")


conn.commit()
conn.close()