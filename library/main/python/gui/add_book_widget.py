from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon

class AddBook(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Options for add book button: ")
        self.isbn_label = QLabel("ISBN:")
        self.isbn_edit = QLineEdit()
        self.title_label = QLabel("Title:")
        self.title_edit = QLineEdit()
        self.author_label = QLabel("Author:")
        self.author_edit = QLineEdit()
        self.publication_label = QLabel("Publication:")
        self.publication_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_icon = QIcon("./library/main/resources/submit-progress.png")
        self.submit_button.setIcon(self.submit_icon)
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.isbn_label, self.isbn_edit)
        layout.addRow(self.title_label, self.title_edit)
        layout.addRow(self.author_label, self.author_edit)
        layout.addRow(self.publication_label, self.publication_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)

    def submit_clicked(self):
        ibsn = self.isbn_edit.text()
        title = self.title_edit.text()
        author = self.author_edit.text()
        publication = self.publication_edit.text()
        if ibsn and title and author and publication:
            self.database.add_book(ibsn, title, author, publication)
            self.message_label.setText("Book added to database.")
        else:
            self.message_label.setText("Please, feel in all information about book.")