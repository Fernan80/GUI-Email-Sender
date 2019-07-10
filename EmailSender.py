# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jesus\Documents\GUI\EmailSender.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

#~~~~~~~~Main purpose: Insert email address and it sends you a funny video link or something. Maybe random video
# Notes: Where Email is placed: Object name = "textEdit", Class name = "QTextEdit"
 #             Picture is placed: Object name = "picture", class name = "Qlabel"
  #            Push Button is placed: Object name = "pushButton", class name = "QPushButton" '''

#Steps to get there:
   #1) First set the button to be connected to the QTextEdit where the user input is use.
   #2) Set up the function() to send an email.
   #3) Have the button execute the function() to send an email to the user input.
   #4) Send a message that it went succesful in the QLabel

   #Fun parts: 
   #1) Place a picture for the picture object()
   #2) Change the background colors and looks



from PyQt5 import QtCore, QtGui, QtWidgets

import smtplib #For actual sending function
import os #For personal email information



class Ui_MainWindow(object): 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 326)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 130, 281, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Scheherazade")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(30, 190, 111, 81))
        self.picture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picture.setFrameShadow(QtWidgets.QFrame.Plain)
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.GetHacked = QtWidgets.QLabel(self.centralwidget)
        self.GetHacked.setGeometry(QtCore.QRect(250, 190, 281, 31))
        self.GetHacked.setText("")
        self.GetHacked.setObjectName("GetHacked")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #connecting the pushButton
        self.pushButton.clicked.connect(self.addItem)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "For Neo"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Hello! Please enter your email and you will recieve a email shortly!"))
    
    
#I hid my password in the environment labled as DB_USER and DB_PASS


    def addItem(self):
        CLIENT_EMAIL= self.textEdit.text()
        self.textEdit.clear()       
        #Senction to send email. We first need a text file
        EMAIL_ADDRESS = os.environ.get('DB_USER')
        EMAIL_PASSWORD = os.environ.get('DB_PASS') 

#Setting up the SMTP with the appropriate server and port # (gmail)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp: 
            smtp.ehlo() #identitifies itself with the server
            smtp.starttls() #incrypt the traffic
            smtp.ehlo() #identify again
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = 'Greetings Neo'
            body = 'Click on the link and I will show you how deep the rabbit hole goes: https://www.youtube.com/watch?v=dQw4w9WgXcQ'

            msg = f'Subject: {subject}\n\n{body}' 
         #   when creating a email from scratch you need a header 
    
            smtp.sendmail(EMAIL_ADDRESS, CLIENT_EMAIL, msg)
                  #(SENDER, RECIEVER, msg)
    
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

