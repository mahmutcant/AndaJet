import math
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
class Eksenel(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("itki.ui",self)
        self.txtre2i.editingFinished.connect(self.Hesapla)
        #self.txtre2i.textChanged.connect(self.Hesapla)
        self.txtre2o.editingFinished.connect(self.Hesapla)
        self.txtPes1.editingFinished.connect(self.Hesapla)
        self.txtPes2.editingFinished.connect(self.Hesapla)
        self.txtre1i.editingFinished.connect(self.Hesapla)
        self.txtre1o.textChanged.connect(self.Hesapla)
        self.txtAei.editingFinished.connect(self.Hesapla)
        self.txtAeo.textChanged.connect(self.Hesapla)
        self.txtPhs1.editingFinished.connect(self.Hesapla2)
        self.txtPhe2.editingFinished.connect(self.Hesapla2)
        self.txtrh1i.editingFinished.connect(self.Hesapla2)
        self.txtrh1o.textChanged.connect(self.Hesapla2)
        #self.txtW41.editingFinished.connect(self.Hesapla3)
        self.txtPmi.editingFinished.connect(self.Hesapla3)
        self.txtPmo.textChanged.connect(self.Hesapla3)
        self.pushButton.clicked.connect(self.onceki)
        self.txtre2i.setValidator(QDoubleValidator(self))
        self.txtre2o.setValidator(QDoubleValidator(self))
        self.txtPes1.setValidator(QDoubleValidator(self))
        self.txtPes2.setValidator(QDoubleValidator(self))
        self.txtre1i.setValidator(QDoubleValidator(self))
        self.txtre1o.setValidator(QDoubleValidator(self))
        self.pushButton.setStyleSheet("QPushButton::hover{background-color:transparent;color:lightseagreen}"
                                      "QPushButton{background-color:transparent;color:black}")
        QWidget.setStyleSheet(self,"QLineEdit{border:2px solid transparent;border-radius:9px}")

    def Hesapla(self):
        if(len(self.txtre2o.text())==0):
            txtre2o=0.0
        else:
            txtre2o=float(self.txtre2o.text())
        if(len(self.txtre2i.text())==0):
            txtre2i=0.0
        else:
            txtre2i=float(self.txtre2i.text())
        if(len(self.txtPes1.text())==0):
            txtPes1=0.0
        else:
            txtPes1=float(self.txtPes1.text())
        if(len(self.txtPes2.text())==0):
            txtPes2=0.0
        else:
            txtPes2=float(self.txtPes2.text())
        if(len(self.txtre1i.text())==0):
            txtre1i=0.0
        else:
            txtre1i=float(self.txtre1i.text())
        if(len(self.txtre1o.text())==0):
            txtre1o=0.0
        else:
            txtre1o=float(self.txtre1o.text())
        try:
            txtAei=((txtre2i)**2-(txtre1i)**2)*math.pi
        except:
            txtAei=0.0
        self.txtAei.setText(str(txtAei))
        try:
            txtAeo=((txtre2o**2)-(txtre1o**2))*math.pi
        except:
            txtAeo=0.0
        self.txtAeo.setText(str(txtAeo))
        try:
            txtFaxial=(txtPes1*txtAei)+(txtPes2*txtAeo*(-1))
        except:
            txtFaxial=0.0
        self.txtFaxial.setText(str(txtFaxial))
    def Hesapla2(self):
        if(len(self.txtPhs1.text())==0):
            txtPhs1=0.0
        else:
            txtPhs1=float(self.txtPhs1.text())
        if(len(self.txtPhe2.text())==0):
            txtPhe2=0.0
        else:
            txtPhe2=float(self.txtPhe2.text())
        if(len(self.txtrh1i.text())==0):
            txtrh1i=0.0
        else:
            txtrh1i=float(self.txtrh1i.text())
        if(len(self.txtrh1o.text())==0):
            txtrh1o=0.0
        else:
            txtrh1o=float(self.txtrh1o.text())
        try:
            txtAh=((txtrh1i**2)-(txtrh1o**2))*math.pi
        except:
            txtAh=0.0
        self.txtAh.setText(str(txtAh))
        try:
            txtFplatform=((txtPhs1+txtPhe2)/2)*(txtAh*(-1))
        except:
            txtFplatform=0.0
        self.txtFplatform.setText(str(txtFplatform))


    def Hesapla3(self):
        if(self.txtW41.text()==0):
            txtW41=0.0
        else:
            txtW41=float(self.txtW41.text())
        if(self.txtPmi.text()==0):
            txtPmi=0.0
        else:
            txtPmi=float(self.txtPmi.text())
        if(self.txtPmo.text()==""):
            txtPmo=0.0
        else:
            txtPmo=float(self.txtPmo.text())
        if(self.txtAei.text()==""):
            txtAei=0.0
        else:
            txtAei=float(self.txtAei.text())
        if(self.txtAeo.text()==""):
            txtAeo=0.0
        else:
            txtAeo=float(self.txtAeo.text())
        if(self.txtFplatform.text()==""):
            txtFplatform=0.0
        else:
            txtFplatform=float(self.txtFplatform.text())
        if(self.txtFaxial.text()==""):
            txtFaxial=0.0
        else:
            txtFaxial=float(self.txtFaxial.text())
        try:
            txtVi=txtW41/(txtPmi*txtAei)
        except:
            txtVi=0.0
        self.txtVi.setText(str(txtVi))
        try:
            txtVo=txtW41/(txtPmo*txtAeo)
        except:
            txtVo=0.0
        self.txtVo.setText(str(txtVo))
        try:
            txtFmoment=(txtW41*txtVi*(1))+(txtW41*txtVo*(-1))
        except:
            txtFmoment=0.0
        self.txtFmoment.setText(str(txtFmoment))
        try:
            txtFaero=txtFaxial+txtFplatform+txtFmoment
        except:
            txtFaero=0.0
        self.txtFaero.setText(str(txtFaero))

    def onceki(self):
        self.close()