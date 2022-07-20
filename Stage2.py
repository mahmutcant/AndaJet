import math
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from Stage3 import stage3
from PyQt5.QtGui import QDoubleValidator
class stage2(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("Stage2.ui",self)
        self.BtnOnceki.clicked.connect(self.onceki)
        self.BtnOnceki.setStyleSheet("QPushButton::hover{background-color:transparent;color:lightseagreen}"
                                      "QPushButton{background-color:transparent}")
        QWidget.setFixedSize(self,690,407)
        self.txtSes.textChanged.connect(self.Hesapla)
        self.p01.hide()
        self.M1.hide()
        self.m1.hide()
        self.alfa.hide()
        self.Rm.hide()
        self.gama.hide()
        self.Vx1.hide()
        self.BtnSonraki.clicked.connect(self.Sonraki)
        self.BtnSonraki.setStyleSheet("QPushButton::hover{background-color:transparent;color:lightseagreen}"
                                      "QPushButton{background-color:transparent}")
        self.sonraki=stage3()
        QWidget.setStyleSheet(self, "QLineEdit{border:2px solid transparent;border-radius:9px}")
        self.txtTs1_T01.setPlaceholderText("Ts1=T01")
        self.txtSes.setPlaceholderText("15 derecedeki ses hızı")
        self.txtSes.setValidator(QDoubleValidator(self))
    def onceki(self):
        self.close()
    def Hesapla(self):
        ses=self.txtSes.text()
        Vx2=self.txtVx2.text()
        T01=float(self.txtTs1_T01.text())
        gama=float(self.gama.text())
        p01=float(self.p01.text())
        P02=float(self.txtP02_P01.text())
        Vx1=float(self.Vx1.text())
        Rm=float(self.Rm.text())
        R2_R1=float(self.txtR2.text())
        Vx2_Vx1=float(self.txtVx2_Vx1.text())
        m1=float(self.m1.text())
        try:
            M2=float(Vx2)/float(ses)
        except:
            M2=0.0
        self.txtM2.setText(str(M2))
        try:
           Ts2=T01/(1+(gama-1)/2*(M2**2))
        except:
           Ts2=0.0
        self.txtTs2.setText(str(Ts2))
        try:
            a2=(gama*287*Ts2)**0.5
        except:
            a2=0.0
        self.txta2.setText(str(a2))
        try:
            V2=M2*a2
        except:
            V2=0.0
        self.txtV2.setText(str(V2))
        try:
            P02_1=p01*P02
        except:
            P02_1=0.0
        self.txtP02.setText(str(P02_1))
        try:
            Rm2=Rm*R2_R1
        except:
            Rm2=0.0
        self.txtRm2.setText(str(Rm2))
        try:
            Vx2_2=Vx1*(Vx2_Vx1)
        except:
            Vx2_2=0.0
        self.txtVx2_2.setText(str(Vx2_2))
        try:
            Ps2=float(self.txtP02.text())/(T01/Ts2)**3
        except:
            Ps2=0.0
        self.txtPs2.setText(str(Ps2))
        try:
            g2=float(self.txtP02.text())/((0.287)*(Ts2))
        except:
            g2=0.0
        self.txtg2.setText(str(g2))
        try:
            Vy2=((V2)**2-(Vx2_2)**2)**0.5
        except:
            Vy2=0.0
        self.txtVy2.setText(str(Vy2))
        try:
            a=math.atan(Vy2/Vx2_2)
            alfa2=math.degrees(a)
        except:
            alfa2=0.0
        self.txtAlfa2.setText(str(alfa2))
        try:
            U2=(math.pi/30)*(15000)*(Rm2)
        except:
            U2=0.0
        self.txtU2.setText(str(U2))
        try:
            Wy2=Vy2-U2
        except:
            Wy2=0.0
        self.txtWy2.setText(str(Wy2))
        try:
            W2=(Wy2**2-(-(Vx2_2**2)))**0.5
        except:
            W2=0.0
        self.txtW2.setText(str(W2))
        try:
            Area2=m1/(g2*Vx2_2)
        except:
            Area2=0.0
        self.txtArea2.setText(str(Area2))
        try:
            H2=Area2/(2*math.pi*Rm2)
        except:
            H2=0.0
        self.txtH2.setText(str(H2))
        try:
            Rt2=Rm2+(H2/2)
        except:
            Rt2=0.0
        self.txtRt2.setText(str(Rt2))
        try:
            Rh2=Rm2-(H2/2)
        except:
            Rh2=0.0
        self.txtRh2.setText(str(Rh2))
        try:
            b=math.atan(Wy2/Vx2_2)
            beta2=math.degrees(b)
        except:
            beta2=0.0
        self.txtBeta2.setText(str(beta2))
    def Sonraki(self):
        self.sonraki.show()
        ses = self.txtSes.text()
        Vx2 = self.txtVx2.text()
        T01 = float(self.txtTs1_T01.text())
        gama = float(self.gama.text())
        p01 = float(self.p01.text())
        P02 = float(self.txtP02_P01.text())
        Vx1 = float(self.Vx1.text())
        Rm = float(self.Rm.text())
        R2_R1 = float(self.txtR2.text())
        Vx2_Vx1 = float(self.txtVx2_Vx1.text())
        m1 = float(self.m1.text())
        try:
            M2 = float(Vx2) / float(ses)
        except:
            M2 = 0.0
        self.txtM2.setText(str(M2))
        try:
            Ts2 = T01 / (1 + (gama - 1) / 2 * (M2 ** 2))
        except:
            Ts2 = 0.0
        self.txtTs2.setText(str(Ts2))
        try:
            a2 = (gama * 287 * Ts2) ** 0.5
        except:
            a2 = 0.0
        self.txta2.setText(str(a2))
        try:
            V2 = M2 * a2
        except:
            V2 = 0.0
        self.txtV2.setText(str(V2))
        try:
            P02_1 = p01 * P02
        except:
            P02_1 = 0.0
        self.txtP02.setText(str(P02_1))
        try:
            Rm2 = Rm * R2_R1
        except:
            Rm2 = 0.0
        self.txtRm2.setText(str(Rm2))
        try:
            Vx2_2 = Vx1 * (Vx2_Vx1)
        except:
            Vx2_2 = 0.0
        self.txtVx2_2.setText(str(Vx2_2))
        try:
            Ps2 = float(self.txtP02.text()) / (T01 / Ts2) ** 3
        except:
            Ps2 = 0.0
        self.txtPs2.setText(str(Ps2))
        try:
            g2 = float(self.txtP02.text()) / ((0.287) * (Ts2))
        except:
            g2 = 0.0
        self.txtg2.setText(str(g2))
        try:
            Vy2 = ((V2) ** 2 - (Vx2_2) ** 2) ** 0.5
        except:
            Vy2 = 0.0
        self.txtVy2.setText(str(Vy2))
        try:
            a = math.atan(Vy2 / Vx2_2)
            alfa2 = math.degrees(a)
        except:
            alfa2 = 0.0
        self.txtAlfa2.setText(str(alfa2))
        try:
            U2 = (math.pi / 30) * (15000) * (Rm2)
        except:
            U2 = 0.0
        self.txtU2.setText(str(U2))
        try:
            Wy2 = Vy2 - U2
        except:
            Wy2 = 0.0
        self.txtWy2.setText(str(Wy2))
        try:
            W2 = (Wy2 ** 2 - (-(Vx2_2 ** 2))) ** 0.5
        except:
            W2 = 0.0
        self.txtW2.setText(str(W2))
        try:
            Area2 = m1 / (g2 * Vx2_2)
        except:
            Area2 = 0.0
        self.txtArea2.setText(str(Area2))
        try:
            H2 = Area2 / (2 * math.pi * Rm2)
        except:
            H2 = 0.0
        self.txtH2.setText(str(H2))
        try:
            Rt2 = Rm2 + (H2 / 2)
        except:
            Rt2 = 0.0
        self.txtRt2.setText(str(Rt2))
        try:
            Rh2 = Rm2 - (H2 / 2)
        except:
            Rh2 = 0.0
        self.txtRh2.setText(str(Rh2))
        try:
            b = math.atan(Wy2 / Vx2_2)
            beta2 = math.degrees(b)
        except:
            beta2 = 0.0
        self.txtBeta2.setText(str(beta2))
        try:
            self.sonraki.gama.setText(gama)
        except:
            self.sonraki.gama.setText("0.0")
        try:
            self.sonraki.Ts2.setText(Ts2)
        except:
            self.sonraki.Ts2.setText("0.0")
        try:
            self.sonraki.Ps2.setText(Ps2)
        except:
            self.sonraki.Ps2.setText("0.0")
        try:
            self.sonraki.p02_p01.setText(P02)
        except :
            self.sonraki.p02_p01.setText("0.0")
        try:
            self.sonraki.W2.setText(W2)
        except:
            self.sonraki.W2.setText("0.0")
        try:
            Mr2=W2/(gama*287*Ts2)**0.5
        except:
            Mr2=0.0
        try:
            self.sonraki.txtMr2.setText(str(Mr2))
        except:
            self.sonraki.txtMr2.setText("0.0")
        try:
            T0r2=Ts2*(1+((gama-1)/2)*Mr2**2)
        except:
            T0r2=0.0
        try:
            self.sonraki.txtT0r2.setText(str(T0r2))
        except:
            self.sonraki.txtT0r2.setText("0.0")
        try:
            P0r2=Ps2*((T0r2/Ts2)**(gama/(gama-1)))
        except:
            P0r2=0.0
        try:
            self.sonraki.txtP0r2.setText(str(P0r2))
        except:
            self.sonraki.txtP0r2.setText("0.0")
        try:
            POr3=P0r2*(P02)
        except:
            POr3=0.0
        try:
            self.sonraki.txtPOr3.setText(str(POr3))
        except:
            self.sonraki.txtPOr3.setText(str(POr3))
        try:
            Vx3=Vx2_2*Vx2_Vx1
        except:
            Vx3=0.0
        try:
            self.sonraki.txtVx3.setText(str(Vx3))
        except:
            self.sonraki.txtVx3.setText("0.0")
        try:
            Rm3=Rm2*R2_R1
        except:
            Rm3=0.0
        try:
            self.sonraki.txtRm3.setText(str(Rm3))
        except:
            self.sonraki.txtRm3.setText("0.0")
        try:
            U3=(math.pi/30)*15000*Rm3
        except:
            U3=0.0
        try:
            self.sonraki.txtU3.setText(str(U3))
        except:
            self.sonraki.txtU3.setText("0.0")
        self.sonraki.U2.setText(str(U2))
        self.sonraki.Vy2.setText(str(Vy2))
        self.sonraki.gama.setText(str(gama))
        self.sonraki.m1.setText(self.m1.text())
        self.sonraki.P01.setText(self.p01.text())
        self.sonraki.T01.setText(str(T01))