from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame

class RemoveBook(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please, fill in book's ISBN. ")
        self.isbn_label = QLabel("ISBN:")
        self.isbn_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label = QLabel()
        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.isbn_label, self.isbn_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label)
        self.setLayout(layout)

    def submit_clicked(self):
        ibsn = self.isbn_edit.text()
        if ibsn and self.database.delete_book(ibsn):
            self.message_label.setText("Book deleted from database.")
        else:
            self.message_label.setText("Couldn't delete book.")