import os,sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

import pafy
import urllib.request
import urllib.parse
import re

import vlc

with open ("MGMT - Kids.lrc", "r") as file:
    data=file.readlines()

timeStamp = data[:]
lyrics = data[:]
xx = 0
for x in timeStamp:
    timeStamp[xx] = x[:10]
    lyrics[xx] = x[10:]
    xx += 1




class Window2(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)

        self.init_ui()


    def init_ui(self):
        self.mySearchBtn= QtWidgets.QPushButton('Download')
        self.myLabel = QtWidgets.QLabel('Enter name of video to download: ')
        self.searchBox = QtWidgets.QLineEdit()
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myLabel)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.searchBox)
        v_box.addWidget(self.mySearchBtn)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Next')

        self.mySearchBtn.clicked.connect(self.btn_search)

        self.setWindowTitle('Youtube Searcher')

    def btn_search(self):
        
        query_string = urllib.parse.urlencode({"search_query" : self.searchBox.text()})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        url = "http://www.youtube.com/watch?v=" + search_results[0]
        video = pafy.new(url)
        #print(video.title)
        self.myLabel.setText(video.title + "\n" + url)
        duration = video.duration
        audiostreams = video.audiostreams
        video.getbestaudio(preftype="m4a").download("music")

# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.init_ui()

    def init_ui(self):

        self.imgSwitch = 1
        self.colSwitch = 0
        self.fontSize = 11
        self.padding = 0
        self.colArray = ['Black','Green','Yellow','Orange','Red','Pink','Purple','Blue','Black']
        self.pic = QtWidgets.QLabel(self)
        self.pic.setGeometry(00,00,500,300)
        self.pic.setScaledContents(True)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))
        self.counter = 0
        self.colors = [(255,255,255), (0,0,255)]


        self.myButton = QtWidgets.QPushButton('Before')
        self.myButton2 = QtWidgets.QPushButton('Next')
        self.myButton3 = QtWidgets.QPushButton('Before \n Image')
        self.myButton4 = QtWidgets.QPushButton('Next \n Image')
        self.myLabel = QtWidgets.QLabel(lyrics[self.counter])
        self.myLabel2 = QtWidgets.QLabel(timeStamp[self.counter])
        #color change button
        self.myButton5 = QtWidgets.QPushButton('Green')
        self.myButton6 = QtWidgets.QPushButton('Font \n Size')
        self.myButton7 = QtWidgets.QPushButton('Text \n Right')
        self.myButton10 = QtWidgets.QPushButton('Song \n Downloader')
        self.myButton11 = QtWidgets.QPushButton('Play')

        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)


        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myButton)
        h_box.addWidget(self.myButton2)
        h_box.addWidget(self.myButton3)
        h_box.addWidget(self.myButton4)
        h_box.addWidget(self.myButton5)
        h_box.addWidget(self.myButton6)
        h_box.addWidget(self.myButton7)
        h_box.addWidget(self.myButton10)
        h_box.addWidget(self.myButton11)
        
        #h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.myLabel)
        v_box.addWidget(self.myLabel2)
        v_box.addWidget(self.slider)
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
        self.myButton7.clicked.connect(self.btn_click7)
        self.myButton10.clicked.connect(self.btn_click10)
        self.myButton11.clicked.connect(self.btn_click11)
        
        self.dialogTextBrowser = Window2(self)

        self.setWindowTitle('Dynamic Lyrics')    
        #self.show()


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
        self.myLabel.setStyleSheet("color:" + self.colArray[self.colSwitch] + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")
        self.myButton5.setText(self.colArray[self.colSwitch+1])

    def btn_click6(self):
        self.fontSize += 2
        if(self.fontSize > 30):
            self.fontSize = 11
        self.myLabel.setStyleSheet("color:" + self.colArray[self.colSwitch] + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")

    def btn_click7(self):
        self.padding += 4
        if(self.padding > 20):
            self.padding = 0
        self.myLabel.setStyleSheet("color:" + self.colArray[self.colSwitch] + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")

    def btn_click10(self):
        self.dialogTextBrowser.exec_()

    def btn_click11(self):
        self.p = vlc.MediaPlayer("music")
        self.p.play()


# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
a_window.show()
sys.exit(app.exec_())
