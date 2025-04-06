from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout

class incidentReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # print("yes")
        self.setWindowTitle("Incident Report")
        self.setModal(True)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)

        
        self.layout = QVBoxLayout(self)
