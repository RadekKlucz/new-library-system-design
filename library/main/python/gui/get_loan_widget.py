from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class GetLoan(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please fill in information about loan:")
        self.isbn_label = QLabel("Loan ID:")
        self.isbn_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label_1 = QLabel()
        self.message_label_2 = QLabel()
        self.message_label_3 = QLabel()
        self.message_label_4 = QLabel()
        self.message_label_5 = QLabel()

        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.isbn_label, self.isbn_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label_1)
        layout.addRow(self.message_label_2)
        layout.addRow(self.message_label_3)
        layout.addRow(self.message_label_4)
        layout.addRow(self.message_label_5)
        self.setLayout(layout)
        
        
    def submit_clicked(self):
        isbn = self.isbn_edit.text()
        data = self.database.get_loan(isbn)
        if data != None: 
            self.message_label_1.setText("Loan ID: " + str(data["loanId"]))
            self.message_label_2.setText("Member ID: " + str(data["memberId"]))
            self.message_label_3.setText("ISBN: " + str(data["ISBN"]))
            self.message_label_4.setText("Loan date: " + str(data["loanDate"]))
            self.message_label_5.setText("Return date: " + str(data["returnDate"]))
        else:
            self.message_label_1.setText("Couldn't find loan.")
            self.message_label_2.setText("")
            self.message_label_3.setText("")
            self.message_label_4.setText("")   
            self.message_label_5.setText("")