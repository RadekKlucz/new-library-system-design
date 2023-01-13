from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QPixmap

class User(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Member buttons (itself details)
        self.get_member_details_button = QPushButton("Get Member Details")
        
        # Book buttons
        self.find_book_button = QPushButton("Find Book")
        # self.update_book_button = QPushButton("Update Book")
        
        # Loan buttons 
        self.add_loan_button = QPushButton("Add loan")
        self.remove_loan_button = QPushButton("Remove loan")
        self.find_loan_button = QPushButton("Find loan")
        
        # Fine buttons
        self.find_fine_button = QPushButton("Find Fine")
        
        # Information label 
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        
        # Create new frame for information label
        self.frame = QFrame()
        self.frame.setFrameStyle(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.frame.setStyleSheet("background-color:white;")
        
        self.layout_frame = QVBoxLayout()
        self.layout_frame.addWidget(self.info_label)
        self.frame.setLayout(self.layout_frame)
        
        # Add widgets to the layout
        self.layout.addWidget(self.frame)
        self.layout.addStretch()
        self.layout.addWidget(self.get_member_details_button)
        self.layout.addWidget(self.find_book_button)
        self.layout.addWidget(self.add_loan_button)
        self.layout.addWidget(self.remove_loan_button)
        self.layout.addWidget(self.find_loan_button)
        self.layout.addWidget(self.find_fine_button)
        self.setLayout(self.layout)
        