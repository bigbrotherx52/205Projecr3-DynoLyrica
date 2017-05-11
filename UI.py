import sys
from PyQt5 import QtWidgets
from search import youtube_search as searcher

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from DownloadCaption import getCaption
from tkinter.filedialog import SaveAs

from __future__ import unicode_literals
import youtube_dl



with open ("MGMT - Kids.lrc", "r") as file:
    data=file.readlines()
DEVELOPER_KEY = "AIzaSyDWH0e3ZQs8bBAYrVleXJsSUhDxMS7EXC0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        #self.myButton = QtWidgets.QPushButton('Next')
        #self.myButton2 = QtWidgets.QPushButton('Before')
        
        self.mySearchBtn= QtWidgets.QPushButton('Search')
        self.myLabel = QtWidgets.QLabel('Button not clicked yet')
        self.lyrics = QtWidgets.QLabel('Lyrics here')
        self.searchBox = QtWidgets.QLineEdit()
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myLabel)
        h_box.addStretch()
        

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.searchBox)
        v_box.addWidget(self.mySearchBtn)
        #v_box.addWidget(self.myButton2)
        v_box.addLayout(h_box)
        v_box.addWidget(self.lyrics)
        #v_box.addWidget(self.myButton)
        
        self.setLayout(v_box)
        self.setWindowTitle('Next')
        self.counter = 0

        self.mySearchBtn.clicked.connect(self.btn_search)
        # create connection between signal (click) and slot (stuff in parens)
        #self.myButton.clicked.connect(self.btn_click)
        # create connection between signal (click) and slot (stuff in parens)
        #self.myButton2.clicked.connect(self.btn_click2)

        self.setWindowTitle('Clicky')    
        self.show()


    def btn_search(self):
        quary = self.searchBox.text()

        
        #build the parser
        

        #try and get results
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    
        # Call the search.list method to retrieve results matching the specified
        # query term.
        
        argparser.add_argument("--q", default = quary)
        argparser.add_argument("--max-results", help="Max results", default=10)
        argparser.add_argument("--closedCaption", help = "closed caption", default = "true")
        args = argparser.parse_args()
        
        search_response = youtube.search().list(
            q=args.q,
            part="id,snippet",
            maxResults=args.max_results
            ).execute()
    
        
        
        videos = []
        ids = []
        #channels = []
        #playlists = []
    
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
        x = 0
        for search_result in search_response.get("items", []):
        
            if search_result["id"]["kind"] == "youtube#video":
                videos.append((search_result["snippet"]["title"]))
                ids.append(search_result["id"]["videoId"])
                print(search_result["id"]["videoId"])
                #videos.append("%s %s" % ( x, search_result["snippet"]["title"]))
                x += 1
      
        print ("get results")
        #print(result)
        
        formattedList = ""
        #number of items returned
     
        for item in videos:
                print("results added: " + item)
                formattedList += "\n" + item
        
      
        self.myLabel.setText(formattedList)
        
                
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl
            ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
            
        getthem ="f"
        # getCaption(id[0])
        
        print(getthem)
        
    
# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
sys.exit(app.exec_())