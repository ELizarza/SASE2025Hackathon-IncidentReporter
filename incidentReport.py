from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, QWidget, QPushButton
from PySide6.QtGui import QPixmap

from selectionWidget import incidentSummary

class incidentReportDialog(QDialog):
    saved = Signal()
    deleted = Signal()
    def __init__(self, parent=None, pixmap: QPixmap = None, summary: incidentSummary = None):
        super().__init__(parent)
        # print("yes")
        self.setWindowTitle("Incident Report")
        self.setModal(True)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)

        self.Dialoglayout = QHBoxLayout(self)

        w = 600
        h = 600
        self.fullImage = QLabel()
        self.fullImage.setPixmap(pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio))
        self.Dialoglayout.addWidget(self.fullImage)

        self.info_layout = QVBoxLayout()

        self.eventSummary = QLabel(summary.summary)
        self.eventType =  QLabel(summary.typeOfIncident)
        self.eventDetails = QLineEdit()

        self.info_layout.addWidget(self.eventSummary)
        self.info_layout.addWidget(self.eventType)
        self.info_layout.addWidget(self.eventDetails)

        self.buttonLayout = QHBoxLayout()
        self.closeButton = QPushButton("Close")
        self.closeButton.clicked.connect(self.closeButtonEvent)
        self.saveButton = QPushButton("Save Report")
        self.saveButton.clicked.connect(self.SaveButtonEvent)
        self.deleteButton = QPushButton("Discard Report")
        self.deleteButton.clicked.connect(self.deleteButtonEvent)
        self.buttonLayout.addWidget(self.closeButton)
        self.buttonLayout.addWidget(self.saveButton)
        self.buttonLayout.addWidget(self.deleteButton)
        self.info_layout.addLayout(self.buttonLayout)
        
        widget = QWidget()
        widget.setLayout(self.info_layout)
        self.Dialoglayout.addWidget(widget)

        self.incidentSum: incidentSummary = summary

    def closeButtonEvent(self):
        self.reject()

    def SaveButtonEvent(self):
        self.incidentSum.additionalInfo = self.eventDetails.text()
        self.saved.emit() 
        self.accept() 

    def deleteButtonEvent(self):
        self.deleted.emit()
        self.reject() 
