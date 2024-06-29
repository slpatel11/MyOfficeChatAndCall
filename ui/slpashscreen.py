
import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QSplashScreen, QVBoxLayout, QLabel

class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setGeometry(300, 200, 400, 300)
        layout = QVBoxLayout()
        self.label = QLabel('Your Application Name', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def showEvent(self, event):
        QTimer.singleShot(3000, self.close)
