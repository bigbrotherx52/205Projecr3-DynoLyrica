import os,sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

with open ("MGMT - Kids.lrc", "r") as file:
    data=file.readlines()


# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.imgSwitch = 1
        self.pic = QtWidgets.QLabel(self)
        self.pic.setGeometry(200,200,600,400)
        self.pic.setScaledContents(True)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))


        self.myButton = QtWidgets.QPushButton('Next')
        self.myButton2 = QtWidgets.QPushButton('Before')
        self.myButton3 = QtWidgets.QPushButton('Next Image')
        self.myButton4 = QtWidgets.QPushButton('Before Image')
        self.myLabel = QtWidgets.QLabel('Button not clicked yet')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myButton)
        h_box.addWidget(self.myButton2)
        h_box.addWidget(self.myButton3)
        h_box.addWidget(self.myButton4)
        
        #h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.myLabel)
        v_box.addLayout(h_box)
        

        self.setLayout(v_box)
        self.setWindowTitle('Next')
        self.setGeometry(100,100,700,500)
        self.counter = 0

        # create connection between signal (click) and slot (stuff in parens)
        self.myButton.clicked.connect(self.btn_click)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton2.clicked.connect(self.btn_click2)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton3.clicked.connect(self.btn_click3)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton4.clicked.connect(self.btn_click4)

        self.setWindowTitle('Clicky')    
        self.show()

    def btn_click(self):
        self.counter += 1
        self.myLabel.setText(data[self.counter])

    def btn_click2(self):
        self.counter -= 1
        self.myLabel.setText(data[self.counter])

    def btn_click3(self):
        self.imgSwitch += 1
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))

    def btn_click4(self):
        self.imgSwitch -= 1
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))


# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
sys.exit(app.exec_())