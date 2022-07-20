from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from HesapSayfasi import AnaSayfa
from Eksenelitki import Eksenel
class Secenek(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("secenek.ui",self)
        QWidget.setFixedSize(self,400,300)
        self.hesapla=AnaSayfa()
        self.hesapla2=Eksenel()
        self.btnYapisal.clicked.connect(self.yapisal)
        self.btnItki.clicked.connect(self.itki)
        self.btnYapisal.setStyleSheet("QPushButton::hover{border:1px solid #0078d4;border-radius:15px;background-color:#e0eef9}"
                                      "QPushButton{border:1px solid #d0d0d0;border-radius:15px;background-color:#fdfdfd}")
        self.btnItki.setStyleSheet("QPushButton::hover{border:1px solid #0078d4;border-radius:15px;background-color:#e0eef9}"
                                      "QPushButton{border:1px solid #d0d0d0;border-radius:15px;background-color:#fdfdfd}")
        self.pixmap=QPixmap("imza.png")
        self.label_2.setPixmap(self.pixmap)
    def yapisal(self):
        self.hesapla.show()
    def itki(self):
        self.hesapla2.show()