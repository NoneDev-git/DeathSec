from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QTextEdit, QComboBox, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import QDateTime, Qt, QTimer
from styles import Styles
import datetime

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Layouts

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)

        self.port_setup_layout = QHBoxLayout()

        self.appbar_layout = QHBoxLayout()
        self.filter_layout = QVBoxLayout()
        self.filters_layout = QGridLayout()
        self.filter_buttons_layout = QHBoxLayout()

        self.victims_layout = QVBoxLayout()

        # end

        #Widgets
    
        self.menu_button = QPushButton("Меню")
        self.menu_button.setFixedSize(100, 40)
        self.menu_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.title = QLabel("Жертвы")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFixedSize(200, 40)
        self.time = QLabel(QDateTime.currentDateTime().toString().split()[3])
        self.time.setFixedHeight(40)
        self.time.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.port_input = QTextEdit("Порт...")
        self.port_input.setFixedSize(200, 40)
        self.port_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.port_acept = QPushButton("Применить")
        self.port_acept.setFixedSize(200, 40)

        self.search_string = QTextEdit("Поиск...")
        self.search_string.setFixedSize(400, 40)
        self.search_string.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.type = QComboBox()
        self.type.setFixedHeight(40)
        self.type.addItem("Тип вируса")
        self.country = QComboBox()
        self.country.setFixedHeight(40)
        self.country.addItem("Страна")
        self.status = QComboBox()
        self.status.setFixedHeight(40)
        self.status.addItem("Статус")
        self.filter_button = QPushButton("Фильтр")
        self.filter_button.setFixedSize(200, 40)
        self.filter_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.clear_filter_button = QPushButton("Отчистить")
        self.clear_filter_button.setFixedSize(200, 40)
        self.clear_filter_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        
        self.list_victims = QListWidget()

        #end

        #Build Interface

        self.appbar_layout.addWidget(self.menu_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.appbar_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.appbar_layout.addWidget(self.time, alignment=Qt.AlignmentFlag.AlignRight)
        self.main_layout.addLayout(self.appbar_layout)

        self.port_setup_layout.addWidget(self.port_input, alignment=Qt.AlignmentFlag.AlignRight)
        self.port_setup_layout.addWidget(self.port_acept, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addLayout(self.port_setup_layout)

        self.filters_layout.addWidget(self.search_string, 1, 0)
        self.filters_layout.addWidget(self.type, 1, 1)
        self.filters_layout.addWidget(self.country, 1, 2)
        self.filters_layout.addWidget(self.status, 1, 3)
        self.filter_layout.addLayout(self.filters_layout)
        self.filter_buttons_layout.addWidget(self.filter_button)
        self.filter_buttons_layout.addWidget(self.clear_filter_button)
        self.filter_layout.addLayout(self.filter_buttons_layout)
        self.main_layout.addLayout(self.filter_layout)


        self.victims_layout.addWidget(self.list_victims)
        self.main_layout.addLayout(self.victims_layout)


        self.setLayout(self.main_layout)
        #end

    def update_time(self):
        self.time.setText(QDateTime.currentDateTime().toString().split()[3])

    def add_to_list(self):
        pass