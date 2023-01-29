from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class RemoveFine(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please, fill in all information about fine. ")
        self.fine_id_label = QLabel("Fine ID:")
        self.fine_id_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.fine_id_label, self.fine_id_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)


    def submit_clicked(self):
        fine_id = self.fine_id_edit.text()
        if fine_id and self.database.get_fine(fine_id) != None:
            self.database.delete_fine(fine_id)
            self.message_label.setText("Fine deleted from database.")
        else:
            self.message_label.setText("Couldn't delete fine.")