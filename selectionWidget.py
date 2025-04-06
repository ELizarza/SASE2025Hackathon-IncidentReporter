from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QFont

class incidentSelect(QWidget):
    def __init__(self):
        super().__init__()

        self.list_layout = QVBoxLayout()
        self.list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.incident_details = incidentItem()
        self.list_layout.addWidget(self.incident_details)
        
        self.setLayout(self.list_layout)

class incidentItem(QWidget):
    def __init__(self):
        super().__init__()

        self.info_layout = QHBoxLayout()

        self.image_preview = QLabel()
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        w = 240
        h = 400
        self.preview_pixmap = QPixmap("overview.png")
        self.image_preview.setPixmap(self.preview_pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio))
        self.info_layout.addWidget(self.image_preview)

        self.date = "1/1/1999"
        self.info = QLabel(self.date)
        self.info.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.date_font = QFont()
        self.date_font.setPointSize(24)
        self.info.setFont(self.date_font)
        self.info_layout.addWidget(self.info)

        self.setStyleSheet("background-color: grey; padding: 12px;")

        self.setLayout(self.info_layout)