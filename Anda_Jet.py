from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
#from HesapSayfasi import AnaSayfa
from Secenek import Secenek
class Giris(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Giris.ui",self)
        self.movie=QMovie("WhatsApp-Image-2022-05-18-at-12.38.gif")
        self.image.setMovie(self.movie)
        self.movie.start()
        QMainWindow.setFixedSize(self,500,520)
        self.pushButton.clicked.connect(self.hesaplamayaBasla)
        self.pushButton.setStyleSheet("QPushButton{background-color:transparent}")
        self.sayfa=Secenek()
    def hesaplamayaBasla(self):
        self.sayfa.show()
        self.close()
