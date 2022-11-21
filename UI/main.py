import os
import sys
import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
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
    def Login(self):
        username = self.usernamefield.text()
        password = self.passwordfield.text()
        
        if db_exist:
            print("database Exists")
        if (db_exist == False):
            print("Database Does not exist: Creating new database")
            conn = sqlite3.connect(db_file_name)
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE Employee (User_name TEXT, Pass_Word TEXT, Clearance INTEGER)")
            self.errormessage.setText("Error: NULL")
            widget.setCurrentIndex(widget.currentIndex()-1)
            conn.close()

        
        if(len(username) == 0 or len(password) == 0):
            self.errormessage.setText("Error: check all input fields")
        else:
            conn = sqlite3.connect(db_file_name)
            cursor = conn.cursor()
            query = 'SELECT Pass_Word FROM Employee WHERE User_name = \''+username+"\'"
            cursor.execute(query)
            result_pass = cursor.fetchone()[0]
            if result_pass == password:
                print("Succesfully logged in.")
            else:
                self.errormessage.setText("Error: incorrect username and password")
            conn.close()

class Create_Screen(QDialog):
    def __init__(self):
        super(Create_Screen, self).__init__()
        loadUi("Create.ui", self)
        self.back.clicked.connect(self.GoBack)
    def GoBack(self):
        print("Back pressed")

class Main_Screen(QMainWindow):
    def __init__(self):
        super(Main_Screen,self)._init__()
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