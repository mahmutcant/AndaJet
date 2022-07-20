import sys
from PyQt5.QtWidgets import QApplication
from Anda_Jet import Giris
app=QApplication([])
window=Giris()
window.show()
app.exec()