import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from styles import Styles
from pages import MainWindow

class DeathSecApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window settings
        self.setWindowTitle("DeathSec")
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet(Styles.MAIN)
        # end

        # Setup GUI
        self.setCentralWidget(MainWindow())
       #end


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeathSecApp()
    window.show()
    sys.exit(app.exec_())
