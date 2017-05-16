import os,sys,random
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

import pafy
import urllib.request
import urllib.parse
import re

import vlc

with open ("MGMT - Kids.lrc", "r") as file:		#Reads all of lines of the lrc file
    data=file.readlines()

timeStamp = data[:]	#creates new array for timestamps
lyrics = data[:]	#creates new array for lyrics
xx = 0
for x in timeStamp:		#trims the uneeded values on timestamps and lyrics to keep them seperate.
    timeStamp[xx] = x[:10]
    lyrics[xx] = x[10:]
    xx += 1




class Window2(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)

        self.init_ui()


    def init_ui(self):		#This is a new window for downloading a youtube video as m4a
        self.mySearchBtn= QtWidgets.QPushButton('Download')
        self.myLabel = QtWidgets.QLabel('Enter name of video to download: ')

        self.searchBox = QtWidgets.QLineEdit()
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.myLabel)	#Label under search
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.searchBox)		#Search text box for searching for video downloads
        v_box.addWidget(self.mySearchBtn)	#Search button
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.mySearchBtn.clicked.connect(self.btn_search)	#Connects btn_search with download button

        self.setWindowTitle('Youtube Searcher')		#Title of download window

    def btn_search(self):
        
        query_string = urllib.parse.urlencode({"search_query" : self.searchBox.text()})				#Sets the search to what you entered in the textbox
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)		#Requests the result
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())		#Decodes the code to something readable
        url = "http://www.youtube.com/watch?v=" + search_results[0]				#Saves url for display
        video = pafy.new(url)		#Used so we can actually download the video 
        self.myLabel.setText(video.title + "\n" + url)		#Where the URL is actually displayed
        duration = video.duration		#Get duration of video
        audiostreams = video.audiostreams		#Grabs audio streams
        video.getbestaudio(preftype="m4a").download("music")	#downloads the m4a version of the audio and saves it as music

# inherit from QWidget class
# QWidget class is the base class of all user interface objects
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.init_ui()

    def init_ui(self):

        self.imgSwitch = 1	#For image switch
        self.colSwitch = 0	#For color Switching
        self.fontSize = 11	#Initializes font size
        self.padding = 0	#Used to push the font more to the center
        self.ranFont = 0	#Initializes random font index
        self.ranColor = 0	#Initializes random color index
        self.colArray = ['Black','Green','Yellow','Orange','Red','Pink','Purple','Blue','Black']	#Initializes color array
        self.pic = QtWidgets.QLabel(self)	#For picture background
        self.pic.setGeometry(00,00,500,300)	#Where the picture is centered
        self.pic.setScaledContents(True)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))	#Chooses first image
        self.counter = 0

        ##  LIST OF COLORS
        self.colors = [ (255,0,0),
            (255,69,0),
            (255,255,0),
            (0,255,0),
            (0,0,255),
            (128,0,128),
            (0,0,0),
            (165,42,42),
            (128,0,0),
            (192,192,192),
            (0,128,128),
            (0,255,255),
            (255,0,255)]

        ##  LIST OF FONTS
        self.fonts = [ "Times New Roman", "Arial", "Lucida Bright", "New Century Schoolbook", "Source Sans Pro", "Semibold", "Courier", "Algerian", "Broadway", "Impact", "Magneto", "Pristina", "Vivaldi"]


        self.myButton = QtWidgets.QPushButton('Before')		#Lyrics before button
        self.myButton2 = QtWidgets.QPushButton('Next')		#Lyrics after button
        self.myButton3 = QtWidgets.QPushButton('Before \n Image')	#Go to next image button
        self.myButton4 = QtWidgets.QPushButton('Next \n Image')		#Go to previous image button
        self.myLabel = QtWidgets.QLabel(lyrics[self.counter])		#Displays lyrics
        self.myLabel2 = QtWidgets.QLabel(timeStamp[self.counter])	#Displays Time stamp
        self.myLabel3 = QtWidgets.QLabel('')	#spacing	
        self.myLabel4 = QtWidgets.QLabel('')	#spacing
        #color change button
        self.myButton5 = QtWidgets.QPushButton('Green')		#Sets label of button as green
        self.myButton6 = QtWidgets.QPushButton('Font \n Size')	#Change font size button
        self.myButton7 = QtWidgets.QPushButton('Text \n Right')	#Moves text right button
        #randomize color (uses list at the top)
        self.myButton8 = QtWidgets.QPushButton('Randomize \n Color')
        self.myButton9 = QtWidgets.QPushButton('Change \n Font')
        self.myButton10 = QtWidgets.QPushButton('Song \n Downloader')
        self.myButton11 = QtWidgets.QPushButton('Play \n ')

        #Slider stuff
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.valueChanged.connect(self.valuec)	#Sets slider so that when the value is changed it is able to change the timestamp


        #Layout for horizontal widgets
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        #h_box.addWidget(self.myButton)		#before
        #h_box.addWidget(self.myButton2)	#next
        h_box.addWidget(self.myButton3)
        h_box.addWidget(self.myButton4)
        #h_box.addWidget(self.myButton5)	#choice of color
        h_box.addWidget(self.myButton6)
        h_box.addWidget(self.myButton7)
        h_box.addWidget(self.myButton8)
        h_box.addWidget(self.myButton9)
        h_box.addWidget(self.myButton10)
        h_box.addWidget(self.myButton11)
        
        #h_box.addStretch()
        #Layout for vertical widgets
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.myLabel3)
        v_box.addWidget(self.myLabel)
        v_box.addWidget(self.myLabel4)
        v_box.addWidget(self.myLabel2)
        v_box.addWidget(self.slider)
        v_box.addLayout(h_box)
        

        self.setLayout(v_box)
        self.setGeometry(300,300,500,400)	#Places the window in certain position with certain dimensions

        # create connection between signal (click) and slot (stuff in parens)
        self.myButton.clicked.connect(self.btn_click)
        self.myButton2.clicked.connect(self.btn_click2)
        self.myButton3.clicked.connect(self.btn_click3)
        self.myButton4.clicked.connect(self.btn_click4)
        self.myButton5.clicked.connect(self.btn_click5)
        self.myButton6.clicked.connect(self.btn_click6)
        self.myButton7.clicked.connect(self.btn_click7)
        self.myButton8.clicked.connect(self.btn_click8)
        self.myButton9.clicked.connect(self.btn_click9)
        self.myButton10.clicked.connect(self.btn_click10)
        self.myButton11.clicked.connect(self.btn_click11)	#VLC

        #Creates window two when you click then button for downloading
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

    def btn_click3(self):		#Switches images
        self.imgSwitch -= 1
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))

    def btn_click4(self):
        self.imgSwitch += 1
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + str(self.imgSwitch) + ".png"))

    def btn_click5(self):		#Used to switch colors with counter so that the rest for the functions work with it
        self.colSwitch += 1
        if(self.colSwitch == 8):
            self.colSwitch = 0
        self.myLabel.setStyleSheet("color:rgb" + str(self.colors[self.ranColor]) + "; font-family: " + str(self.fonts[self.ranFont]) + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")
        self.myButton5.setText(self.colArray[self.colSwitch+1])

    def btn_click6(self):		#Changes font size, entire style sheet is needed each time or there will be a loss in the style sheet
        self.fontSize += 2
        if(self.fontSize > 30):
            self.fontSize = 11
        self.myLabel.setStyleSheet("color:rgb" + str(self.colors[self.ranColor]) + "; font-family: " + str(self.fonts[self.ranFont]) + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")

    def btn_click7(self):		#Moves the lyrics over by incrememted amount
        self.padding += 4
        if(self.padding > 20):
            self.padding = 0
        self.myLabel.setStyleSheet("color:rgb" + str(self.colors[self.ranColor]) + "; font-family: " + str(self.fonts[self.ranFont]) + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")

    def btn_click8(self):		#Sets color to random
        self.ranColor = random.randint(0,12)
        self.myLabel.setStyleSheet("color:rgb" + str(self.colors[self.ranColor]) + "; font-family: " + str(self.fonts[self.ranFont]) + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")

    def btn_click9(self):		#Sets font to random
        self.ranFont = random.randint(0,6)
        self.myLabel.setStyleSheet("color:rgb" + str(self.colors[self.ranColor]) + "; font-family: " + str(self.fonts[self.ranFont]) + "; font-size: " + str(self.fontSize) + "pt; " + "padding: " + str(self.padding) + "px;")

    def btn_click10(self):		#Opens second window
        self.dialogTextBrowser.exec_()

    def btn_click11(self):		#Starts music
        self.p = vlc.MediaPlayer("music")
        self.p.stop()
        self.p.play()
        self.slider.setSliderPosition(0)

    def valuec(self):			#Dynamically changes the lyrics and timestamp based on the position of the slider
        self.slider.setMaximum(len(lyrics)-1)
        size = self.slider.value()
        #print(self.slider.sliderPosition())
        self.myLabel.setText(lyrics[size])
        self.myLabel2.setText(timeStamp[size])  #timestamp




# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
a_window.show()
sys.exit(app.exec_())
