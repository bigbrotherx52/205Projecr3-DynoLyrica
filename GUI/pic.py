import os,sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.setGeometry(0, 0, 400, 200)

pic = QtWidgets.QLabel(window)
pic.setGeometry(10, 10, 400, 100)
#use full ABSOLUTE path to the image, not relative
pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/taco.png"))

window.show()
sys.exit(app.exec_())