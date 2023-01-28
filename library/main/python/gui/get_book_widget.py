from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QVBoxLayout, QFrame


class GetBook(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        
        # Create a new fields widget
        self.description = QLabel("Please fill in book's ISBN:")
        self.isbn_label = QLabel("ISBN:")
        self.isbn_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_clicked)
        self.message_label_1 = QLabel()
        self.message_label_2 = QLabel()
        self.message_label_3 = QLabel()
        self.message_label_4 = QLabel()

        layout = QFormLayout()
        layout.addRow(self.description)
        layout.addRow(self.isbn_label, self.isbn_edit)
        layout.addRow(self.submit_button)
        layout.addRow(self.message_label_1)
        layout.addRow(self.message_label_2)
        layout.addRow(self.message_label_3)
        layout.addRow(self.message_label_4)
        self.setLayout(layout)
        
    def submit_clicked(self):
        isbn = self.isbn_edit.text()
        data = self.database.get_book(isbn)
        if data != None:
            
            self.message_label_1.setText("IBSN: " + str(data["ISBN"]))
            self.message_label_2.setText("Title: " + data["Title"])
            self.message_label_3.setText("Author: " + data["Author"])
            self.message_label_4.setText("Publication: " + data["Publication"])
        else:
            self.message_label_1.setText("Couldn't find book.")
            self.message_label_2.setText("")
            self.message_label_3.setText("")
            self.message_label_4.setText("")
            