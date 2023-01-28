from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from datetime import datetime, timedelta

class AddLoan(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please feel in information about new loan: ")
        self.user_label = QLabel("User's ID:")
        self.user_edit = QLineEdit()
        self.isbn_label = QLabel("ISBN:")
        self.isbn_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.user_label, self.user_edit)
        layout.addRow(self.isbn_label, self.isbn_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)
        
        
    def submit_clicked(self):
        member_id = self.user_edit.text()
        isbn = self.isbn_edit.text()
        data_book = self.database.get_book(isbn)
        if member_id and isbn and data_book != None:
            current_date = datetime.now()
            return_date = current_date + timedelta(weeks=4)
            self.database.add_loan(member_id, isbn, current_date, return_date)
            self.message_label.setText("Loan submitted successfully.")

        else:
            self.message_label.setText("Please fill in all correct fields.")