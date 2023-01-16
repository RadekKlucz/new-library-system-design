from library.main.python.database import Database

class Query(Database):
    def __init__(self):
        super().__init__()
        
    # Action for logins table
    def get_login(self, login, password):
        self.cursor_object.execute('''SELECT * FROM logins WHERE login = ? AND password = ?''', (login, password))
        return self.cursor_object.fetchone()

    # Action for members table
    def add_member(self, login, password, name, surname, address):
        # hash_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor_object.execute('''INSERT INTO logins (login, password) VALUES (?, ?)''', (login, password))        
        self.cursor_object.execute('''INSERT INTO members (name, surname, address) VALUES (?, ?, ?)''', (name, surname, address))
        self.connection.commit()
        
    def delete_member(self, login, password):
        pass
    

    def get_member(self, login):
        self.cursor_object.execute('''SELECT members.memberID, members.name, members.surname, members.address FROM members 
                                   INNER JOIN logins ON members.memberID = logins.memberId WHERE logins.login = ?''', (login,))
        return self.cursor_object.fetchone()
    
    # def get_all_members(self):
    #     self.cursor_object.execute('''SELECT * FROM members''')
    #     return self.cursor_object.fetchall()

    # Action for books table
    def add_book(self, ISBN, title, author, publication):
        self.cursor_object.execute('''INSERT INTO books (ISBN, Title, Author, Publication) VALUES (?, ?, ?, ?)''', (ISBN, title, author, publication))
        self.connection.commit()


    def get_book(self, ISBN):
        self.cursor_object.execute('''SELECT * FROM books WHERE ISBN = ?''', (ISBN,))
        return self.cursor_object.fetchone()

    
    # def get_all_books(self):
    #     self.cursor_object.execute('''SELECT * FROM books''')
    #     return self.cursor_object.fetchall()


    def delete_book(self, ISBN):
        self.cursor_object.execute('''DELETE FROM books WHERE ISBN = ?''', (ISBN,))
        self.connection.commit()


    # def update_book(self, ISBN, title, author, publication):
    #     self.cursor_object.execute('''UPDATE books SET Title = ?, Author = ?, Publication = ? WHERE ISBN = ?''', (title, author, publication, ISBN))
    #     self.connection.commit()
        

    # Action for loans table
    def add_loan(self, memberId, ISBN, loanDate, returnDate):
        self.cursor_object.execute('''INSERT INTO loans (memberId, ISBN, loanDate, returnDate) VALUES (?, ?, ?, ?)''', (memberId, ISBN, loanDate, returnDate))
        self.connection.commit()


    def get_loan(self, loanId):
        self.cursor_object.execute('''SELECT * FROM loans WHERE loanId = ?''', (loanId,))
        return self.cursor_object.fetchone()


    # def get_all_loans(self):
    #     self.cursor_object.execute('''SELECT * FROM loans''')
    #     return self.cursor_object.fetchall()

    def delete_loan(self, loanId):
        self.cursor_object.execute('''DELETE FROM loans WHERE loanId = ?''', (loanId,))
        self.connection.commit()

    # Action for reservation table
    def add_reservation(self, memberId, ISBN, reservationDate):
        self.cursor_object.execute('''INSERT INTO reservations (memberId, ISBN, reservationDate) VALUES (?, ?, ?)''', (memberId, ISBN, reservationDate))
        self.connection.commit()


    def get_reservation(self, reservationId):
        self.cursor_object.execute('''SELECT * FROM reservations WHERE reservationId = ?''', (reservationId,))
        return self.cursor_object.fetchone()


    # def get_all_reservations(self):
    #     self.cursor_object.execute('''SELECT * FROM reservations''')
    #     return self.cursor_object.fetchall()


    def delete_reservation(self, reservationId):
        self.cursor_object.execute('''DELETE FROM reservations WHERE reservationId = ?''', (reservationId,))
        self.connection.commit()

    # Action for fines table
    def add_fine(self, memberId, ISBN, fineAmount):
        self.cursor_object.execute('''INSERT INTO fines (memberId, ISBN, fineAmount) VALUES (?, ?, ?)''', (memberId, ISBN, fineAmount))
        self.connection.commit()


    def get_fine(self, fineId):
        self.cursor_object.execute('''SELECT * FROM fines WHERE fineId = ?''', (fineId,))
        return self.cursor_object.fetchone()


    # def get_all_fines(self):
    #     self.cursor_object.execute('''SELECT * FROM fines''')
    #     return self.cursor_object.fetchall()


    def delete_fine(self, fineId):
        self.cursor_object.execute('''DELETE FROM fines WHERE fineId = ?''', (fineId,))
        self.connection.commit()
            
            
if __name__ == "__main__":
    db = Query()
    print("Add member to database")
    db.add_member("admin", "admin", "Admin", "Big", "Admin Street 1")
    db.add_member("user", "user", "User", "Small", "User Street 2")
    print("Get member from database")
    print(db.get_login("admin"))
    print(db.get_member(1))
    print(db.get_member(2))
    print(db.get_login("user"))


    # print("Add book to database")
    # db.add_book("1234567890123", "Title", "Author", "Publication")
    # print("Boot from database")
    # print(db.get_book("1234567890123"))
    # db.add_book("2234567890123", "Title", "Author", "Publication")
    # print("All books from database")
    # print(db.get_all_books())
    # print("Delete book from database")
    # db.delete_book("1234567890123")
    # print(db.get_all_books())
    # print("Update book in database")
    # db.add_book("1234567890123", "Title", "Author", "Publication")
    # db.update_book("1234567890123", "New Title", "New Author", "New Publication")
    # print(db.get_book("1234567890123"))


    # print("Add loan to database")
    # db.add_loan(1, "1234567890123", "2020-01-01", "2020-01-15")
    # print(db.get_loan(1))
    # print(db.get_all_loans())
    # db.delete_loan(1)
    # print(db.get_all_loans())
    # db.add_loan(1, "1234567890123", "2020-01-01", "2020-01-15")
    # db.add_reservation(1, "1234567890123", "2020-01-01")
    # print(db.get_reservation(1))
    # print(db.get_all_reservations())
    # db.delete_reservation(1)
    # print(db.get_all_reservations())
    # db.add_fine(1, "1234567890123", 10)
    # print(db.get_fine(1))
    # print(db.get_all_fines())
    # db.delete_fine(1)
    # print(db.get_all_fines())
    db.close_connection()