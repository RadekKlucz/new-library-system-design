from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QObject


class Login(QWidget): 

    correct_credentials = pyqtSignal()
    incorrect_credentials = pyqtSignal()
    
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create the credentials' background
        
        self.label = QLabel(self)
        self.background_pixmap = QPixmap("./library/gui/resources/second_background.jpg")
        self.label.setPixmap(self.background_pixmap)
        self.label.setGeometry(0, 0, self.frameGeometry().width(), self.frameGeometry().height())
        self.label.setAlignment(Qt.AlignCenter)
        
        # Create the credensials' environment
        self.main_layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/gui/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.check_credentials)
        self.form_layout = QFormLayout()
        self.form_layout.addRow("Username", self.username_input)
        self.form_layout.addRow("Password", self.password_input)
        self.form_layout.addRow(self.submit_button)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.label)
        self.setLayout(self.main_layout)
        
        
             
             
    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()
        result = self.database.get_login(username, password)
        if result:
            self.correct_credentials.emit()
        else:
            self.incorrect_credentials.emit()