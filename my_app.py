from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QListWidget, QLineEdit)
from inst import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.hello_text=QLabel(txt_hello)
        self.instract=QLabel(txt_instruct)
        self.btn_next=QPushButton(txt_next, self)
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.hello_text,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instract, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw=TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_hight)
        self.move(win_x,win_y)

app=QApplication([])
mv=MainWin()
app.exec_()
