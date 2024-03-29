# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QScrollArea, QMessageBox
from PyQt5.QtCore import Qt
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: black;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 531, 71))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"     color: white;\n"
"     \n"
"    font: 20pt \"Segoe UI Semilight\";\n"
"}")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 130, 541, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 511, 361))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget\n"
"{\n"
      "color: white;\n"
      "font: 10pt \"SF Pro Display\";\n}")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.rawlist= str(subprocess.run('adb shell pm list package', shell=True, capture_output=True).stdout.decode())
        self.items= self.rawlist.split('\r\n')
        n=0
        for item in self.items:
            print(n)
            n+= 1
            list_item = QListWidgetItem(item.replace("package:com.", "").replace("."," ").title(), self.listWidget)
            list_item.setFlags(list_item.flags() | Qt.ItemIsUserCheckable)
            list_item.setCheckState(Qt.Unchecked)
        self.resetSel = QtWidgets.QPushButton(self.centralwidget)
        self.resetSel.setGeometry(QtCore.QRect(580, 130, 201, 61))
        self.resetSel.setStyleSheet("QPushButton\n"
"{\n"
"     color: black;\n"
"     background-color: orange;\n"
"     border-radius: 30px;\n"
"    font: 63 14pt \"Segoe UI Semibold\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"     color: black;\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(186, 122, 0, 255), stop:1 rgba(215, 206, 255, 255));\n"
"     border-radius: 25px;\n"
"    font: 63 14pt \"Segoe UI Semibold\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Buttons/reset-sel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetSel.setIcon(icon)
        self.resetSel.setObjectName("resetSel")
        self.removeSel = QtWidgets.QPushButton(self.centralwidget)
        self.removeSel.setGeometry(QtCore.QRect(580, 210, 201, 61))
        self.removeSel.setStyleSheet("QPushButton\n"
"{\n"
"     color: white;\n"
"     background-color: red;\n"
"     border-radius: 30px;\n"
"    font: 63 14pt \"Segoe UI Semibold\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"     color: white;\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"     border-radius: 25px;\n"
"    font: 63 14pt \"Segoe UI Semibold\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/Buttons/remove-apps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeSel.setIcon(icon1)
        self.removeSel.setIconSize(QtCore.QSize(40, 40))
        self.removeSel.setObjectName("removeSel")
        self.removeSel.clicked.connect(lambda: self.removeApps())
        self.reloadList = QtWidgets.QPushButton(self.centralwidget)
        self.reloadList.setGeometry(QtCore.QRect(580, 290, 211, 61))
        self.reloadList.clicked.connect(lambda: self.setupUi(MainWindow))
        self.reloadList.setStyleSheet("QPushButton\n"
"{\n"
"     color: white;\n"
"     background-color: green;\n"
"     border-radius: 30px;\n"
"    font: 63 14pt \"Segoe UI Semibold\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"     color: white;\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 195, 0, 255), stop:1 rgba(255, 255, 255, 0));\n"
"     border-radius: 25px;\n"
"    font: 63 14pt \"Segoe UI Semibold\";\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/Buttons/applist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadList.setIcon(icon2)
        self.reloadList.setIconSize(QtCore.QSize(40, 40))
        self.reloadList.setObjectName("reloadList")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 520, 781, 23))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 380, 211, 101))
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    color: white;\n"
"    \n"
"    font: 20pt \"SF Pro Display\";\n"
"}")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def removeApps(self):
      try:
        n= 0
        num= 0
        r= 0
        for item1 in self.items:
            if(self.listWidget.item(n).checkState()==Qt.Checked):
                num+= 1
            n+=1
        n=0
        print(num)
        for item in self.items:
            if(self.listWidget.item(n).checkState()==Qt.Checked):
                out= subprocess.run("adb shell pm uninstall -k --user 0 "+self.items[n].replace("package:",""),shell=True,capture_output=True)
                print(out)
                r+= 1
                self.progressBar.setValue(int(r/num*100))
                n+= 1
            else:
                n+=1
        info= QMessageBox()
        info.setWindowTitle("Done!")
        info.setText(num+" apps uninstalled successfully!")
        info.setIcon(QtGui.QIcon(QMessageBox.Information))
        info.exec_()
      except:
        info= QMessageBox()
        info.setWindowTitle("Failed!")
        info.setText("No apps were uninstalled!")
        info.setIcon(QtGui.QIcon(QMessageBox.Warning))
        info.exec_()
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select the apps you want to remove:"))
        self.resetSel.setText(_translate("MainWindow", "Reset selection"))
        self.removeSel.setText(_translate("MainWindow", "Remove apps"))
        self.reloadList.setText(_translate("MainWindow", "Reload app list"))
        self.label_2.setText(_translate("MainWindow", "TeamX \n"
"AppManager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("AppManager | v0.5 Developer Preview")
    MainWindow.show()
    sys.exit(app.exec_())
