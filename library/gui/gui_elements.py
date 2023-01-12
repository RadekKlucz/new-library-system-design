from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit


class GuiElements(QWidget):
    def __init__(self):
        super().__init__()      
      
    def login_panel(self):
        self.username_field = QLineEdit()
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)
        
        login_fields_layout = QFormLayout()
        login_fields_layout.addRow(QLabel("Username:"), self.username_field)
        login_fields_layout.addRow(QLabel("Password:"), self.password_field)

        return login_fields_layout   
        