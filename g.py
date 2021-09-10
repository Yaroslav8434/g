from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl
from PyQt5 import Qt
from pathlib import Path
import os
from glob import glob

path = Path.home() / "Music"
os.chdir(path)
g = glob('*.mp3')

app = Qt.QCoreApplication([])
media_player = QtMultimedia.QMediaPlayer()
url = QUrl.fromLocalFile("")



def play():
    content = QtMultimedia.QMediaContent(url)
    media_player.setMedia(content)
    media_player.play()


def stop():
    content = QtMultimedia.QMediaContent(url)
    media_player.setMedia(content)
    media_player.stop()


def volume(setVolume):
    content = QtMultimedia.QMediaContent(url)
    media_player.setMedia(content)
    media_player.setVolume(setVolume)



app.exec()