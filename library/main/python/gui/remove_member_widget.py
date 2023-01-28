from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame

class RemoveMember(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please fill in user's login: ")
        self.login_label = QLabel("Login:")
        self.login_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.login_label, self.login_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)

    def submit_clicked(self):
        login = self.login_edit.text()
        if login and self.database.delete_member(login):
            self.message_label.setText("User deleted from database.")
        else:
            self.message_label.setText("User does not exist.")
