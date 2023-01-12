from PyQt5 import QtWidgets, QtGui


class GuiElements(QtWidgets.QWidget):      
      
    def login_panel(self):
        self.username_label = QtWidgets.QLabel("Username:", self)
        self.username_field = QtWidgets.QLineEdit(self)
        
        self.login_fields_layout = QtWidgets.QVBoxLayout()
        self.login_fields_layout.addWidget(self.username_label)
        self.login_fields_layout.addWidget(self.username_field)
        return self.login_fields_layout   
        