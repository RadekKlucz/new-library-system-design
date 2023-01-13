from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame


class GetMember(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.login_label = QLabel("Login:")
        self.login_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        layout = QFormLayout()
        layout.addRow(self.login_label, self.login_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)
        
    def submit_clicked(self):
        login = self.login_edit.text()
        if login:
            result = self.database.get_member(login)
            print(result)
            self.message_label.setText("Data submitted successfully.")
            self.message_label.setText(result)

        else:
            self.message_label.setText("Please fill in all fields.")