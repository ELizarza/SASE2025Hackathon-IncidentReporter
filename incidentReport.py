from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, QWidget
from PySide6.QtGui import QPixmap

from selectionWidget import incidentSummary

class incidentReportDialog(QDialog):
    def __init__(self, parent=None, pixmap: QPixmap = None, summary: incidentSummary = None):
        super().__init__(parent)
        # print("yes")
        self.setWindowTitle("Incident Report")
        self.setModal(True)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)

        self.Dialoglayout = QHBoxLayout(self)

        w = 800
        h = 640
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
        
        widget = QWidget()
        widget.setLayout(self.info_layout)
        self.Dialoglayout.addWidget(widget)
