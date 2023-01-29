from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QPixmap
from library.main.python.gui.add_member_widget import AddMemberWidget
from library.main.python.gui.get_member_details_widget import GetMember
from library.main.python.gui.remove_member_widget import RemoveMember
from library.main.python.gui.add_book_widget import AddBook
from library.main.python.gui.remove_book_widget import RemoveBook
from library.main.python.gui.get_book_widget import GetBook
from library.main.python.gui.add_load_widget import AddLoan
from library.main.python.gui.get_loan_widget import GetLoan
from library.main.python.gui.remove_loan_widget import RemoveLoan
from library.main.python.gui.add_fine_widget import AddFine
from library.main.python.gui.remove_fine_widget import RemoveFine
from library.main.python.gui.get_fine_widget import GetFine


class LibrarianWidget(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        # Create a new layout for the librarian 
        self.layout = QVBoxLayout()
        
        # Create a new frame for the Librarian to display a data and buttons
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)
        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)
                
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
        
        # Add widgets to the layout
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
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)
        
        # Set up actions for the buttons
        self.add_member_button.clicked.connect(self.show_add_member_widgets)
        self.get_member_details_button.clicked.connect(self.show_member_details_widgets)
        self.remove_member_button.clicked.connect(self.delete_user_widgets)
        self.add_book_button.clicked.connect(self.add_book_widgets)
        self.remove_book_button.clicked.connect(self.delete_book_widgets)
        self.find_book_button.clicked.connect(self.find_book_widgets)
        self.add_loan_button.clicked.connect(self.add_loan_widgets)
        self.find_loan_button.clicked.connect(self.get_loan_widgets)
        self.remove_loan_button.clicked.connect(self.remove_loan_widgets)
        self.add_fine_button.clicked.connect(self.add_fine_widgets)
        self.remove_fine_button.clicked.connect(self.remove_fine_widgets)
        self.find_fine_button.clicked.connect(self.get_fine_widgets)
        
    def show_add_member_widgets(self):
        self.add_member_widget = AddMemberWidget(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.add_member_widget)
        self.setLayout(self.layout)

        
    def show_member_details_widgets(self):
        self.get_member_details_widget = GetMember(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.get_member_details_widget)
        self.setLayout(self.layout)
        
    def delete_user_widgets(self):
        self.delete_member_widget = RemoveMember(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.delete_member_widget)
        self.setLayout(self.layout)
        
    def add_book_widgets(self):
        self.add_book_widget = AddBook(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.add_book_widget)
        self.setLayout(self.layout)
        
    def delete_book_widgets(self):
        self.remove_book_widget = RemoveBook(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.remove_book_widget)
        self.setLayout(self.layout)
    
    
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
        
    
    def add_fine_widgets(self):
        self.add_fine_widget = AddFine(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.add_fine_widget)
        self.setLayout(self.layout)
        
    def remove_fine_widgets(self):
        self.remove_fine_widget = RemoveFine(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.remove_fine_widget)
        self.setLayout(self.layout)
        
    def get_fine_widgets(self):
        self.get_fine_widget = GetFine(self.database)
        self.remove_widgets_from_frame()
        self.frame_layout.addWidget(self.get_fine_widget)
        self.setLayout(self.layout)
         
        
    def remove_widgets_from_frame(self):
        for i in reversed(range(self.frame_layout.count())):
            self.frame_layout.itemAt(i).widget().setParent(None)