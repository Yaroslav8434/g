from pathlib import Path
from PyQt5 import QtWidgets, uic
import sys
import os
from glob import glob

path = Path.home() / "Music"
os.chdir(path)
g = glob('*.mp3')
os.chdir(r"C:\Users\broar\PycharmProjects\pythonProject1")





app = QtWidgets.QApplication(sys.argv)
win = uic.loadUi("f.ui")
win.listWidget.addItem("gg")
app.exec()

