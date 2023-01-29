from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class RemoveLoan(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please, fill in all information about loan. ")
        self.loan_id_label = QLabel("Loan ID:")
        self.loan_id_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.loan_id_label, self.loan_id_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)


    def submit_clicked(self):
        loan_id = self.loan_id_edit.text()
        if loan_id and self.database.get_loan(loan_id) != None:
            self.database.delete_loan(loan_id)
            self.message_label.setText("Loan deleted from database.")
        else:
            self.message_label.setText("Couldn't delete loan.")   