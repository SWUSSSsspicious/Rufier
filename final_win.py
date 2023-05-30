from PyQt5.QtCore import Qt, QTime, QTimer, QLocale
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QListWidget, QLineEdit, QGridLayout)
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from inst import *
class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp=exp
        self.initUI()
        self.set_appear()
        self.show()
    def result(self):
        if self.exp.age<7:
            self.index=0
            return 'нет данных для такого возраста'
        self.index=(4*(int(self.exp.tes1)+int(self.exp.tes2)+int(self.exp.tes3))-200)/10
        if self.exp.age==7 or self.exp.age==8:
            if self.index>=21:
                return txt_res1
            elif self.index<21 and self.index>=17:
                return txt_res2
            elif self.index<17 and self.index>=12:
                return txt_res3
            elif self.index<12 and self.index>=6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age==9 or self.exp.age==10:
            if self.index>=19.5:
                return txt_res1
            elif self.index<19.5 and self.index>=15.5:
                return txt_res2
            elif self.index<15.5 and self.index>=10.5:
                return txt_res3
            elif self.index<10.5 and self.index>=5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age==11 or self.exp.age==12:
            if self.index>=18:
                return txt_res1
            elif self.index<18 and self.index>=14:
                return txt_res2
            elif self.index<14 and self.index>=9:
                return txt_res3
            elif self.index<9 and self.index>=3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age==13 or self.exp.age==14:
            if self.index>=16.5:
                return txt_res1
            elif self.index<16.5 and self.index>=12.5:
                return txt_res2
            elif self.index<12.5 and self.index>=7.5:
                return txt_res3
            elif self.index<7.5 and self.index>=2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age>=15:
            if self.index>=15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            else:
                return txt_res5

    def initUI(self):
        self.workh_text=QLabel(txt_work_heart+self.result())
        self.int_res=QLabel(txt_int_res+str(self.index))

        self.line_main = QVBoxLayout()
        
        self.line_main.addWidget(self.int_res,alignment=Qt.AlignCenter)
        self.line_main.addWidget(self.workh_text,alignment=Qt.AlignCenter)
        self.setLayout(self.line_main)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width-300, win_hight-200)
        self.move(win_x,win_y)
