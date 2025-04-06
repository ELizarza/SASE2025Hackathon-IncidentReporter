from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDialog, QMainWindow
from PySide6.QtGui import QPixmap, QFont

class incidentSelect(QWidget):
    def __init__(self):
        super().__init__()

        self.list_layout = QVBoxLayout()
        self.list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # self.incident_details = incidentItem()
        # self.list_layout.addWidget(self.incident_details)
        
        self.setLayout(self.list_layout)

class incidentSummary():
    def __init__(self):
        self.incSummary: str = "This is a sample summary, it will include information about the report here. a lot of things could go her\nlike more words or something\nI like words"
        self.typeOfIncident: str = "!"
        self.additionalInfo: str = "Additional Info: "
        self.suggestedAction: str = ""

class incidentItem(QWidget):
    buttonSignal = Signal(QMainWindow, QPixmap, incidentSummary)
    def __init__(self, parent, imagepath, date: QDate, summary: incidentSummary):
        super().__init__()

        self.mainWindow = parent
        self.info_layout = QHBoxLayout()

        self.image_preview = QLabel()
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignLeft)
        w = 240
        h = 400
        self.preview_pixmap = QPixmap(imagepath)
        self.image_preview.setPixmap(self.preview_pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio))
        self.info_layout.addWidget(self.image_preview)

        # self.date = "1/1/1999"
        self.info = QLabel(date.toString())
        self.info.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.date_font = QFont()
        self.date_font.setPointSize(24)
        self.info.setFont(self.date_font)
        self.info_layout.addWidget(self.info)

        self.setStyleSheet("background-color: LightGrey; padding: 12px;")

        self.setLayout(self.info_layout)

        self.summaryInfo = summary

    def setImage(self, pixmap: QPixmap):
        w = 240
        h = 400
        self.preview_pixmap = pixmap
        self.image_preview.setPixmap(self.preview_pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio))

    def mousePressEvent(self, event):
        # print(event)
        if event.button() is Qt.MouseButton.LeftButton:
            self.buttonSignal.emit(self, self.preview_pixmap, self.summaryInfo)
        return super().mousePressEvent(event)
    
