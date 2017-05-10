import sys
from PyQt5 import QtWidgets
from search import youtube_search as searcher
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import pafy
import urllib.request
import urllib.parse
import re


with open ("MGMT - Kids.lrc", "r") as file:
    data=file.readlines()



# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

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
        self.show()

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
        audiostreams[0].download("music")

# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
sys.exit(app.exec_())