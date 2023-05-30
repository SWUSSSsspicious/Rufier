from PyQt5.QtCore import Qt, QTime, QTimer, QLocale
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QListWidget, QLineEdit)
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from inst import *
from final_win import *
class Expiriment():
    def __init__(self, age, test1, test2, test3):
        self.age=age
        self.tes1=test1
        self.tes2=test2
        self.tes3=test3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def next_click(self):
        self.hide()
        self.exp=Expiriment(int(self.age_ent.text()),self.f_test_res.text(), self.sec_test_res.text(), self.last_test_res.text())
        self.tw=FinalWin(self.exp)
    def connects(self):
        self.next_wind.clicked.connect(self.next_click)
        self.first_test.clicked.connect(self.timer_test)
        self.sec_test.clicked.connect(self.timer_sits)
        self.fin_test.clicked.connect(self.timer_final)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_hight)
        self.move(win_x,win_y)
    def initUI(self):
        self.first_test=QPushButton(txt_first_test, self)
        self.sec_test=QPushButton(txt_timer_start, self)
        self.fin_test=QPushButton(txt_final_text,self)
        self.next_wind=QPushButton(txt_sec_wind, self)
        
        self.name=QLabel(txt_name)
        self.age=QLabel(txt_age)
        self.first_t=QLabel(txt_first_test_inst)
        self.sec_t=QLabel(txt_sec_test_inst)
        self.final_t=QLabel(txt_last_test_inst)
        self.text_timer=QLabel(txt_timer)
        self.text_timer.setFont(QFont('Times', 36, QFont.Bo
