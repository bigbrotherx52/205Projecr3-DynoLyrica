import os,sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore 

with open ("MGMT - Kids.lrc", "r") as file:
    data=file.readlines()

timeStamp = data[:]
lyrics = data[:]
xx = 0
for x in timeStamp:
    timeStamp[xx] = x[:10]
    lyrics[xx] = x[10:]
    xx += 1



# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.imgSwitch = 1
        self.colSwitch = 0
        self.fontSize = 12
        self.colArray = ['Black','Green','Yellow','Orange','Red','Pink','Purple','Blue','Black']
        self.pic = QtWidgets.QLabel(self)
        self.pic.setGeometry(00,00,500,300)
        self.pic.setScaledContents(True)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))
        self.counter = 0


        self.myButton = QtWidgets.QPushButton('Before')
        self.myButton2 = QtWidgets.QPushButton('Next')
        self.myButton3 = QtWidgets.QPushButton('Before Image')
        self.myButton4 = QtWidgets.QPushButton('Next Image')
        self.myLabel = QtWidgets.QLabel(lyrics[self.counter])
        self.myLabel2 = QtWidgets.QLabel(timeStamp[self.counter])
        #color change button
        self.myButton5 = QtWidgets.QPushButton('Green')
        self.myButton6 = QtWidgets.QPushButton('Font Size')


        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myButton)
        h_box.addWidget(self.myButton2)
        h_box.addWidget(self.myButton3)
        h_box.addWidget(self.myButton4)
        h_box.addWidget(self.myButton5)
        h_box.addWidget(self.myButton6)
        
        #h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.myLabel)
        v_box.addWidget(self.myLabel2)
        v_box.addLayout(h_box)
        

        self.setLayout(v_box)
        self.setWindowTitle('Next')
        self.setGeometry(200,200,500,300)

        # create connection between signal (click) and slot (stuff in parens)
        self.myButton.clicked.connect(self.btn_click)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton2.clicked.connect(self.btn_click2)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton3.clicked.connect(self.btn_click3)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton4.clicked.connect(self.btn_click4)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton5.clicked.connect(self.btn_click5)
        self.myButton6.clicked.connect(self.btn_click6)

        self.setWindowTitle('Dynamic Lyrics')    
        self.show()

    def btn_click(self):
        self.counter -= 1
        self.myLabel.setText(lyrics[self.counter])
        self.myLabel2.setText(timeStamp[self.counter])  #timestamp

    def btn_click2(self):
        self.counter += 1
        self.myLabel.setText(lyrics[self.counter])
        self.myLabel2.setText(timeStamp[self.counter])

    def btn_click3(self):
        self.imgSwitch -= 1
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))

    def btn_click4(self):
        self.imgSwitch += 1
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))

    def btn_click5(self):
        self.colSwitch += 1
        if(self.colSwitch == 8):
            self.colSwitch = 0
        self.myLabel.setStyleSheet("color:" + self.colArray[self.colSwitch])
        self.myButton5.setText(self.colArray[self.colSwitch+1])

    def btn_click6(self):
        self.fontSize += 2
        self.myLabel.setStyleSheet("font-size: " + str(self.fontSize) + "pt")

# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
sys.exit(app.exec_())
