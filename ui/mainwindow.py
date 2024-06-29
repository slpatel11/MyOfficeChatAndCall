from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import QTimer, Qt
from ui.slpashscreen import SplashScreen
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        # self.setGeometry(100, 100, 400, 300)
        self.central_widget = QLabel('This is the main window', self)
        self.setCentralWidget(self.central_widget)

