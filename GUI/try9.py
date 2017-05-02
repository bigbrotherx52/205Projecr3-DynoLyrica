import sys
from PyQt5 import QtWidgets

with open ("MGMT - Kids.lrc", "r") as file:
    data=file.readlines()


# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.myButton = QtWidgets.QPushButton('Next')
        self.myButton2 = QtWidgets.QPushButton('Before')
        self.myLabel = QtWidgets.QLabel('Button not clicked yet')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myLabel)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.myButton)
        v_box.addWidget(self.myButton2)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Next')
        self.counter = 0

        # create connection between signal (click) and slot (stuff in parens)
        self.myButton.clicked.connect(self.btn_click)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton2.clicked.connect(self.btn_click2)

        self.setWindowTitle('Clicky')    
        self.show()

    def btn_click(self):
        self.counter += 1
        self.myLabel.setText(data[self.counter])

    def btn_click2(self):
        self.counter -= 1
        self.myLabel.setText(data[self.counter])

# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
sys.exit(app.exec_())