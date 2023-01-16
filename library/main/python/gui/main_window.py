from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QErrorMessage
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from library.main.python.gui import login, librarian_widget, user_widget
from library.main.python.database import query

class MainWindow(QMainWindow):
    
    user_type = ""
        
    def __init__(self):
        super().__init__()
        self.library_database = query.Query()
        self.initUI()


    def initUI(self):
        # Create background
        self.label = QLabel()
        self.pixmap = QPixmap("./library/main/resources/main_background.jpg")
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())
        
        # Create a librarian button
        self.librarian_button = QPushButton("Librarian", self)
        self.librarian_icon = QIcon("./library/main/resources/librarian.png")
        self.librarian_button.setIcon(self.librarian_icon)
        self.librarian_button.clicked.connect(self.set_librarian)
        self.librarian_button.clicked.connect(self.show_login_form)

        # Create a user button
        self.user_button = QPushButton("User", self)
        self.user_icon = QIcon("./library/main/resources/user.png")
        self.user_button.setIcon(self.user_icon)
        self.user_button.clicked.connect(self.set_user)
        self.user_button.clicked.connect(self.show_login_form)
        
        # Create description 
        self.description = QLabel('''Welcome to library system.\nIn the first step please select your role.''', self)
        self.description.setAlignment(Qt.AlignCenter)
    
        # Add widget 
        layout = QVBoxLayout()
        layout.addWidget(self.librarian_button)
        layout.addWidget(self.user_button)
        layout.addWidget(self.description)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(widget)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Library System")
        self.show()
        
        self.login = login.Login(self.library_database)
        self.login.correct_credentials.connect(self.show_main_widget)
        self.login.incorrect_credentials.connect(self.show_error_message)

        
    def show_main_widget(self):
        self.setCentralWidget(QWidget())
        self.main_layout = QVBoxLayout()
        if self.user_type == "Librarian":
            self.librarian_widget = librarian_widget.LibrarianWidget(self.library_database)
            self.main_layout.addWidget(self.librarian_widget)
        else:
            self.user = user_widget.User()
            self.main_layout.addWidget(self.user)
        self.centralWidget().setLayout(self.main_layout)

        
    def show_error_message(self):
        error_message = QErrorMessage()
        error_message.showMessage("Incorrect credentials")
        
    def show_login_form(self):
        self.setCentralWidget(self.login)
        
    def set_librarian(self):
        self.user_type = "Librarian"
        
    def set_user(self):
        self.user_type = "User"