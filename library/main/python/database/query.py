from library.main.python.database.database import Database

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
        
    def delete_member(self, login):        
        member_id = self.cursor_object.execute('''SELECT memberId FROM logins WHERE login=?''', (login,))
        member_id = member_id.fetchone()[0]
        if member_id:
            self.cursor_object.execute('''DELETE FROM logins WHERE login = ?''', (login,))
            self.cursor_object.execute('''DELETE FROM members WHERE memberId = ?''', (member_id,))
            self.connection.commit()
            return True
        else: 
            return False


    def get_member(self, login):
        data = self.cursor_object.execute('''SELECT members.memberId, members.name, members.surname, members.address FROM members 
                                   INNER JOIN logins ON members.memberId = logins.memberId WHERE logins.login = ?''', (login,))
        if data:
            result = data.fetchone()
            if result:
                column_names = [column[0] for column in data.description]
                return dict(zip(column_names, result))
        
        
    # Action for books table
    def add_book(self, ISBN, title, author, publication):
        self.cursor_object.execute('''INSERT INTO books (ISBN, Title, Author, Publication) VALUES (?, ?, ?, ?)''', (ISBN, title, author, publication))
        self.connection.commit()


    def get_book(self, ISBN):
        data = self.cursor_object.execute('''SELECT * FROM books WHERE ISBN = ?''', (ISBN,))
        if data:
            result = data.fetchone()
            if result:
                column_names = [column[0] for column in data.description]
                return dict(zip(column_names, result))
        

    def delete_book(self, ISBN):
        self.cursor_object.execute('''DELETE FROM books WHERE ISBN = ?''', (ISBN,))
        self.connection.commit()
   

    # Action for loans table
    def add_loan(self, memberId, ISBN, loanDate, returnDate):
        self.cursor_object.execute('''INSERT INTO loans (memberId, ISBN, loanDate, returnDate) VALUES (?, ?, ?, ?)''', (memberId, ISBN, loanDate, returnDate))
        self.connection.commit()


    def get_loan(self, loanId):
        data = self.cursor_object.execute('''SELECT * FROM loans WHERE loanId = ?''', (loanId,))
        if data:    
            result = data.fetchone()
            if result:
                column_names = [column[0] for column in data.description]
                return dict(zip(column_names, result))
                



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


    def delete_reservation(self, reservationId):
        self.cursor_object.execute('''DELETE FROM reservations WHERE reservationId = ?''', (reservationId,))
        self.connection.commit()

    # Action for fines table
    def add_fine(self, memberId, ISBN, fineAmount):
        self.cursor_object.execute('''INSERT INTO fines (memberId, ISBN, fineAmount) VALUES (?, ?, ?)''', (memberId, ISBN, fineAmount))
        self.connection.commit()


    def get_fine(self, fineId):
        data = self.cursor_object.execute('''SELECT * FROM fines WHERE fineId = ?''', (fineId,))
        if data:
            result = self.cursor_object.fetchone()
            if result:
                column_names = [column[0] for column in data.description]
                return dict(zip(column_names, result))                
        


    def delete_fine(self, fineId):
        self.cursor_object.execute('''DELETE FROM fines WHERE fineId = ?''', (fineId,))
        self.connection.commit()