from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from library.gui.add_member_widget import AddMemberWidget
from library.gui.get_member_details_widget import GetMember


class LibrarianWidget(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        # Create a new layout for the Librarian 
        self.layout = QVBoxLayout()
        
        # Member buttons
        self.add_member_button = QPushButton("Add Member")
        self.remove_member_button = QPushButton("Remove Member")
        self.get_member_details_button = QPushButton("Get Member Details")
        # self.get_all_members_button = QPushButton("Get All Members") 
        
        # Book buttons
        self.add_book_button = QPushButton("Add Book")
        self.remove_book_button = QPushButton("Remove Book")
        self.find_book_button = QPushButton("Find Book")
        # self.update_book_button = QPushButton("Update Book")
        
        # Loan buttons 
        self.add_loan_button = QPushButton("Add loan")
        self.remove_loan_button = QPushButton("Remove loan")
        self.find_loan_button = QPushButton("Find loan")
        
        # Fine buttons
        self.add_fine_button = QPushButton("Add Fine")
        self.remove_fine_button = QPushButton("Remove Fine")
        self.find_fine_button = QPushButton("Find Fine")
        
        # # Create new frame for information label
        # self.frame = QFrame()
        # self.frame.setFrameStyle(QFrame.StyledPanel)
        # self.frame.setFrameShadow(QFrame.Raised)
        # self.frame.setLineWidth(2)
        # self.frame.setMidLineWidth(2)
        # self.frame.setStyleSheet("background-color:white;")
        
        # self.layout_frame = QVBoxLayout()
        # self.layout_frame.addWidget(self.info_label)
        # self.frame.setLayout(self.layout_frame)
        
        # Add widgets to the layout
        # Zamiast frame dodac jakies zdjecie do tla a to w nastepnym oknie
        self.layout.addWidget(self.add_member_button)
        self.layout.addWidget(self.remove_member_button)
        self.layout.addWidget(self.get_member_details_button)
        self.layout.addWidget(self.add_book_button)
        self.layout.addWidget(self.remove_book_button)
        self.layout.addWidget(self.find_book_button)
        self.layout.addWidget(self.add_loan_button)
        self.layout.addWidget(self.remove_loan_button)
        self.layout.addWidget(self.find_loan_button)
        self.layout.addWidget(self.add_fine_button)
        self.layout.addWidget(self.remove_fine_button)
        self.layout.addWidget(self.find_fine_button)
        self.setLayout(self.layout)
        
        # self.remove_book_button.clicked.connect(self.remove_book_action)
        self.add_member_button.clicked.connect(self.show_add_member_widget)
        self.get_member_details_button.clicked.connect(self.show_member_details)
        # self.find_book_button.clicked.connect(self.find_book_action)
        # dodac akcje dla każdego przycisku 
    
         # Information label 
        # self.info_label = QLabel()
        # self.info_label.setWordWrap(True)
        
        # self.layout = QFormLayout()
        # self.layout.addWidget(self.frame)
        # self.layout.addStretch()
        
    def show_add_member_widget(self):
        self.add_member_widget = AddMemberWidget(self.database)
        self.layout.addWidget(self.add_member_widget)
        self.setLayout(self.layout)

        # self.setCentralWidget(self.add_member_widget)
        
    def show_member_details(self):
        self.get_member_details_widget = GetMember(self.database)
        self.layout.addWidget(self.get_member_details_widget)
        self.setLayout(self.layout)
    
    
    
    def find_book_action(self):
        # remove book action here
        pass
        