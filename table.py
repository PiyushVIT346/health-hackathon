import sqlite3

def create_table():
    
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            history TEXT DEFAULT '[]'
        )
        ''')
        cursor.execute("SELECT * FROM users2")
        rows = cursor.fetchall()
        if rows:
            print("ID | Name         | Email                | Password      | History")
            print("----------------------------------------------------------------------")
            for row in rows:
                print(f"{row[0]:<3} | {row[1]:<12} | {row[2]:<20} | {row[3]} | {row[4]}")
        else:
            print("No users found in the database.")

        conn.commit()
create_table()
