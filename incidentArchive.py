from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, QWidget, QPushButton
from PySide6.QtGui import QPixmap

from selectionWidget import incidentSummary

class incidentArchiveDialog(QDialog):
    def __init__(self, parent=None, pixmap: QPixmap = None, summary: incidentSummary = None):
        super().__init__(parent)
        # print("yes")
        self.setWindowTitle("Incident Archive")
        self.setModal(True)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)

        self.Dialoglayout = QHBoxLayout(self)

        w = 600
        h = 600
        self.fullImage = QLabel()
        self.fullImage.setPixmap(pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio))
        self.Dialoglayout.addWidget(self.fullImage)

        self.info_layout = QVBoxLayout()

        self.eventSummary = QLabel(summary.incSummary)
        self.eventType =  QLabel(summary.typeOfIncident)
        self.eventDetails = QLabel(summary.additionalInfo)
        self.eventActionNeeded = QLabel(summary.suggestedAction)

        self.closeButton = QPushButton("close")
        self.closeButton.clicked.connect(self.closeButtonEvent)

        self.info_layout.addWidget(self.eventSummary, 30)
        self.info_layout.addWidget(self.eventType, 30)
        self.info_layout.addWidget(self.eventDetails, 30)
        self.info_layout.addWidget(self.eventActionNeeded, 30)
        self.info_layout.addWidget(self.closeButton)
        
        widget = QWidget()
        widget.setLayout(self.info_layout)
        self.Dialoglayout.addWidget(widget)

    def closeButtonEvent(self):
        self.reject() 
