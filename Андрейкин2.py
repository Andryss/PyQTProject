import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTextBrowser
from PyQt5.QtWidgets import QLabel, QLCDNumber, QMenuBar, QStatusBar, QTextEdit
from PyQt5.QtGui import  QFont, QCursor
from PyQt5.QtCore import Qt, QSize, QRect, QCoreApplication, QMetaObject

operator = []
operation = True
memory = 0
K = 0
M = 0
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_1.clicked.connect(self.one)
        self.btn_2.clicked.connect(self.two)
        self.btn_3.clicked.connect(self.three)
        self.btn_4.clicked.connect(self.four)
        self.btn_5.clicked.connect(self.five)
        self.btn_6.clicked.connect(self.six)
        self.btn_7.clicked.connect(self.seven)
        self.btn_8.clicked.connect(self.eight)
        self.btn_9.clicked.connect(self.nine)
        self.btn_0.clicked.connect(self.zero)
        self.btn_00.clicked.connect(self.zerozero)
        self.btn_floating.clicked.connect(self.floating)
        
        self.btn_m_plus.clicked.connect(self.m_plus)
        self.btn_m_minus.clicked.connect(self.m_minus)
        self.btn_mr.clicked.connect(self.mr)
        self.btn_mc.clicked.connect(self.mc)
        
        self.btn_sin.clicked.connect(self.sin)
        self.btn_cos.clicked.connect(self.cos)
        self.btn_tg.clicked.connect(self.tg)
        self.btn_ctg.clicked.connect(self.ctg)
        
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_ymn.clicked.connect(self.ymn)
        self.btn_step.clicked.connect(self.step)
        self.btn_delen.clicked.connect(self.delen)
        self.btn_pr.clicked.connect(self.pr)
        
        
        self.btn_delet.clicked.connect(self.delet)
        self.btn_ac.clicked.connect(self.ac)
        self.btn_result.clicked.connect(self.result)
        
        
    def one(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('1')
            operation = False
        else:
            operator[-1] += '1'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def two(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('2')
            operation = False
        else:
            operator[-1] += '2'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def three(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('3')
            operation = False
        else:
            operator[-1] += '3'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def four(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('4')
            operation = False
        else:
            operator[-1] += '4'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def five(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('5')
            operation = False
        else:
            operator[-1] += '5'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def six(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('6')
            operation = False
        else:
            operator[-1] += '6'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def seven(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('7')
            operation = False
        else:
            operator[-1] += '7'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def eight(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('8')
            operation = False
        else:
            operator[-1] += '8'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def nine(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('9')
            operation = False
        else:
            operator[-1] += '9'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def zero(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('0')
            operation = False
        else:
            operator[-1] += '0'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def zerozero(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('00')
            operation = False
        else:
            operator[-1] += '00'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    def floating(self):
        global operator, operation, K
        K = 0
        if operation:
            operator.append('.')
            operation = False
        else:
            operator[-1] += '.'
        self.window.display(operator[-1])
        self.sprav.setText(''.join(operator))
    
    def m_plus(self):
        global memory, operator, K
        K = 0
        if operator[-1].isdigit():
            memory = float(memory) + float(operator[-1])
            self.m.setText("M+")
    def m_minus(self):
        global memory, operator, K
        K = 0
        if operator[-1].isdigit():
            memory = float(memory) - float(operator[-1])
            self.m.setText("M-")
    def mr(self):
        global operator, memory, K
        K = 0
        if memory != 0:
            operator.append('mr')
            self.window.display(memory)
            self.sprav.setText(''.join(operator))
    def mc(self):
        global memory, K
        K = 0
        memory = 0
        self.m.setText("")
        
    def sin(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('sin')
        self.sprav.setText(''.join(operator))
    def cos(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('cos')
        self.sprav.setText(''.join(operator))
    def tg(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('tg')
        self.sprav.setText(''.join(operator))
    def ctg(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('ctg')
        self.sprav.setText(''.join(operator))
        
    def plus(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('+')
        self.sprav.setText(''.join(operator))
    def minus(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('-')
        self.sprav.setText(''.join(operator))
    def ymn(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('*')
        self.sprav.setText(''.join(operator))
    def step(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('^')
        self.sprav.setText(''.join(operator))
    def delen(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('/')
        self.sprav.setText(''.join(operator))
    def pr(self):
        global operator, operation, K
        K = 0
        operation = True
        operator.append('%')
        self.sprav.setText(''.join(operator))
            
    def delet(self):
        global operator, operation, K, M
        M += 1
        if M == 7:
            self.resize(490, 440)
            M = 0
        K = 0
        if len(operator) != 0:
            last = operator[-1]
            if last == 'sin' or last == 'cos' or last == 'tg' or last == 'ctg' or last == 'mr':
                del operator[-1]
            else:
                operator[-1] = operator[-1][:-1:]
            if operator[-1] == '':
                del operator[-1]
            if len(operator) != 0:
                self.window.display(operator[-1])
            else:
                operator = ['']
                self.window.display(0)
            self.sprav.setText(''.join(operator))
    def ac(self):
        global operator, operation, K
        K += 1
        if K == 7:
            self.resize(912, 689)
        operator = []
        operation = True
        self.window.display(0)
        self.sprav.setText(''.join(operator))
    
    def result(self):
        global operator, memory, operation, K
        K = 0
        try:
            while 'mr' in operator:
                index = operator.index('mr')
                operator[index] = memory
            while 'sin' in operator:
                index = operator.index('sin')
                rad = math.radians(float(operator[index + 1]))
                sin = math.sin(rad)
                del operator[index + 1]
                operator[index] = str(sin)
            while 'cos' in operator:
                index = operator.index('cos')
                rad = math.radians(float(operator[index + 1]))
                cos = math.cos(rad)
                del operator[index + 1]
                operator[index] = str(cos)
            while 'tg' in operator:
                index = operator.index('tg')
                rad = math.radians(float(operator[index + 1]))
                tg = math.tan(rad)
                del operator[index + 1]
                operator[index] = str(tg)
            while 'ctg' in operator:
                index = operator.index('ctg')
                rad = math.radians(float(operator[index + 1]))
                ctg = 1 / math.tan(rad)
                del operator[index + 1]
                operator[index] = str(ctg)
            while '^' in operator:
                index = operator.index('^')
                count = float(operator[index - 1]) ** float(operator[index + 1])
                del operator[index + 1]
                operator[index] = str(float(round(count, 15)))
                del operator[index - 1]
            while ('*' in operator) or ("/" in operator) or ("%" in operator):
                if '*' in operator:
                    index_1 = operator.index('*')
                else:
                    index_1 = 1000
                if '/' in operator:
                    index_2 = operator.index('/')
                else:
                    index_2 = 1000
                if '%' in operator:
                    index_3 = operator.index('%')
                else:
                    index_3 = 1000
                spisok = [index_1, index_2, index_3]
                if min(spisok) == index_2:
                    count = float(operator[index_2 - 1]) / float(operator[index_2 + 1])
                    del operator[index_2 + 1]
                    operator[index_2] = str(count)
                    del operator[index_2 - 1]
                elif min(spisok) == index_1:
                    count = float(operator[index_1 - 1]) * float(operator[index_1 + 1])
                    del operator[index_1 + 1]
                    operator[index_1] = str(float(round(count, 15)))
                    del operator[index_1 - 1]
                elif min(spisok) == index_3:
                    count = float(operator[index_3 - 1]) % float(operator[index_3 + 1])
                    del operator[index_3 + 1]
                    operator[index_3] = str(float(round(count, 15)))
                    del operator[index_3 - 1]
            while ('+' in operator) or ("-" in operator):
                if '+' in operator:
                    index_1 = operator.index('+')
                else:
                    index_1 = 1000
                if '-' in operator:
                    index_2 = operator.index('-')
                else:
                    index_2 = 1000
                if (index_1 > index_2) and (index_2 != -1):
                    count = float(operator[index_2 - 1]) - float(operator[index_2 + 1])
                    del operator[index_2 + 1]
                    operator[index_2] = str(count)
                    del operator[index_2 - 1]
                elif (index_1 < index_2) and (index_1 != -1):
                    count = float(operator[index_1 - 1]) + float(operator[index_1 + 1])
                    del operator[index_1 + 1]
                    operator[index_1] = str(count)
                    del operator[index_1 - 1]
            self.sprav.setText(''.join(operator))
            self.window.display(operator[0])
        except Exception:
            self.window.display('Error')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(912, 689)
        MainWindow.resize(490, 440)
        font = QFont()
        font.setFamily("MS Gothic")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.window = QLCDNumber(self.centralwidget)
        self.window.setGeometry(QRect(10, 10, 461, 60))
        self.window.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:1 rgba(249, 187, 0, 255));")
        self.window.setDigitCount(20)
        self.window.setObjectName("window")
        self.btn_ac = QPushButton(self.centralwidget)
        self.btn_ac.setGeometry(QRect(410, 320, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_ac.setFont(font)
        self.btn_ac.setStyleSheet("font: 75 20pt \"Segoe Script\";color: rgb(255, 0, 0);\n"
"background-color: rgb(29, 29, 29);")
        self.btn_ac.setIconSize(QSize(16, 16))
        self.btn_ac.setObjectName("btn_ac")
        self.btn_mr = QPushButton(self.centralwidget)
        self.btn_mr.setGeometry(QRect(170, 80, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_mr.setFont(font)
        self.btn_mr.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 239, 239);font: 75 15pt \"Segoe Script\";")
        self.btn_mr.setIconSize(QSize(16, 16))
        self.btn_mr.setObjectName("btn_mr")
        self.btn_mc = QPushButton(self.centralwidget)
        self.btn_mc.setGeometry(QRect(250, 80, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_mc.setFont(font)
        self.btn_mc.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 239, 239);font: 75 15pt \"Segoe Script\";")
        self.btn_mc.setIconSize(QSize(16, 16))
        self.btn_mc.setObjectName("btn_mc")
        self.btn_m_plus = QPushButton(self.centralwidget)
        self.btn_m_plus.setEnabled(True)
        self.btn_m_plus.setGeometry(QRect(10, 80, 61, 50))
        self.btn_m_plus.setMaximumSize(QSize(61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_m_plus.setFont(font)
        self.btn_m_plus.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_m_plus.setMouseTracking(True)
        self.btn_m_plus.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 239, 239);font: 75 15pt \"Segoe Script\";")
        self.btn_m_plus.setIconSize(QSize(16, 16))
        self.btn_m_plus.setCheckable(False)
        self.btn_m_plus.setChecked(False)
        self.btn_m_plus.setObjectName("btn_m_plus")
        self.btn_m_minus = QPushButton(self.centralwidget)
        self.btn_m_minus.setGeometry(QRect(90, 80, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_m_minus.setFont(font)
        self.btn_m_minus.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 239, 239);font: 75 15pt \"Segoe Script\";")
        self.btn_m_minus.setIconSize(QSize(16, 16))
        self.btn_m_minus.setObjectName("btn_m_minus")
        self.btn_cos = QPushButton(self.centralwidget)
        self.btn_cos.setGeometry(QRect(410, 80, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_cos.setFont(font)
        self.btn_cos.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(255, 169, 254);font: 75 20pt \"Segoe Script\";")
        self.btn_cos.setIconSize(QSize(16, 16))
        self.btn_cos.setObjectName("btn_cos")
        self.btn_sin = QPushButton(self.centralwidget)
        self.btn_sin.setGeometry(QRect(330, 80, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_sin.setFont(font)
        self.btn_sin.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(255, 169, 254);font: 75 20pt \"Segoe Script\";")
        self.btn_sin.setIconSize(QSize(16, 16))
        self.btn_sin.setObjectName("btn_sin")
        self.btn_tg = QPushButton(self.centralwidget)
        self.btn_tg.setGeometry(QRect(330, 140, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_tg.setFont(font)
        self.btn_tg.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(255, 169, 254);font: 75 20pt \"Segoe Script\";")
        self.btn_tg.setIconSize(QSize(16, 16))
        self.btn_tg.setObjectName("btn_tg")
        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QRect(250, 200, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(27, 147, 0);")
        self.btn_minus.setIconSize(QSize(16, 16))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QRect(250, 140, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(27, 147, 0);")
        self.btn_plus.setIconSize(QSize(16, 16))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_ymn = QPushButton(self.centralwidget)
        self.btn_ymn.setGeometry(QRect(250, 260, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_ymn.setFont(font)
        self.btn_ymn.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(27, 147, 0);")
        self.btn_ymn.setIconSize(QSize(16, 16))
        self.btn_ymn.setObjectName("btn_ymn")
        self.btn_result = QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QRect(330, 320, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_result.setFont(font)
        self.btn_result.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 40pt \"Segoe Script\";color: rgb(255, 140, 0);")
        self.btn_result.setIconSize(QSize(16, 16))
        self.btn_result.setObjectName("btn_result")
        self.btn_step = QPushButton(self.centralwidget)
        self.btn_step.setGeometry(QRect(330, 200, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_step.setFont(font)
        self.btn_step.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(27, 147, 0);")
        self.btn_step.setIconSize(QSize(16, 16))
        self.btn_step.setObjectName("btn_step")
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QRect(10, 140, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_1.setFont(font)
        self.btn_1.setMouseTracking(False)
        self.btn_1.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 85, 255);font: 75 30pt \"Segoe Script\";")
        self.btn_1.setIconSize(QSize(16, 16))
        self.btn_1.setCheckable(False)
        self.btn_1.setChecked(False)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QRect(90, 140, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 85, 255);font: 75 30pt \"Segoe Script\";")
        self.btn_2.setIconSize(QSize(16, 16))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QRect(170, 140, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 85, 255);font: 75 30pt \"Segoe Script\";")
        self.btn_3.setIconSize(QSize(16, 16))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QRect(10, 200, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 85, 255);font: 75 30pt \"Segoe Script\";")
        self.btn_4.setIconSize(QSize(16, 16))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QRect(90, 200, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 85, 255);font: 75 30pt \"Segoe Script\";")
        self.btn_5.setIconSize(QSize(16, 16))
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QRect(170, 200, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(0, 85, 255);")
        self.btn_6.setIconSize(QSize(16, 16))
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QRect(10, 260, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(0, 85, 255);")
        self.btn_7.setIconSize(QSize(16, 16))
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QRect(90, 260, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(0, 85, 255);")
        self.btn_8.setIconSize(QSize(16, 16))
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QRect(170, 260, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(0, 85, 255);")
        self.btn_9.setIconSize(QSize(16, 16))
        self.btn_9.setObjectName("btn_9")
        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QRect(10, 320, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(0, 85, 255);")
        self.btn_0.setIconSize(QSize(16, 16))
        self.btn_0.setObjectName("btn_0")
        self.btn_ctg = QPushButton(self.centralwidget)
        self.btn_ctg.setGeometry(QRect(410, 140, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_ctg.setFont(font)
        self.btn_ctg.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(255, 169, 254);font: 75 20pt \"Segoe Script\";")
        self.btn_ctg.setIconSize(QSize(16, 16))
        self.btn_ctg.setObjectName("btn_ctg")
        self.btn_delen = QPushButton(self.centralwidget)
        self.btn_delen.setGeometry(QRect(330, 260, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_delen.setFont(font)
        self.btn_delen.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 30pt \"Segoe Script\";color: rgb(27, 147, 0);")
        self.btn_delen.setIconSize(QSize(16, 16))
        self.btn_delen.setObjectName("btn_delen")
        self.Sprav = QLabel(self.centralwidget)
        self.Sprav.setGeometry(QRect(500, 10, 401, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.Sprav.setFont(font)
        self.Sprav.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);")
        self.Sprav.setObjectName("Sprav")
        self.Text_sprav = QTextBrowser(self.centralwidget)
        self.Text_sprav.setGeometry(QRect(490, 69, 411, 351))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Text_sprav.setFont(font)
        self.Text_sprav.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 12pt \"Segoe Script\";")
        self.Text_sprav.setObjectName("Text_sprav")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(10, 480, 391, 160))
        font = QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 170, 0);")
        self.textEdit.setObjectName("textEdit")
        self.Sprav_2 = QLabel(self.centralwidget)
        self.Sprav_2.setGeometry(QRect(10, 430, 391, 41))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.Sprav_2.setFont(font)
        self.Sprav_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);")
        self.Sprav_2.setObjectName("Sprav_2")
        self.Text_sprav_2 = QTextBrowser(self.centralwidget)
        self.Text_sprav_2.setGeometry(QRect(410, 480, 491, 161))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Text_sprav_2.setFont(font)
        self.Text_sprav_2.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 12pt \"Segoe Script\";")
        self.Text_sprav_2.setObjectName("Text_sprav_2")
        self.m = QLabel(self.centralwidget)
        self.m.setGeometry(QRect(13, 13, 20, 10))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(9)
        self.m.setFont(font)
        self.m.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:1 rgba(249, 187, 0, 255));")
        self.m.setText("")
        self.m.setObjectName("m")
        self.btn_floating = QPushButton(self.centralwidget)
        self.btn_floating.setGeometry(QRect(250, 320, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_floating.setFont(font)
        self.btn_floating.setStyleSheet("background-color: rgb(29, 29, 29);font: 75 40pt \"Segoe Script\";\n"
"color: rgb(20, 24, 255);")
        self.btn_floating.setIconSize(QSize(16, 16))
        self.btn_floating.setObjectName("btn_floating")
        self.btn_00 = QPushButton(self.centralwidget)
        self.btn_00.setGeometry(QRect(90, 320, 141, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_00.setFont(font)
        self.btn_00.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(0, 85, 255);font: 75 30pt \"Segoe Script\";")
        self.btn_00.setIconSize(QSize(16, 16))
        self.btn_00.setObjectName("btn_00")
        self.btn_delet = QPushButton(self.centralwidget)
        self.btn_delet.setGeometry(QRect(410, 260, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_delet.setFont(font)
        self.btn_delet.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(255, 0, 0);font: 75 20pt \"Segoe Script\";")
        self.btn_delet.setIconSize(QSize(16, 16))
        self.btn_delet.setObjectName("btn_delet")
        self.btn_pr = QPushButton(self.centralwidget)
        self.btn_pr.setGeometry(QRect(410, 200, 61, 50))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_pr.setFont(font)
        self.btn_pr.setStyleSheet("background-color: rgb(29, 29, 29);color: rgb(27, 147, 0);font: 75 30pt \"Segoe Script\";")
        self.btn_pr.setIconSize(QSize(16, 16))
        self.btn_pr.setObjectName("btn_pr")
        self.sprav = QLabel(self.centralwidget)
        self.sprav.setGeometry(QRect(40, 380, 441, 41))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(15)
        self.sprav.setFont(font)
        self.sprav.setStyleSheet("color: rgb(255, 255, 255);")
        self.sprav.setText("")
        self.sprav.setObjectName("sprav")
        self.Sprav_4 = QLabel(self.centralwidget)
        self.Sprav_4.setGeometry(QRect(410, 430, 491, 41))
        font = QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.Sprav_4.setFont(font)
        self.Sprav_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);")
        self.Sprav_4.setObjectName("Sprav_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 912, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_ac.setText(_translate("MainWindow", "AC"))
        self.btn_mr.setText(_translate("MainWindow", "MR"))
        self.btn_mc.setText(_translate("MainWindow", "MC"))
        self.btn_m_plus.setText(_translate("MainWindow", "M+"))
        self.btn_m_minus.setText(_translate("MainWindow", "M-"))
        self.btn_cos.setText(_translate("MainWindow", "cos"))
        self.btn_sin.setText(_translate("MainWindow", "sin"))
        self.btn_tg.setText(_translate("MainWindow", "tg"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_ymn.setText(_translate("MainWindow", "x"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn_step.setText(_translate("MainWindow", "^"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_ctg.setText(_translate("MainWindow", "ctg"))
        self.btn_delen.setText(_translate("MainWindow", "/"))
        self.Sprav.setText(_translate("MainWindow", "         Справочник"))
        self.Text_sprav.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe Script\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[M+] – прибавление числа в память</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[M-] – вычитание числа из памяти</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[^] – возведение в выбранную степень</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[+][-][x][</span><span style=\" font-family:\'Symbol\'; color:#0febff;\">¸</span><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">] – арифметические операции</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[MR] – вывести содержимое памяти на дисплей</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[MC] – очистить содержимое памяти</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[AC] – общий сброс</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\">[sin][cos][tg][ctg] – формулы произведения тригонометрических функций, при работе с этими функциями сначала записывается sin, cos, tg, ctg потом число(Например sin 45)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#0febff;\">[Del]</span><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\"> – удаляет последнюю введенную цифру или знак действия</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#0febff;\">[%]</span><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\"> – вычисляет остаток от деления</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#0febff;\"><br /></span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#0febff;\">[.]</span><span style=\" font-family:\'Lato-Regular,Arial,sans-serif\'; color:#0febff;\"> – используется для записи дробной части</span></p></body></html>"))
        self.Sprav_2.setText(_translate("MainWindow", "        Для заметок"))
        self.Text_sprav_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe Script\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#00ff7f;\">    </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#11ff00;\">  - Если указанный порядок действий невозможно вычислить</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#11ff00;\">      - Если мы накасячили</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#11ff00;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#11ff00;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#11ff00;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#11ff00;\">                   По всем вопросам обращайтесь  https://vk.com/vasily.shishkin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#11ff00;\">                                                                    https://vk.com/andrey.krivosheev</span></p></body></html>"))
        self.btn_floating.setText(_translate("MainWindow", "."))
        self.btn_00.setText(_translate("MainWindow", "00"))
        self.btn_delet.setText(_translate("MainWindow", "Del"))
        self.btn_pr.setText(_translate("MainWindow", "%"))
        self.Sprav_4.setText(_translate("MainWindow", "  Почему появляется ошибка?"))       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())