import os
import sys

# set the NEMA driver path to the system
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(('../ST7735'))

import NEMA_Driver as Nema # to use the disable and enable functions easier
import Ford_ST7735 as FST7735
import Main_Program as main # to use the main programs methods
import sqlite3
from time import sleep
from PyQt5.uic import*
from PyQt5 import QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import cv2

db_file_name ="Ford_Data.db"
db_exist=os.path.exists(db_file_name)

class Login_Screen(QDialog):
    def __init__(self):
        super(Login_Screen, self).__init__()
        loadUi("Login.ui", self)
        self.login.clicked.connect(self.GoToLogin)
        self.create.clicked.connect(self.GoToCreate)
        
    def GoToLogin(self):
        login_Screen = Login_Screen_2()
        widget.addWidget(login_Screen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def GoToCreate(self):
        create_Screen = Create_Screen()
        widget.addWidget(create_Screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Login_Screen_2(QDialog):
    def __init__(self):
        super(Login_Screen_2, self).__init__()
        loadUi("Login_2.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.Login)
        self.back.clicked.connect(self.GoBack)
        
    def Login(self):
        username = self.usernamefield.text()
        password = self.passwordfield.text()
        
        if db_exist:
            print("database Exists")
            if(len(username) == 0 or len(password) == 0):
                self.errormessage.setText("Error: check all input fields")
            else:
                conn = sqlite3.connect(db_file_name)
                cursor = conn.cursor()
                query1 = 'SELECT Pass_Word FROM Employee WHERE User_Name = \''+username+"\'"
                query2 = 'SELECT User_Name FROM Employee WHERE User_Name = \''+username+"\'"
                cursor.execute(query1)
                result_pass1 = cursor.fetchone()
                cursor.execute(query2)
                result_pass2 = cursor.fetchone()

                if (result_pass2):
                    if result_pass1[0] == password:
                        print("Succesfully logged in.")
                        main_screen = Main_Screen()
                        widget.addWidget(main_screen)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                        widget.setFixedWidth(1000)
                        widget.setFixedHeight(730)
                    else:
                        self.errormessage.setText("Error: incorrect username and password")
                    conn.close()
                else:
                    print("error")
        elif (db_exist == False):
            self.errormessage.setText("Error: NULL, create an account")
    
    def GoBack(self):
        previous_screen = Login_Screen()
        widget.addWidget(previous_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Create_Screen(QDialog):
    def __init__(self):
        super(Create_Screen, self).__init__()
        loadUi("Create.ui", self)
        self.newPasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create.clicked.connect(self.CreateAccount)
        self.back.clicked.connect(self.GoBack)
    
    def CreateAccount(self):
        newUsername = self.newUsernameField.text()
        newPassword = self.newPasswordField.text()
        confirmPassword = self.confirmPassField.text()
        accessCode = self.newAccessCodeField.text()
        
        if db_exist:
            print("database Exists")
            if(len(newUsername) == 0 or len(newPassword) == 0 or len(confirmPassword) == 0 or len(accessCode) == 0):
                self.errormessage.setText("Error: check all input fields")
            elif newPassword!=confirmPassword:
                self.errormessage.setText("Error: Passwords are not the same")
            else:
                conn = sqlite3.connect(db_file_name)
                cursor = conn.cursor()
                query1 = 'SELECT Access_Code FROM Employee WHERE User_Name = \'''Test'"\'"
                cursor.execute(query1)
                result_pass1 = cursor.fetchone()
                if(str(accessCode) == result_pass1[0]):
                    clearance = 2
                else:
                    print(result_pass1[0])
                    clearance = 1
                new_info = [newUsername,newPassword,accessCode,clearance]
                cursor.execute("INSERT INTO Employee VALUES (?,?,?,?)",new_info)
                conn.commit()
                conn.close()
                print("Succesfully created account.")
                print(clearance)
                main_screen = Main_Screen()
                widget.addWidget(main_screen)
                widget.setCurrentIndex(widget.currentIndex()+1)
                widget.setFixedWidth(1000)
                widget.setFixedHeight(700)

        elif (db_exist == False):
            self.errormessage.setText("Error: NULL, create an account")


    def GoBack(self):
        previous_screen = Login_Screen()
        widget.addWidget(previous_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Main_Screen(QMainWindow):
    def __init__(self):
        super(Main_Screen,self).__init__()
        loadUi("Main.ui",self)
        self.pasue_Video_Button.clicked.connect(self.Pause_Video)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker2 = Worker2()
        self.Worker2.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.widget.setFixedWidth(1000)
        self.widget.setFixedHeight(750)
        self.show_Run_Button.clicked.connect(self.Show_Run_TFT)
        self.show_IP_Button.clicked.connect(self.Show_IP_TFT)
        self.R2_DPWM_Set_Button.clicked.connect(self.Set_R2_DPWM)
        self.R1_DPWM_Set_Button.clicked.connect(self.Set_R1_DPWM)
        self.Led_On.clicked.connect(self.TurnLEDOn)
        self.Led_Off.clicked.connect(self.TurnLEDOff)
        self.Lcd_On.clicked.connect(self.TurnLCDOn)
        self.Lcd_Off.clicked.connect(self.TurnLCDOff)
        self.enable_Motors.clicked.connect(self.TurnMotorsOn)
        self.disable_Motors.clicked.connect(self.TurnMotorsOff)
        self.Start_Main.clicked.connect(self.Start_Program)
        self.Stop_Main.clicked.connect(self.Stop_Program)
        self.increment_X.clicked.connect(self.Increment_X)
        self.increment_Y.clicked.connect(self.Increment_Y)
        self.increment_Z.clicked.connect(self.Increment_Z)
        self.decrement_X.clicked.connect(self.Decrement_X)
        self.decrement_Y.clicked.connect(self.Decrement_Y)
        self.decrement_Z.clicked.connect(self.Decrement_Z)
        self.home_Button.clicked.connect(self.Home_All)
        self.get_Readings.clicked.connect(self.Get_Reading)
        self.speed_Slider.valueChanged.connect(self.Set_Speed_Label)
        self.distance_Slider.valueChanged.connect(self.Set_Distance_Label)
        
    def Set_R1_DPWM(self):
        main.dspwmr1 = self.R1_DPWM_Text_Box.text()
        
    def Set_R2_DPWM(self):
        main.dspwmr2 = self.R2_DPWM_Text_Box.text()
        
    def TurnLEDOn(self):
        main.turn_LED_On()
        self.LED_Light.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.LED_Light.setText("ON")
        
    def TurnLEDOff(self):
        main.turn_LED_Off()
        self.LED_Light.setStyleSheet("background-color:rgb(193, 193, 193)")
        self.LED_Light.setText("OFF")
        
    def TurnLCDOn(self):
        main.turn_LCD_On()
        self.LCD_Light.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.LCD_Light.setText("ON")
        
    def TurnLCDOff(self):
        main.turn_LCD_Off()
        self.LCD_Light.setStyleSheet("background-color:rgb(193, 193, 193)")
        self.LCD_Light.setText("OFF")
        
    def TurnMotorsOn(self):
        main.enable_Motors()
        self.Motors_Light.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.Motors_Light.setText("ON")
        
    def TurnMotorsOff(self):
        main.disable_Motors()
        self.Motors_Light.setStyleSheet("background-color:rgb(193, 193, 193)")
        self.Motors_Light.setText("OFF")
        
    def Start_Program():
        main.start_Program()
        
    def Stop_Program():
        main.stop_program()
        
    def Increment_X(self):
        speed = self.speed_Slider.value()
        distance = self.distance_Slider.value()
        main.set_Speed(speed)
        main.set_Distance(distance)
        main.increment_X()
        
    def Increment_Y(self):
        speed = self.speed_Slider.value()
        distance = self.distance_Slider.value()
        main.set_Speed(speed)
        main.set_Distance(distance)
        main.increment_Y()
        
    def Increment_Z(self):
        speed = self.speed_Slider.value()
        distance = self.distance_Slider.value()
        main.set_Speed(speed)
        main.set_Distance(distance)
        main.increment_Z()
        
    def Decrement_X(self):
        speed = self.speed_Slider.value()
        distance = self.distance_Slider.value()
        main.set_Speed(speed)
        main.set_Distance(distance)
        main.decrement_X()
        
    def Decrement_Y(self):
        speed = self.speed_Slider.value()
        distance = self.distance_Slider.value()
        main.set_Speed(speed)
        main.set_Distance(distance)
        main.decrement_Y()
        
    def Decrement_Z(self):
        speed = self.speed_Slider.value()
        distance = self.distance_Slider.value()
        main.set_Speed(speed)
        main.set_Distance(distance)
        main.decrement_Z()
        
    def Home_All():
        main.home()
        
    def Get_Reading(self):
        main.get_Reading()
        
    def Set_Speed_Label(self):
        self.Speed_Text.setText("SPD: = " + str(self.speed_Slider.value()))
        
    def Set_Distance_Label(self):
        self.Distance_Text.setText("DST: = " + str(self.distance_Slider.value()))
        
    def ImageUpdateSlot(self, Image):
        self.camera_Display.setPixmap(QPixmap.fromImage(Image))
        
    def Pause_Video(self):
        self.Worker1.Pause_Video()
    
    def Show_IP_TFT():
        FST7735.Check_Info()
    
    def Show_Run_TFT():
        FST7735.Run()
        
    def Show_Home_TFT():
        FST7735.Home()
    
    def Show_Menu_TFT():
        FST7735.Intro()
        
    def Show_Main_Menu_TFT():
        FST7735.Draw_Main_Menu()
        
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
                Pic = convertToQtFormat.scaled(640,480,Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def Pause_Video(self):
        self.quit()

class Worker2(QThread):
    def run(self):
        self.ThreadActive = True
        FST7735.Intro()
        FST7735.Draw_Main_Menu()
        self.quit()


# main
app = QApplication(sys.argv)
welcome = Login_Screen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(600)
widget.setFixedHeight(400)

widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")