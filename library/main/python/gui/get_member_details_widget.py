from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class GetMember(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please fill in member's login: ")
        self.login_label = QLabel("Login:")
        self.login_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label_1 = QLabel()
        self.message_label_2 = QLabel()
        self.message_label_3 = QLabel()
        self.message_label_4 = QLabel()
        
        # Set up a new layout 
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.login_label, self.login_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label_1)
        layout.addRow(self.message_label_2)
        layout.addRow(self.message_label_3)
        layout.addRow(self.message_label_4)
        self.setLayout(layout)
        
        
    def submit_clicked(self):
        login = self.login_edit.text()
        data = self.database.get_member(login)
        if data != None:
            self.message_label_1.setText("Member ID: " + str(data["memberId"]))
            self.message_label_2.setText("Name: " + data["name"])
            self.message_label_3.setText("Surname: " + data["surname"])
            self.message_label_4.setText("Address: " + data["address"])
        else:
            self.message_label_1.setText("Couldn't find member.")
            self.message_label_2.setText("")
            self.message_label_3.setText("")
            self.message_label_4.setText("")