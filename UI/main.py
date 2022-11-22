import os
import sys
import sqlite3
from time import sleep
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QWidget, QStackedWidget

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
                        widget.setFixedHeight(700)
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