# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(711, 520)
        self.BtnHesapla = QtWidgets.QPushButton(Form)
        self.BtnHesapla.setGeometry(QtCore.QRect(140, 350, 81, 31))
        self.BtnHesapla.setObjectName("BtnHesapla")
        self.BtnIptal = QtWidgets.QPushButton(Form)
        self.BtnIptal.setGeometry(QtCore.QRect(340, 350, 81, 31))
        self.BtnIptal.setObjectName("BtnIptal")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 301))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 167, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 165, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(11, 145, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(7, 183, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 181, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(11, 258, 159, 16))
        self.label_7.setObjectName("label_7")
        self.txtT01 = QtWidgets.QLineEdit(self.groupBox)
        self.txtT01.setGeometry(QtCore.QRect(192, 41, 133, 20))
        self.txtT01.setObjectName("txtT01")
        self.txtP01 = QtWidgets.QLineEdit(self.groupBox)
        self.txtP01.setGeometry(QtCore.QRect(192, 77, 133, 20))
        self.txtP01.setObjectName("txtP01")
        self.txtM1 = QtWidgets.QLineEdit(self.groupBox)
        self.txtM1.setGeometry(QtCore.QRect(192, 113, 133, 20))
        self.txtM1.setObjectName("txtM1")
        self.txtm1 = QtWidgets.QLineEdit(self.groupBox)
        self.txtm1.setGeometry(QtCore.QRect(192, 149, 133, 20))
        self.txtm1.setObjectName("txtm1")
        self.txtAlfa = QtWidgets.QLineEdit(self.groupBox)
        self.txtAlfa.setGeometry(QtCore.QRect(192, 185, 133, 20))
        self.txtAlfa.setObjectName("txtAlfa")
        self.txtRm = QtWidgets.QLineEdit(self.groupBox)
        self.txtRm.setGeometry(QtCore.QRect(192, 221, 133, 20))
        self.txtRm.setObjectName("txtRm")
        self.txtGama = QtWidgets.QLineEdit(self.groupBox)
        self.txtGama.setGeometry(QtCore.QRect(192, 257, 133, 20))
        self.txtGama.setObjectName("txtGama")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 10, 321, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.txtTs1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtTs1.setGeometry(QtCore.QRect(181, 31, 133, 20))
        self.txtTs1.setReadOnly(True)
        self.txtTs1.setObjectName("txtTs1")
        self.txtPs1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtPs1.setGeometry(QtCore.QRect(181, 57, 133, 20))
        self.txtPs1.setReadOnly(True)
        self.txtPs1.setObjectName("txtPs1")
        self.txtg1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtg1.setGeometry(QtCore.QRect(181, 83, 133, 20))
        self.txtg1.setReadOnly(True)
        self.txtg1.setObjectName("txtg1")
        self.txta1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txta1.setGeometry(QtCore.QRect(181, 109, 133, 20))
        self.txta1.setReadOnly(True)
        self.txta1.setObjectName("txta1")
        self.txtV1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtV1.setGeometry(QtCore.QRect(181, 135, 133, 20))
        self.txtV1.setReadOnly(True)
        self.txtV1.setObjectName("txtV1")
        self.txtH1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtH1.setGeometry(QtCore.QRect(181, 213, 133, 20))
        self.txtH1.setReadOnly(True)
        self.txtH1.setObjectName("txtH1")
        self.txtRt = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtRt.setGeometry(QtCore.QRect(181, 239, 133, 20))
        self.txtRt.setReadOnly(True)
        self.txtRt.setObjectName("txtRt")
        self.txtRh = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtRh.setGeometry(QtCore.QRect(181, 265, 133, 20))
        self.txtRh.setReadOnly(True)
        self.txtRh.setObjectName("txtRh")
        self.txtArea1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtArea1.setGeometry(QtCore.QRect(181, 187, 133, 20))
        self.txtArea1.setReadOnly(True)
        self.txtArea1.setObjectName("txtArea1")
        self.txtVx1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtVx1.setGeometry(QtCore.QRect(181, 161, 133, 20))
        self.txtVx1.setReadOnly(True)
        self.txtVx1.setObjectName("txtVx1")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(11, 34, 168, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(11, 60, 166, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 85, 171, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(11, 111, 161, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(11, 213, 161, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(11, 187, 161, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(11, 136, 161, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(11, 162, 161, 16))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(11, 264, 161, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(11, 238, 161, 16))
        self.label_18.setObjectName("label_18")
        self.BtnTemizle = QtWidgets.QPushButton(Form)
        self.BtnTemizle.setGeometry(QtCore.QRect(240, 350, 81, 31))
        self.BtnTemizle.setObjectName("BtnTemizle")
        self.BtnSonraki = QtWidgets.QPushButton(Form)
        self.BtnSonraki.setGeometry(QtCore.QRect(460, 360, 221, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BtnSonraki.setFont(font)
        self.BtnSonraki.setStyleSheet("")
        self.BtnSonraki.setObjectName("BtnSonraki")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txtT01, self.txtP01)
        Form.setTabOrder(self.txtP01, self.txtM1)
        Form.setTabOrder(self.txtM1, self.txtm1)
        Form.setTabOrder(self.txtm1, self.txtAlfa)
        Form.setTabOrder(self.txtAlfa, self.txtRm)
        Form.setTabOrder(self.txtRm, self.txtGama)
        Form.setTabOrder(self.txtGama, self.BtnHesapla)
        Form.setTabOrder(self.BtnHesapla, self.BtnIptal)
        Form.setTabOrder(self.BtnIptal, self.txtg1)
        Form.setTabOrder(self.txtg1, self.txtPs1)
        Form.setTabOrder(self.txtPs1, self.txtTs1)
        Form.setTabOrder(self.txtTs1, self.txtV1)
        Form.setTabOrder(self.txtV1, self.txtH1)
        Form.setTabOrder(self.txtH1, self.txtRt)
        Form.setTabOrder(self.txtRt, self.txtRh)
        Form.setTabOrder(self.txtRh, self.txtArea1)
        Form.setTabOrder(self.txtArea1, self.txtVx1)
        Form.setTabOrder(self.txtVx1, self.txta1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ana Sayfa"))
        self.BtnHesapla.setText(_translate("Form", "Hesapla"))
        self.BtnIptal.setText(_translate("Form", "İptal"))
        self.groupBox.setTitle(_translate("Form", "Girilecek Değerler"))
        self.label.setText(_translate("Form", "T01 (Çıkış anındaki sıcaklık değeri) :"))
        self.label_2.setText(_translate("Form", "P01 (Çıkış anındaki basınç değeri) :"))
        self.label_3.setText(_translate("Form", "                         M1 (Mach Sayısı) : "))
        self.label_4.setText(_translate("Form", "            m1 (Kütlesel debi ağırlığı) : "))
        self.label_5.setText(_translate("Form", "                                              alfa : "))
        self.label_6.setText(_translate("Form", "Rm (Aft çapının uzunluğu) :"))
        self.label_7.setText(_translate("Form", "                                         gama : "))
        self.groupBox_2.setTitle(_translate("Form", "Stage 1 Sonuçlar"))
        self.label_8.setText(_translate("Form", "Ts1 (Giriş anındaki sıcaklık değeri) : "))
        self.label_9.setText(_translate("Form", "Ps1 (Giriş anındaki basınç değeri) : "))
        self.label_10.setText(_translate("Form", "                                                g1 : "))
        self.label_11.setText(_translate("Form", "                                                a1 : "))
        self.label_12.setText(_translate("Form", "                                               H1 : "))
        self.label_13.setText(_translate("Form", "                                          Area1 : "))
        self.label_14.setText(_translate("Form", "                                                V1 : "))
        self.label_15.setText(_translate("Form", "                                              Vx1 :"))
        self.label_17.setText(_translate("Form", "                                               Rh : "))
        self.label_18.setText(_translate("Form", "                                                Rt : "))
        self.BtnTemizle.setText(_translate("Form", "Temizle"))
        self.BtnSonraki.setText(_translate("Form", "Sonraki Sayfa >"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
