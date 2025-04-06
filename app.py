from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow, QScrollArea, QGridLayout, QLabel
from PySide6.QtGui import QPalette

from selectionWidget import incidentSelect, incidentItem, incidentSummary
from incidentReport import incidentReportDialog
from incidentArchive import incidentArchiveDialog

class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle("Advanced Image Analysis Platform")
        #setGeometry: first 2 arguements define where on the screen the window will appear and the other 2 args are the width and height
        self.setGeometry(100, 100, 1800, 900)
        # Setting things as instance variables (self.thing) allows them to be accessed from other methods.
        self.incidentWindow = incidentSelect()
        self.archiveWindow = incidentSelect()
        # self.dummyItem = incidentItem(self)
        # self.incidentWindow.list_layout.addWidget(self.dummyItem)
        self.addIncident(self)
        self.addIncidentArchive(self)

        self.incidentReviewLabel = QLabel("Incidents Pending Review")

        self.listView = QScrollArea()
        self.listView.setWidgetResizable(True)
        self.listView.setStyleSheet("background-color: LightGray;")
        self.listView.setWidget(self.incidentWindow)

        self.incidentArchiveLabel = QLabel("Incident Archive")

        self.listViewArchive = QScrollArea()
        self.listViewArchive.setWidgetResizable(True)
        self.listViewArchive.setStyleSheet("background-color: LightGray;")
        self.listViewArchive.setWidget(self.archiveWindow)

        self.grid = QGridLayout()
        self.grid.addWidget(self.incidentReviewLabel, 1, 1)
        self.grid.addWidget(self.incidentArchiveLabel, 1, 2)
        self.grid.addWidget(self.listView, 2, 1)
        self.grid.addWidget(self.listViewArchive, 2, 2)
        

        self.cenWidget = QWidget()
        self.cenWidget.setLayout(self.grid)
        #determines which widget gets the main window
        self.setCentralWidget(self.cenWidget)

    def addIncident(self, parent = None):
        newIncident = incidentItem(parent)
        self.incidentWindow.list_layout.addWidget(newIncident)
        newIncident.buttonSignal.connect(self.openIncidentReport)

    def addIncidentArchive(self, parent = None):
        newIncident = incidentItem(parent)
        self.archiveWindow.list_layout.addWidget(newIncident)
        newIncident.buttonSignal.connect(self.openIncidentArchive)

    def openIncidentReport(self, parent = None, pixmap=None, summary=None):
        newIncidentReport = incidentReportDialog(parent, pixmap, summary)
        newIncidentReport.show()

    def openIncidentArchive(self, parent = None, pixmap=None, summary=None):
        newIncidentReport = incidentArchiveDialog(parent, pixmap, summary)
        newIncidentReport.show()