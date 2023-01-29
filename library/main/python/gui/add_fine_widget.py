from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class AddFine(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please fill in all information about fine: ")
        self.member_login_label = QLabel("Member's login: ")
        self.member_login_edit = QLineEdit()
        self.isbn_label = QLabel("ISBN:")
        self.isbn_edit = QLineEdit()
        self.amount_label = QLabel("Amount:")
        self.amount_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.member_login_label, self.member_login_edit)
        layout.addRow(self.isbn_label, self.isbn_edit)
        layout.addRow(self.amount_label, self.amount_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)

    def submit_clicked(self):
        member_login = self.member_login_edit.text()
        member_data = self.database.get_member(member_login)
        if member_data != None:
            member_id = member_data["memberId"]
        else:
            member_id = None
        isbn = self.isbn_edit.text()
        amount = self.amount_edit.text()
        book_data = self.database.get_book(isbn)
        if member_id != None and isbn and amount and book_data != None:
            self.database.add_fine(member_id, isbn, amount)
            self.message_label.setText("Fine added to database.")
        else:
            self.message_label.setText("Please, feel in all correct information about fine.")