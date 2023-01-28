import sqlite3
import os
# import hashlib

class Database:
    def __init__(self):
        # Create database
        os.remove("library.db")
        self.connection = sqlite3.connect("library.db")

        # Create a cursor object 
        self.cursor_object = self.connection.cursor()

        # Create the logins table 
        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS logins (
                                        memberId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        login TEXT NOT NULL, 
                                        password BLOB NOT NULL
                                    );''')

        # Create memebers table
        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS members (
                                        memberId INTEGER PRIMARY KEY AUTOINCREMENT, 
                                        name TEXT NOT NULL,
                                        surname TEXT NOT NULL,
                                        address TEXT NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES logins (memberId)
                                    );''')

        # Create the books table                            
        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS books (
                                        ISBN TEXT PRIMARY KEY,
                                        Title TEXT NOT NULL,
                                        Author TEXT NOT NULL,
                                        Publication TEXT NOT NULL
                                    ); ''')

        # Create the loans table
        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS loans (
                                        loanId INTEGER PRIMARY KEY,
                                        memberId INTEGER NOT NULL,
                                        ISBN TEXT NOT NULL,
                                        loanDate TEXT NOT NULL,
                                        returnDate TEXT NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES members (memberId),
                                        FOREIGN KEY (ISBN) REFERENCES books (ISBN)
                                    );''')

        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS reservations (
                                        reservationId INTEGER PRIMARY KEY,
                                        memberId INTEGER NOT NULL,
                                        ISBN TEXT NOT NULL,
                                        reservationDate TEXT NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES members (memberId),
                                        FOREIGN KEY (ISBN) REFERENCES books (ISBN)
                                    );''')

        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS fines (
                                        fineId INTEGER PRIMARY KEY,
                                        memberId INTEGER NOT NULL,
                                        ISBN TEXT NOT NULL,
                                        fineAmount REAL NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES members (memberId),
                                        FOREIGN KEY (ISBN) REFERENCES books (ISBN)
                                    );''')

        # Add start admin and user to tables
        self.cursor_object.execute('''INSERT INTO logins (login, password) VALUES (?, ?)''', ("admin", "admin1"))
        self.cursor_object.execute('''INSERT INTO members (name, surname, address) VALUES (?, ?, ?)''', ("admin", "admin", "admin"))
        self.cursor_object.execute('''INSERT INTO logins (login, password) VALUES (?, ?)''', ("user", "user1")) 
        self.cursor_object.execute('''INSERT INTO members (name, surname, address) VALUES (?, ?, ?)''', ("user", "user", "user"))

        # Commit the changes
        self.connection.commit()


    def close_connection(self):
        self.connection.close()