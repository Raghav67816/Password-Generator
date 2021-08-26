import random
import array
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pyperclip

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(467, 674)
        MainWindow.setMinimumSize(QSize(467, 674))
        MainWindow.setMaximumSize(QSize(467, 674))
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.bg)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.heading = QLabel(self.container)
        self.heading.setObjectName(u"heading")
        self.heading.setMinimumSize(QSize(0, 50))
        self.heading.setMaximumSize(QSize(16777215, 50))
        self.heading.setStyleSheet(u"QLabel{\n"
"	font-size: 20px;\n"
"	color: rgb(68, 136, 204)\n"
"}")

        self.verticalLayout_4.addWidget(self.heading)

        self.inputs = QFrame(self.container)
        self.inputs.setObjectName(u"inputs")
        self.inputs.setMinimumSize(QSize(0, 100))
        self.inputs.setMaximumSize(QSize(16777215, 100))
        self.inputs.setFrameShape(QFrame.StyledPanel)
        self.inputs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.inputs)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.pl = QLineEdit(self.inputs)
        self.pl.setObjectName(u"pl")
        self.pl.setMinimumSize(QSize(350, 30))
        self.pl.setMaximumSize(QSize(350, 30))
        self.pl.setStyleSheet(u"QLineEdit{  \n"
"	border: 2px solid rgb(66, 132, 198);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	border-bottom-color: rgb(66, 132, 198);\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-right-color: white\n"
"}")
        self.pl.setMaxLength(2)
        self.pl.setCursorPosition(0)
        self.pl.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.pl.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.pl)

        self.spacer = QFrame(self.inputs)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setMinimumSize(QSize(5, 5))
        self.spacer.setMaximumSize(QSize(5, 5))
        self.spacer.setFrameShape(QFrame.StyledPanel)
        self.spacer.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.spacer)

        self.sb = QPushButton(self.inputs)
        self.sb.setObjectName(u"sb")
        self.sb.setMinimumSize(QSize(30, 30))
        self.sb.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(66, 132, 198);\n"
"	color: white;\n"
"	border: 0px solid rgb(240, 240, 240);\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 173, 255)\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.sb)


        self.verticalLayout_4.addWidget(self.inputs)

        self.ouput_field = QFrame(self.container)
        self.ouput_field.setObjectName(u"ouput_field")
        self.ouput_field.setFrameShape(QFrame.StyledPanel)
        self.ouput_field.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ouput_field)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info = QLabel(self.ouput_field)
        self.info.setObjectName(u"info")
        self.info.setMinimumSize(QSize(0, 30))
        self.info.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.info)

        self.ugp = QPlainTextEdit(self.ouput_field)
        self.ugp.setObjectName(u"ugp")
        self.ugp.setStyleSheet(u"QPlainTextEdit{  \n"
"	border: 2px solid rgb(66, 132, 198);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px\n"
"}")
        self.ugp.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.ugp)

        self.copybtn = QPushButton(self.ouput_field)
        self.copybtn.setObjectName(u"copybtn")
        self.copybtn.setMinimumSize(QSize(30, 30))
        self.copybtn.setMaximumSize(QSize(60, 16777215))
        self.copybtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(66, 132, 198);\n"
"	color: white;\n"
"	border: 0px solid rgb(240, 240, 240);\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 173, 255)\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.copybtn)


        self.verticalLayout_4.addWidget(self.ouput_field)


        self.verticalLayout_2.addWidget(self.container)


        self.verticalLayout.addWidget(self.bg)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Password Generator</p></body></html>", None))
        self.pl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password Length", None))
        self.sb.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"Note:- Password generated are unique and we do not save your data.", None))
        self.ugp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unique Generated Password", None))
        self.copybtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
    # retranslateUi

        self.sb.clicked.connect(self.sb_func)
        self.copybtn.clicked.connect(self.copy_pass)
        self.pl.setValidator(QIntValidator())

    def sb_func(self):
                # Define max lenght of password
        integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
        lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']
        
        uppercase_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']
        
        symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
                '*', '(', ')', '<']
        passwords_list = integers + uppercase_alpha + lower_alpha + symbols
        rand_digit = random.choice(integers)
        rand_upper = random.choice(uppercase_alpha)
        rand_lower = random.choice(lower_alpha)
        rand_symbol = random.choice(symbols)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        int_input = self.pl.text()
        for x in range(int(int_input) - 4):
            temp_pass = temp_pass + random.choice(passwords_list)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        password = ""

        for x in temp_pass_list:
            password = password + x
            self.ugp.setPlainText(password)

    def copy_pass(self):
        pyperclip.copy(self.ugp.toPlainText())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.setWindowTitle("Password Generator")
    window.setWindowIcon(QIcon("./padlock.png"))
    window.show()
    sys.exit(app.exec_())
