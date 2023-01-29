from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class GetFine(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please fill in fine ID:")
        self.fine_id_label = QLabel("Fine ID:")
        self.fine_id_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label_1 = QLabel()
        self.message_label_2 = QLabel()
        self.message_label_3 = QLabel()
        self.message_label_4 = QLabel()

        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.fine_id_label, self.fine_id_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label_1)
        layout.addRow(self.message_label_2)
        layout.addRow(self.message_label_3)
        layout.addRow(self.message_label_4)
        self.setLayout(layout)
        
        
    def submit_clicked(self):
        fine_id = self.fine_id_edit.text()
        data = self.database.get_fine(fine_id)
        if data != None:
            self.message_label_1.setText("Fine ID: " + str(data["fineId"]))
            self.message_label_2.setText("Member ID: " + str(data["memberId"]))
            self.message_label_3.setText("ISBN: " + str(data["ISBN"]))
            self.message_label_4.setText("Fine amount: " + str(data["fineAmount"]))
        else:
            self.message_label_1.setText("Couldn't find fine.")
            self.message_label_2.setText("")
            self.message_label_3.setText("")
            self.message_label_4.setText("")
            