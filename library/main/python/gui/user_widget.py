from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from library.main.python.gui.get_book_widget import GetBook
from library.main.python.gui.add_load_widget import AddLoan
from library.main.python.gui.get_loan_widget import GetLoan
from library.main.python.gui.remove_loan_widget import RemoveLoan
from library.main.python.gui.get_fine_widget import GetFine


class User(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        # Create a new layout for the user 
        self.layout = QVBoxLayout()
        
        # Create a new frame for the user to display a data and buttons
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)
        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)
        
        # Book buttons
        self.find_book_button = QPushButton("Find Book")
                
        # Loan buttons 
        self.add_loan_button = QPushButton("Add loan")
        self.remove_loan_button = QPushButton("Remove loan")
        self.find_loan_button = QPushButton("Find loan")
        
        # Fine buttons
        self.find_fine_button = QPushButton("Find Fine")
        
        # Add widgets to the layout
        self.layout.addWidget(self.find_book_button)
        self.layout.addWidget(self.add_loan_button)
        self.layout.addWidget(self.remove_loan_button)
        self.layout.addWidget(self.find_loan_button)
        self.layout.addWidget(self.find_fine_button)
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)
        
        # Set up the action for the buttons
        self.find_book_button.clicked.connect(self.find_book_widgets)
        self.add_loan_button.clicked.connect(self.add_loan_widgets)
        self.remove_loan_button.clicked.connect(self.remove_loan_widgets)
        self.find_loan_button.clicked.connect(self.get_loan_widgets)
        self.find_fine_button.clicked.connect(self.get_fine_widgets)
    
    
    def find_book_widgets(self):
        self.find_book_widget = GetBook(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.find_book_widget)
        self.setLayout(self.layout)
        
        
    def add_loan_widgets(self):
        self.add_loan_widget = AddLoan(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.add_loan_widget)
        self.setLayout(self.layout)
        
        
    def get_loan_widgets(self):
        self.get_loan_widget = GetLoan(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.get_loan_widget)
        self.setLayout(self.layout)
        
    
    def remove_loan_widgets(self):
        self.remove_loan_widget = RemoveLoan(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.remove_loan_widget)
        self.setLayout(self.layout)
        
        
    def get_fine_widgets(self):
        self.get_fine_widget = GetFine(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.get_fine_widget)
        self.setLayout(self.layout)
        
        
    def remove_widgets_from_frame(self):
        for i in reversed(range(self.frame_layout.count())):
            self.frame_layout.itemAt(i).widget().setParent(None)