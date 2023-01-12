from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
# from library.database import bd
from library.gui import gui_elements as ge

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui_elements = ge.GuiElements()  
        self.initUI()
   

    def initUI(self):
        # Create a log in button
        self.login_button = QPushButton("Log in", self)
        self.login_button.clicked.connect(self.gui_elements.login_panel())

        # self.sigin_button = QPushButton("Sign in", self)
        # self.sigin_button.clicked.connect(self.gui_elements.sign_in_panel())
        
        # Create label 
        self.label = QLabel('''Welcome to library system.\nIn the first step please log in to system''', self)
        self.label.setFixedSize(300, 100)
        
        # Add widget 
        self.button.move(50, 50)
        self.label.move(50, 100)
        
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Main Window")
        self.show()