import sys
from PySide6.QtWidgets import QApplication
from ui.mainwindow import MainWindow
from ui.slpashscreen import SplashScreen
from PySide6.QtCore import Qt, QTimer




def main():
    app = QApplication(sys.argv)
    screen_geometry=app.primaryScreen().availableGeometry()
    
    main_window = MainWindow()
    main_window.setGeometry(screen_geometry)
    main_window.show()
  

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
