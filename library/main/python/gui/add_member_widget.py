from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class AddMemberWidget(QWidget):
    def __init__(self, database):
        self.database = database
        super().__init__()
        
        # Create a new fields widget
        self.description = QLabel("Please feel in information about new member: ")
        self.login_label = QLabel("Set Login:")
        self.login_edit = QLineEdit()
        self.password_label = QLabel("Set Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.surname_label = QLabel("Surname:")
        self.surname_edit = QLineEdit()
        self.address_label = QLabel("Address:")
        self.address_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.login_label, self.login_edit)
        layout.addRow(self.password_label, self.password_edit)
        layout.addRow(self.name_label, self.name_edit)
        layout.addRow(self.surname_label, self.surname_edit)
        layout.addRow(self.address_label, self.address_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)
        
        
    def submit_clicked(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        name = self.name_edit.text()
        surname = self.surname_edit.text()
        address = self.address_edit.text()
        if login and password and name and surname and address:
            self.database.add_member(login, password, name, surname, address)
            print(self.database.get_member(2))
            self.message_label.setText("Data submitted successfully.")
        else:
            self.message_label.setText("Please fill in all fields.")