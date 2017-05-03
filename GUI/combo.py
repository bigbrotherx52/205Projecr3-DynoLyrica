import os,sys
import PyQt5.QtGui as gui, PyQt5.QtCore as core
from PyQt5 import QtWidgets
from PyQt5 import QtGui as gui
from PyQt5 import QtCore as core

app = QtWidgets.QApplication(sys.argv)
#app = gui.QApplication([])

cb = QtWidgets.QComboBox()

cb.addItem('int 1',1)
cb.addItem('int 2',2)
cb.addItem('int 3',3)
cb.addItem('int 4',4)

print (cb.itemData(0))

core.pyqtSlot('int')
def f(index):
    data,can_convert =  cb.itemData(index)
    if can_convert:
        print ('integer:',data)

cb.currentIndexChanged.connect(f)

cb.show()

app.exec_()