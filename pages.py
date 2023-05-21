from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QTextEdit, QComboBox, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import QDateTime, Qt, QTimer
from styles import Styles
from modules import InfectedDevice
import datetime

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.victims = {}

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
        self.filter_button.pressed.connect(self.do_filter)
        self.clear_filter_button = QPushButton("Отчистить")
        self.clear_filter_button.setFixedSize(200, 40)
        self.clear_filter_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.clear_filter_button.pressed.connect(self.clear_filter)
        
        
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

    def add_to_list(self, victim: InfectedDevice):
        if victim.name not in self.victims:
            label = f"{victim.name} | {victim.method} | {victim.ip} | {victim.country} | {'Online' if victim.status == True else f'Last online: {victim.last_online}'}"
            self.victims[victim.name] = (victim, label)
            self.update_list()
        
    def update_list(self, f=True):
        if f:
            self.type.clear()
            self.country.clear()
            self.status.clear()
            self.search_string.setText("Поиск...")
            self.type.addItem("Тип вируса")
            self.country.addItem("Страна")
            self.status.addItem("Статус")
        self.list_victims.clear()
        for i in self.victims:
            victim = self.victims[i]
            info = victim[0]
            device = victim[1]
            self.list_victims.addItem(device)
            if f:
                self.type.addItem(info.method)
                self.country.addItem(info.country)
                self.status.addItem("Online" if info.status == True else "Offline")

    def clear_filter(self):
        self.update_list()

    def do_filter(self):
        self.update_list(False)
        k = 0
        for i in range(self.list_victims.count()):
            device = self.list_victims.item(i - k).text().split(" | ")
            print(device)
            if self.search_string.toPlainText() != "Поиск...":
                if self.search_string.toPlainText() not in device[0]:
                    s = self.list_victims.takeItem(i - k)
                    del s
                    k += 1
                    continue
            if self.type.currentText() != "Тип вируса":
                if self.type.currentText() != device[1]:
                    s = self.list_victims.takeItem(i - k)
                    del s
                    k += 1
                    continue
            if self.country.currentText() != "Страна":
                if self.country.currentText() != device[3]:
                    s = self.list_victims.takeItem(i - k)
                    del s
                    k += 1
                    continue
            if self.status.currentText() != "Статус":
                if self.status.currentText() == "Online":
                    if self.status.currentText() != device[-1]:
                        s = self.list_victims.takeItem(i - k)
                        del s
                        k += 1
                        continue
                else:
                    if device[-1] == "Online":
                        s = self.list_victims.takeItem(i - k)
                        del s
                        k += 1
                        continue
        k = 0