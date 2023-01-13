from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

class LibrarianWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        # Member buttons
        self.add_member_button = QPushButton("Add Member")
        self.remove_member_button = QPushButton("Remove Member")
        self.get_member_details_button = QPushButton("Get Member Details")
        # self.get_all_members_button = QPushButton("Get All Members") 
        
        # Book buttons
        self.add_book_button = QPushButton("Add Book")
        self.remove_book_button = QPushButton("Remove Book")
        self.find_book_button = QPushButton("Find Book")
        # self.update_book_button = QPushButton("Update Book")
        
        # Loan buttons 
        self.add_loan_button = QPushButton("Add loan")
        self.remove_loan_button = QPushButton("Remove loan")
        self.find_loan_button = QPushButton("Find loan")
        
        # Fine buttons
        self.add_fine_button = QPushButton("Add Fine")
        self.remove_fine_button = QPushButton("Remove Fine")
        self.find_fine_button = QPushButton("Find Fine")
        
        self.layout.addWidget(self.add_member_button)
        self.layout.addWidget(self.remove_member_button)
        self.layout.addWidget(self.get_member_details_button)
        self.layout.addWidget(self.add_book_button)
        self.layout.addWidget(self.remove_book_button)
        self.layout.addWidget(self.find_book_button)
        self.layout.addWidget(self.add_loan_button)
        self.layout.addWidget(self.remove_loan_button)
        self.layout.addWidget(self.find_loan_button)
        self.layout.addWidget(self.add_fine_button)
        self.layout.addWidget(self.remove_fine_button)
        self.layout.addWidget(self.find_fine_button)
        self.setLayout(self.layout)
        
        # self.remove_book_button.clicked.connect(self.remove_book_action)
        self.add_book_button.clicked.connect(self.add_book_action)
        self.find_book_button.clicked.connect(self.find_book_action)
        
    def add_book_action(self):
        # add book action here
        pass
    def find_book_action(self):
        # remove book action here
        pass

        
        
        
        
        
        