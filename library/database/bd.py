import sqlite3

class Database:
    def __init__(self):
        # Create database
        self.connection = sqlite3.connect("library.db")
        # Create a cursor object 
        cursor_object = connection.cursor()
        
        # Add table
        self.create_tables()

        
        
    def create_tables(self): 
        # Create the users table 
        cursor_object.execute('''CREATE TABLE users \\
                              (id INTEGER PRIMARY KEY, name TEXT, password TEXT)''')
        
        # Commit the changes and close the connection 
        connection.commit()
        # connection.close()