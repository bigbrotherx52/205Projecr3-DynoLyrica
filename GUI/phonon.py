import os
from PyQt5 import QApplication
from PyQt5.phonon import Phonon

app = QApplication([])
app.setApplicationName('Phonon Video Player')

#file_path = os.path.join(os.path.dirname(__file__), '320x240.ogv')
file_path = os.path.join(os.path.dirname(__file__), 'FolgersCoffe_512kb_mp4_026vbr260.ogv')
media_src = Phonon.MediaSource(file_path)

media_obj = Phonon.MediaObject()
media_obj.setCurrentSource(media_src)

video_widget = Phonon.VideoWidget()
Phonon.createPath(media_obj, video_widget)

audio_out = Phonon.AudioOutput(Phonon.VideoCategory)
Phonon.createPath(media_obj, audio_out)

video_widget.show()

media_obj.play()

app.exec_()
