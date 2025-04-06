from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QWidget, QMainWindow, QScrollArea, QGridLayout, QLabel, QMenuBar, QMenu
from PySide6.QtGui import QPalette, QAction

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
        # self.addIncident("overview.png", QDate.currentDate(), self)
        # self.testCases()
        # self.addIncidentArchive(self)

        self.incidentReviewLabel = QLabel("Incidents Pending Review")

        self.listView = QScrollArea()
        self.listView.setWidgetResizable(True)
        self.listView.setStyleSheet("background-color: Gray;")
        self.listView.setWidget(self.incidentWindow)

        self.incidentArchiveLabel = QLabel("Incident Archive")

        self.listViewArchive = QScrollArea()
        self.listViewArchive.setWidgetResizable(True)
        self.listViewArchive.setStyleSheet("background-color: Gray;")
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

        self.menu = QMenuBar()
        self.testMenu = QMenu("Test")
        self.test_action = QAction("Insert Incidents", self)
        self.test_action.triggered.connect(self.testCases)
        self.testMenu.addAction(self.test_action)

        self.menu.addMenu(self.testMenu)
        self.setMenuBar(self.menu)

    def addIncident(self, imagepath, date: QDate, summary: incidentSummary, parent = None):
        newIncident = incidentItem(parent, imagepath, date, summary)
        self.incidentWindow.list_layout.addWidget(newIncident)
        newIncident.buttonSignal.connect(self.openIncidentReport)

    def addIncidentArchive(self, incident: incidentItem):
        self.incidentWindow.list_layout.removeWidget(incident)
        self.archiveWindow.list_layout.addWidget(incident)
        incident.buttonSignal.disconnect()
        incident.buttonSignal.connect(self.openIncidentArchive)

    def deleteIncident(self, incident: incidentItem):
        self.incidentWindow.list_layout.removeWidget(incident)
        incident.buttonSignal.disconnect()
        incident.deleteLater()

    def openIncidentReport(self, parent = None, pixmap=None, summary=None):
        newIncidentReport = incidentReportDialog(parent, pixmap, summary)
        newIncidentReport.saved.connect(self.addIncidentArchive)
        newIncidentReport.deleted.connect(self.deleteIncident)
        newIncidentReport.show()

    def openIncidentArchive(self, parent = None, pixmap=None, summary=None):
        newIncidentReport = incidentArchiveDialog(parent, pixmap, summary)
        newIncidentReport.show()

    def testCases(self):
        image1 = "testIncidents/injury1.jpg"
        image2 = "testIncidents/injury2.jpg"
        image3 = "testIncidents/injury3.webp"
        # image4 = "testIncidents/injury4.png"
        self.addIncident(image1, QDate.currentDate(), self.generateSummary(image1), self)
        self.addIncident(image2, QDate.currentDate(), self.generateSummary(image2), self)
        self.addIncident(image3, QDate.currentDate(), self.generateSummary(image3), self)
        # self.addIncident(image4, QDate.currentDate(), self.generateSummary(image4), self)
        

    def generateSummary(self, imagepath: str) -> incidentSummary:
        image_summary = incidentSummary()
        if imagepath == "testIncidents/injury1.jpg":
            image_summary.typeOfIncident = "Injury Type: Sprain"
            image_summary.incSummary = "Summary: A scene in a factory or industrial setting where one worker appears to have sustained an injury,\nand another worker is assisting him while communicating on a walkie-talkie, likely calling for help."
            image_summary.suggestedAction = "Suggested Action: Both workers are wearing protective equipment such as hard hats, gloves, and safety vests,\nshowing adherence to safety protocols, although additional measures (e.g., better hazard awareness or machine guarding)\nmay be needed."

        if imagepath == "testIncidents/injury2.jpg":
            image_summary.typeOfIncident = "Injury Type: laceration or deep cut"
            image_summary.incSummary = "Summary: The worker appears to have accidentally injured himself with a handsaw, likely to the hand or fingers."
            image_summary.suggestedAction = "Suggested Action: Immediate attention is needed—this type of injury can lead to heavy bleeding and potential nerve or tendon damage."

        if imagepath == "testIncidents/injury3.webp":
            image_summary.typeOfIncident = "Injury Type: Fall"
            image_summary.incSummary = "Summary: A construction worker is seen lying on the floor in visible pain, clutching his knee. Possibly a fall from a ladder or elevated surface."
            image_summary.suggestedAction = "Suggested Action: Immediate assessment for joint or bone injury, and potentially calling emergency medical services if mobility is compromised."

        if imagepath == "testIncidents/injury4.png":
            image_summary.typeOfIncident = "Injury Type: Knee or leg injury"
            image_summary.incSummary = "Summary: A construction worker is lying on the floor in visible pain, holding his knee. Possible Cause is tripping over loose cords or equipment"
            image_summary.suggestedAction = "Suggested Action: Immediate first aid and assessment and Removal of trip hazards from the workspace and improved organization of tools and cables."

        return image_summary
