import sys
from time import sleep
from PyQt5.uic import*
from PyQt5 import QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import cv2
class Main_Screen(QMainWindow):
    def __init__(self):
        super(Main_Screen,self).__init__()
        loadUi("Main.ui",self)
        self.pasue_Video_Button.clicked.connect(self.Pause_Video)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
    def ImageUpdateSlot(self, Image):
        self.camera_Display.setPixmap(QPixmap.fromImage(Image))
    def Pause_Video(self):
        self.Worker1.Pause_Video()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image,1)
                convertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1],FlippedImage.shape[0],QImage.Format_RGB888)
                Pic = convertToQtFormat.scaled(450,260,Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def Pause_Video(self):
        self.quit()
# main
app = QApplication(sys.argv)
welcome = Main_Screen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1000)
widget.setFixedHeight(720)

widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")