import time
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator
import math
from Stage2 import stage2
class AnaSayfa(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("AnaSayfa.ui",self)
        QWidget.setFixedSize(self,691,520)
        self.BtnTemizle.clicked.connect(self.Temizle)
        self.txtT01.editingFinished.connect(self.Hesapla)
        self.txtP01.editingFinished.connect(self.Hesapla)
        self.txtM1.editingFinished.connect(self.Hesapla)
        self.txtm1.editingFinished.connect(self.Hesapla)
        self.txtAlfa.editingFinished.connect(self.Hesapla)
        self.txtRm.editingFinished.connect(self.Hesapla)
        self.txtGama.textChanged.connect(self.Hesapla)
        self.txtT01.setValidator(QDoubleValidator(self))
        self.txtP01.setValidator(QDoubleValidator(self))
        self.txtM1.setValidator(QDoubleValidator(self))
        self.txtm1.setValidator(QDoubleValidator(self))
        self.txtAlfa.setValidator(QDoubleValidator(self))
        self.txtRm.setValidator(QDoubleValidator(self))
        self.txtGama.setValidator(QDoubleValidator(self))
        self.sayfa2=stage2()
        self.BtnSonraki.clicked.connect(self.sonraki)
        self.BtnIptal.clicked.connect(self.close)

        self.BtnTemizle.setStyleSheet("QPushButton::hover{border-radius:10px; border:1px solid green; background:green;color:white}"
                                      "QPushButton{border-radius:10px; border:1px solid green; color:black}")
        self.BtnIptal.setStyleSheet("QPushButton::hover{background-color:transparent;color:lightseagreen}"
                                      "QPushButton{background-color:transparent;color:black}")
        self.BtnSonraki.setStyleSheet("QPushButton::hover{background-color:transparent;color:lightseagreen}"
                                      "QPushButton{background-color:transparent;color:black}")
        QWidget.setStyleSheet(self,"QLineEdit{border:2px solid transparent;border-radius:9px}")
        self.txtT01.setPlaceholderText("T01")
        self.txtP01.setPlaceholderText("P01")
        self.txtM1.setPlaceholderText("M1")
        self.txtm1.setPlaceholderText("m1")
        self.txtAlfa.setPlaceholderText("alfa")
        self.txtRm.setPlaceholderText("Rm")
        self.txtGama.setPlaceholderText("gama")
        self.txtTs1.setPlaceholderText("Ts1")
        self.txtPs1.setPlaceholderText("Ps1")
        self.txtg1.setPlaceholderText("g1")
        self.txta1.setPlaceholderText("a1")
        self.txtV1.setPlaceholderText("V1")
        self.txtVx1.setPlaceholderText("Vx1")
        self.txtArea1.setPlaceholderText("Area1")
        self.txtH1.setPlaceholderText("H1")
        self.txtRt.setPlaceholderText("Rt")
        self.txtRh.setPlaceholderText("Rt")
    def Hesapla(self):
        T01 = self.txtT01.text()
        if(len(T01)==0):
            T01="0.0"
            self.txtT01.setText("")
        P01 = self.txtP01.text()
        if(len(P01)==0):
            P01="0.0"
            self.txtP01.setText("")
        M1 = self.txtM1.text()
        if(len(M1)==0):
            M1="0.0"
            self.txtM1.setText("")
        m1 = self.txtm1.text()
        if(len(m1)==0):
            m1="0.0"
            self.txtm1.setText("")
        alfa =self.txtAlfa.text()
        if(len(alfa)==0):
            alfa="0.0"
            self.txtAlfa.setText("")
        Rm = self.txtRm.text()
        if(len(Rm)==0):
            Rm="0.0"
            self.txtRm.setText("")
        gama = self.txtGama.text()
        if(len(gama)==0):
            gama="0.0"
            self.txtGama.setText("")
        try:
            Ts1=float(T01)/(1+(float(gama)-1)/2*(float(M1)**2))
        except ZeroDivisionError:
            Ts1=0.0
        try:
            Ps1=float(P01)/(float(T01)/float(Ts1))**3
        except ZeroDivisionError:
            Ps1=0.0
        try:
            g1=float(Ps1)*1000/(287*float(Ts1))
        except ZeroDivisionError:
            g1=0.0
        try:
            a1=(float(gama)*287*Ts1)**0.5
        except ZeroDivisionError:
            a1=0.0
        try:
            V1=float(M1)*a1
        except ZeroDivisionError:
            V1=0.0
        Vx1=V1
        try:
            Area1=float(m1)/(float(g1)*float(Vx1))
        except ZeroDivisionError:
            Area1=0.0
        try:
            H1=float(Area1 / (math.pi * 2 * float(Rm)))
        except ZeroDivisionError:
            H1=0.0
        try:
            Rt=float(Rm)+(H1/2)
        except ZeroDivisionError:
            Rt=0.0
        try:
            Rh=float(Rm)-(H1/2)
        except ZeroDivisionError:
            Rh=0.0
        self.txtTs1.setText(str(Ts1))
        self.txtPs1.setText(str(Ps1))
        self.txtg1.setText(str(g1))
        self.txta1.setText(str(a1))
        self.txtV1.setText(str(V1))
        self.txtVx1.setText(str(Vx1))
        self.txtArea1.setText(str(Area1))
        self.txtH1.setText(str(H1))
        self.txtRt.setText(str(Rt))
        self.txtRh.setText(str(Rh))
    def Temizle(self):
        self.txtT01.setText("")
        self.txtP01.setText("")
        self.txtM1.setText("")
        self.txtm1.setText("")
        self.txtAlfa.setText("")
        self.txtRm.setText("")
        self.txtGama.setText("")
        self.txtTs1.setText("")
        self.txtPs1.setText("")
        self.txtg1.setText("")
        self.txta1.setText("")
        self.txtV1.setText("")
        self.txtVx1.setText("")
        self.txtVx1.setText("")
        self.txtArea1.setText("")
        self.txtH1.setText("")
        self.txtRt.setText("")
        self.txtRh.setText("")

    def sonraki(self):
        T01 = self.txtT01.text()
        if (len(T01) == 0):
            T01 = "0.0"
            self.txtT01.setText("0.0")
        P01 = self.txtP01.text()
        if (len(P01) == 0):
            P01 = "0.0"
            self.txtP01.setText("0.0")
        M1 = self.txtM1.text()
        if (len(M1) == 0):
            M1 = "0.0"
            self.txtM1.setText("0.0")
        m1 = self.txtm1.text()
        if (len(m1) == 0):
            m1 = "0.0"
            self.txtm1.setText("0.0")
        alfa = self.txtAlfa.text()
        if (len(alfa) == 0):
            alfa = "0.0"
            self.txtAlfa.setText("0.0")
        Rm = self.txtRm.text()
        if (len(Rm) == 0):
            Rm = "0.0"
            self.txtRm.setText("0.0")
        gama = self.txtGama.text()
        if (len(gama) == 0):
            gama = "0.0"
            self.txtGama.setText("0.0")
        try:
            Ts1 = float(T01) / (1 + (float(gama) - 1) / 2 * (float(M1) ** 2))
        except ZeroDivisionError:
            Ts1 = 0.0
        try:
            Ps1 = float(P01) / (float(T01) / float(Ts1)) ** 3
        except ZeroDivisionError:
            Ps1 = 0.0
        try:
            g1 = float(Ps1) * 1000 / (287 * float(Ts1))
        except ZeroDivisionError:
            g1 = 0.0
        try:
            a1 = (float(gama) * 287 * Ts1) ** 0.5
        except ZeroDivisionError:
            a1 = 0.0
        try:
            V1 = float(M1) * a1
        except ZeroDivisionError:
            V1 = 0.0
        Vx1 = V1
        try:
            Area1 = float(m1) / (float(g1) * float(Vx1))
        except ZeroDivisionError:
            Area1 = 0.0
        try:
            H1 = float(Area1 / (math.pi * 2 * float(Rm)))
        except ZeroDivisionError:
            H1 = 0.0
        try:
            Rt = float(Rm) + (H1 / 2)
        except ZeroDivisionError:
            Rt = 0.0
        try:
            Rh = float(Rm) - (H1 / 2)
        except ZeroDivisionError:
            Rh = 0.0

        self.txtTs1.setText(str(Ts1))
        self.txtPs1.setText(str(Ps1))
        self.txtg1.setText(str(g1))
        self.txta1.setText(str(a1))
        self.txtV1.setText(str(V1))
        self.txtVx1.setText(str(Vx1))
        self.txtArea1.setText(str(Area1))
        self.txtH1.setText(str(H1))
        self.txtRt.setText(str(Rt))
        self.txtRh.setText(str(Rh))
        self.sayfa2.show()
        self.sayfa2.txtTs1_T01.setText(str(T01))
        self.sayfa2.p01.setText(P01)
        self.sayfa2.M1.setText(M1)
        self.sayfa2.m1.setText(m1)
        self.sayfa2.alfa.setText(alfa)
        self.sayfa2.Rm.setText(Rm)
        self.sayfa2.gama.setText(gama)
        self.sayfa2.Vx1.setText(str(Vx1))
        try:
            Vx2=float(Vx1)*0.97
        except ZeroDivisionError:
            Vx2=0.0
        self.sayfa2.txtVx2.setText(str(Vx2))
        try:
            P02=float(Ps1)/float(P01)
        except ZeroDivisionError:
            P02=0.0
        self.sayfa2.txtP02_P01.setText(str(P02))
        try:
            R2=float(Rt)/float(Rh)
        except ZeroDivisionError:
            R2=0.0
        self.sayfa2.txtR2.setText(str(R2))
        try:
            Vx2_Vx1=Vx2/Vx1
        except ZeroDivisionError:
            Vx2_Vx1=0.0
        self.sayfa2.txtVx2_Vx1.setText(str(Vx2_Vx1))


