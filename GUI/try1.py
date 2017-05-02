import sys
from PyQt5 import QtWidgets

# function that will create window

def myWindow():
    # create application object
    # sys.argv are the command line arguments
    app = QtWidgets.QApplication(sys.argv)
    # top level window
    tlw = QtWidgets.QWidget()
    textbox = QtWidgets.QLineEdit(tlw)
    textbox.move(20,20)
    textbox.resize(280,40)
    textbox.setText('Chicken')
    tlw.show()
    # event loop
    sys.exit(app.exec_())

# call function to run
myWindow()