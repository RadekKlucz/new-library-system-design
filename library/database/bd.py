import sqlite3
import os
import hashlib

class Database:
    def __init__(self):
        # Create database
        os.remove("library.db")
        self.connection = sqlite3.connect("library.db")

        # Create a cursor object 
        self.cursor_object = self.connection.cursor()

        # Create the logins table 
        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS logins (
                                        memberId INTEGER PRIMARY KEY,
                                        login TEXT NOT NULL, 
                                        password BLOB NOT NULL
                                    );
                                    ''')

        # Create memebers table
        self.cursor_object.execute('''CREATE TABLE IF NOT EXISTS members (
                                        memberId INTEGER PRIMARY KEY, 
                                        name TEXT NOT NULL,
                                        surname TEXT NOT NULL,
                                        address TEXT NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES logins (memberId)
                                    )   
                                    ''')

        # Create the books table                            
        self.cursor_object.execute("""CREATE TABLE IF NOT EXISTS books (
                                ISBN TEXT PRIMARY KEY,
                                Title TEXT NOT NULL,
                                Author TEXT NOT NULL,
                                Publication TEXT NOT NULL
                            )
                            """)

        # Create the loans table
        self.cursor_object.execute("""CREATE TABLE IF NOT EXISTS loans (
                                        loanId INTEGER PRIMARY KEY,
                                        memberId INTEGER NOT NULL,
                                        ISBN TEXT NOT NULL,
                                        loanDate TEXT NOT NULL,
                                        returnDate TEXT NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES members (memberId),
                                        FOREIGN KEY (ISBN) REFERENCES books (ISBN)
                                    )
                                    """)

        self.cursor_object.execute("""CREATE TABLE IF NOT EXISTS reservations (
                                        reservationId INTEGER PRIMARY KEY,
                                        memberId INTEGER NOT NULL,
                                        ISBN TEXT NOT NULL,
                                        reservationDate TEXT NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES members (memberId),
                                        FOREIGN KEY (ISBN) REFERENCES books (ISBN)
                                    )
                                    """)

        self.cursor_object.execute("""CREATE TABLE IF NOT EXISTS fines (
                                        fineId INTEGER PRIMARY KEY,
                                        memberId INTEGER NOT NULL,
                                        ISBN TEXT NOT NULL,
                                        fineAmount REAL NOT NULL,
                                        FOREIGN KEY (memberId) REFERENCES members (memberId),
                                        FOREIGN KEY (ISBN) REFERENCES books (ISBN)
                                    )
                                    """)

        # Commit the changes
        self.connection.commit()


    def get_login(self, login):
        self.cursor_object.execute('''SELECT * FROM logins WHERE login = ?''', (login,))
        return self.cursor_object.fetchone()


    def add_member(self, memeber_id, login, password, name, surname, address):
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor_object.execute('''INSERT INTO logins (memberId, login, password) VALUES (?, ?, ?)''', (memeber_id, login, hash_password))        
        self.cursor_object.execute('''INSERT INTO members (memberId, name, surname, address) VALUES (?, ?, ?, ?)''', (memeber_id, name, surname, address))
        self.connection.commit()


    def get_member(self, memberId):
        self.cursor_object.execute('''SELECT * FROM members WHERE memberId = ?''', (memberId,))
        return self.cursor_object.fetchone()


    def add_book(self, ISBN, title, author, publication):
        self.cursor_object.execute('''INSERT INTO books (ISBN, Title, Author, Publication) VALUES (?, ?, ?, ?)''', (ISBN, title, author, publication))
        self.connection.commit()


    def get_book(self, ISBN):
        self.cursor_object.execute('''SELECT * FROM books WHERE ISBN = ?''', (ISBN,))
        return self.cursor_object.fetchone()

    
    def get_all_books(self):
        self.cursor_object.execute('''SELECT * FROM books''')
        return self.cursor_object.fetchall()


    def delete_book(self, ISBN):
        self.cursor_object.execute('''DELETE FROM books WHERE ISBN = ?''', (ISBN,))
        self.connection.commit()


    def update_book(self, ISBN, title, author, publication):
        self.cursor_object.execute('''UPDATE books SET Title = ?, Author = ?, Publication = ? WHERE ISBN = ?''', (title, author, publication, ISBN))
        self.connection.commit()

    
    def add_loan(self, memberId, ISBN, loanDate, returnDate):
        self.cursor_object.execute('''INSERT INTO loans (memberId, ISBN, loanDate, returnDate) VALUES (?, ?, ?, ?)''', (memberId, ISBN, loanDate, returnDate))
        self.connection.commit()


    def get_loan(self, loanId):
        self.cursor_object.execute('''SELECT * FROM loans WHERE loanId = ?''', (loanId,))
        return self.cursor_object.fetchone()


    def get_all_loans(self):
        self.cursor_object.execute('''SELECT * FROM loans''')
        return self.cursor_object.fetchall()


    def delete_loan(self, loanId):
        self.cursor_object.execute('''DELETE FROM loans WHERE loanId = ?''', (loanId,))
        self.connection.commit()

    
    def add_reservation(self, memberId, ISBN, reservationDate):
        self.cursor_object.execute('''INSERT INTO reservations (memberId, ISBN, reservationDate) VALUES (?, ?, ?)''', (memberId, ISBN, reservationDate))
        self.connection.commit()


    def get_reservation(self, reservationId):
        self.cursor_object.execute('''SELECT * FROM reservations WHERE reservationId = ?''', (reservationId,))
        return self.cursor_object.fetchone()


    def get_all_reservations(self):
        self.cursor_object.execute('''SELECT * FROM reservations''')
        return self.cursor_object.fetchall()


    def delete_reservation(self, reservationId):
        self.cursor_object.execute('''DELETE FROM reservations WHERE reservationId = ?''', (reservationId,))
        self.connection.commit()


    def add_fine(self, memberId, ISBN, fineAmount):
        self.cursor_object.execute('''INSERT INTO fines (memberId, ISBN, fineAmount) VALUES (?, ?, ?)''', (memberId, ISBN, fineAmount))
        self.connection.commit()


    def get_fine(self, fineId):
        self.cursor_object.execute('''SELECT * FROM fines WHERE fineId = ?''', (fineId,))
        return self.cursor_object.fetchone()


    def get_all_fines(self):
        self.cursor_object.execute('''SELECT * FROM fines''')
        return self.cursor_object.fetchall()


    def delete_fine(self, fineId):
        self.cursor_object.execute('''DELETE FROM fines WHERE fineId = ?''', (fineId,))
        self.connection.commit()


    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    db = Database()
    db.add_member(1, "admin", "admin", "Admin", "Big", "Admin Street 1")
    print(db.get_login("admin"))
    print(db.get_member(1))
    db.add_book("1234567890123", "Title", "Author", "Publication")
    print(db.get_book("1234567890123"))
    db.add_book("2234567890123", "Title", "Author", "Publication")
    print(db.get_all_books())
    db.delete_book("1234567890123")
    print(db.get_all_books())
    db.add_book("1234567890123", "Title", "Author", "Publication")
    db.update_book("1234567890123", "New Title", "New Author", "New Publication")
    print(db.get_book("1234567890123"))
    db.add_loan(1, "1234567890123", "2020-01-01", "2020-01-15")
    print(db.get_loan(1))
    print(db.get_all_loans())
    db.delete_loan(1)
    print(db.get_all_loans())
    db.add_loan(1, "1234567890123", "2020-01-01", "2020-01-15")
    db.add_reservation(1, "1234567890123", "2020-01-01")
    print(db.get_reservation(1))
    print(db.get_all_reservations())
    db.delete_reservation(1)
    print(db.get_all_reservations())
    db.add_fine(1, "1234567890123", 10)
    print(db.get_fine(1))
    print(db.get_all_fines())
    db.delete_fine(1)
    print(db.get_all_fines())
    db.close_connection()