import sys
from PyQt5 import QtWidgets
from search import youtube_search as searcher
from apiclient.errors import HttpError
from oauth2client.tools import argparser


with open ("MGMT - Kids.lrc", "r") as file:
    data=file.readlines()



# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.timesClicked = 0
        self.myButton = QtWidgets.QPushButton('Next')
        self.myButton2 = QtWidgets.QPushButton('Before')
        
        self.mySearchBtn= QtWidgets.QPushButton('Search')
        self.myLabel = QtWidgets.QLabel('Button not clicked yet')
        self.searchBox = QtWidgets.QLineEdit()
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myLabel)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.searchBox)
        v_box.addWidget(self.mySearchBtn)
        #v_box.addWidget(self.myButton)
        #v_box.addWidget(self.myButton2)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Next')
        self.counter = 0

        self.mySearchBtn.clicked.connect(self.btn_search)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton.clicked.connect(self.btn_click)
        # create connection between signal (click) and slot (stuff in parens)
        self.myButton2.clicked.connect(self.btn_click2)

        timesClicked = 0

        self.setWindowTitle('Clicky')    
        self.show()


    def btn_search(self):
        
        self.quary = self.searchBox.text()
        #a = argparser[:]

        if(self.timesClicked == 0):
            #build the parser
            argparser.add_argument("--q", help = "text", default = self.searchBox.text())
            argparser.add_argument("--max-results", help="Max results", default=10)
            argparser.add_argument("--closedCaption", help = "closed caption", default = "true")
            args = argparser.parse_args()
        if(self.timesClicked > 0):
            #argparser.add_argument("--q", help = "text", default = self.searchBox.text())
            #argparser.add_argument("--max-results", help="Max results", default=10)
            #argparser.add_argument("--closedCaption", help = "closed caption", default = "true")
            args = argparser.parse_args()
        self.timesClicked += 1
        print(self.searchBox.text())
        #try and get results
        result = ''
        try:
            result = searcher(args)
        except HttpError:
            print ("An HTTP error %d occurred:")
      
        #print ("get results")
        #print (args)
        #print(result)
        
        formattedList = ""
        #number of items returned
        print(result.__len__())
        print(result)
        for item in result:
            #print("results added: " + item)
            formattedList += "\n" + item
        
        self.myLabel.setText(formattedList)
        self.args = argparser

        
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