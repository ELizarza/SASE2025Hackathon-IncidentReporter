from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow

from selectionWidget import incidentSelect

class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle("Advanced Image Analysis Platform")
        #setGeometry: first 2 arguements define where on the screen the window will appear and the other 2 args are the width and height
        self.setGeometry(100, 100, 1800, 900)
        # Setting things as instance variables (self.thing) allows them to be accessed from other methods.
        self.incidentWindow = incidentSelect() 
        

        #creates widget and sets layout to popluate it
        # widget = QWidget()
        #determines which widget gets the main window
        self.setCentralWidget(self.incidentWindow)