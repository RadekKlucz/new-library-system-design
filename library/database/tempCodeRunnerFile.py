       # # Create the books table                            
        # self.cursor_object.execute("""CREATE TABLE IF NOT EXISTS books (
        #                         ISBN TEXT PRIMARY KEY,
        #                         Title TEXT NOT NULL,
        #                         Author TEXT NOT NULL,
        #                         Publication TEXT NOT NULL
        #                     )
        #                     """)

        # # Create the loans table
        # self.cursor_object.execute("""CREATE TABLE IF NOT EXISTS loans (
        #                                 loanId INTEGER PRIMARY KEY,
        #                                 memberId INTEGER NOT NULL,
        #                                 ISBN TEXT NOT NULL,
        #                                 loanDate TEXT NOT NULL,
        #                                 returnDate TEXT NOT NULL,
        #                                 FOREIGN KEY (memberId) REFERENCES members (memberId),
        #                                 FOREIGN KEY (ISBN) REFERENCES books (ISBN)
        #                             )
        #                             """)