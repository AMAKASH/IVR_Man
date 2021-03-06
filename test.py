# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_ivrMan(object):
    def setupUi(self, ivrMan):
        ivrMan.setObjectName("ivrMan")
        ivrMan.resize(1116, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\../Assets/windowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ivrMan.setWindowIcon(icon)
        ivrMan.setStyleSheet("QWidget#centralwidget{\n"
                             "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.71, y2:0.528409, stop:0 rgba(85, 0, 127, 255), stop:1 rgba(97, 148, 193, 255));\n"
                             "}\n"
                             "\n"
                             "")
        ivrMan.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(ivrMan)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(170, 29, 791, 61))
        self.mainLabel.setStyleSheet("font: 57 24pt \"Roboto Medium\";color:rgb(255, 255, 255)")
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 791, 301))
        self.groupBox.setStyleSheet("QGroupBox#groupBox{\n"
                                    "    font: 57 18pt \"Roboto Medium\";color:rgb(255, 255, 255)\n"
                                    "}")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(20, 40, 761, 241))
        self.frame.setStyleSheet("font: 57 12pt \"Roboto Medium\";color:rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelOrderID = QtWidgets.QLabel(self.frame)
        self.labelOrderID.setGeometry(QtCore.QRect(40, 20, 81, 16))
        self.labelOrderID.setObjectName("labelOrderID")
        self.labelOrderDate = QtWidgets.QLabel(self.frame)
        self.labelOrderDate.setGeometry(QtCore.QRect(460, 20, 81, 16))
        self.labelOrderDate.setObjectName("labelOrderDate")
        self.labelCustomerName = QtWidgets.QLabel(self.frame)
        self.labelCustomerName.setGeometry(QtCore.QRect(40, 60, 131, 16))
        self.labelCustomerName.setObjectName("labelCustomerName")
        self.labelCustomerEmail = QtWidgets.QLabel(self.frame)
        self.labelCustomerEmail.setGeometry(QtCore.QRect(460, 60, 131, 16))
        self.labelCustomerEmail.setObjectName("labelCustomerEmail")
        self.labelOrderStatus = QtWidgets.QLabel(self.frame)
        self.labelOrderStatus.setGeometry(QtCore.QRect(460, 100, 131, 16))
        self.labelOrderStatus.setObjectName("labelOrderStatus")
        self.textEditCustomerPhone = QtWidgets.QTextEdit(self.frame)
        self.textEditCustomerPhone.setGeometry(QtCore.QRect(170, 90, 141, 31))
        self.textEditCustomerPhone.setStyleSheet("color:rgb(0, 0, 0)")
        self.textEditCustomerPhone.setObjectName("textEditCustomerPhone")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 100, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 131, 16))
        self.label_7.setObjectName("label_7")
        self.plainTextEditOderDetils = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEditOderDetils.setGeometry(QtCore.QRect(150, 140, 581, 91))
        self.plainTextEditOderDetils.setStyleSheet("color:rgb(0, 0, 0);\n"
                                                   "font: 25 10pt \"Roboto Light\";")
        self.plainTextEditOderDetils.setObjectName("plainTextEditOderDetils")
        self.labelAction = QtWidgets.QLabel(self.centralwidget)
        self.labelAction.setGeometry(QtCore.QRect(0, 440, 800, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelAction.setFont(font)
        self.labelAction.setStyleSheet("font: 57 14pt \"Roboto Medium\";color:rgb(255, 255, 255)")
        self.labelAction.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAction.setObjectName("labelAction")
        self.con_disconButton = QtWidgets.QPushButton(self.centralwidget)
        self.con_disconButton.setGeometry(QtCore.QRect(330, 480, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.con_disconButton.setFont(font)
        self.con_disconButton.setStyleSheet("QPushButton{\n"
                                            "    border-radius:10px;\n"
                                            "    background-color: rgb(0, 170, 127);\n"
                                            "    border:1px solid white;\n"
                                            "    color:white;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color: rgb(0, 150, 127);\n"
                                            "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI\\../Assets/connect2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.con_disconButton.setIcon(icon1)
        self.con_disconButton.setObjectName("con_disconButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(810, 110, 16, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(840, 130, 231, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 170)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem('Item'))
        self.mainLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel_2.setGeometry(QtCore.QRect(840, 100, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.mainLabel_2.setFont(font)
        self.mainLabel_2.setStyleSheet("font: 57 16pt \"Roboto Medium\";color:rgb(255, 255, 255)")
        self.mainLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel_2.setObjectName("mainLabel_2")
        ivrMan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ivrMan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 21))
        self.menubar.setObjectName("menubar")
        ivrMan.setMenuBar(self.menubar)
        self.con_disconButton.setFocus()

        self.retranslateUi(ivrMan)
        QtCore.QMetaObject.connectSlotsByName(ivrMan)
        self.con_disconButton.clicked.connect(self.buttonAction)

    def retranslateUi(self, ivrMan):
        _translate = QtCore.QCoreApplication.translate
        ivrMan.setWindowTitle(_translate("ivrMan", "IVR Man"))
        self.mainLabel.setText(_translate("ivrMan", "Interactive Voice Response (IVR) Manager"))
        self.groupBox.setTitle(_translate("ivrMan", "  Curent Order  "))
        self.labelOrderID.setText(_translate("ivrMan", "Order ID# "))
        self.labelOrderDate.setText(_translate("ivrMan", "Order Date: "))
        self.labelCustomerName.setText(_translate("ivrMan", "Customer Name:"))
        self.labelCustomerEmail.setText(_translate("ivrMan", "Customer Email:"))
        self.labelOrderStatus.setText(_translate("ivrMan", "Order Status:"))
        self.label_6.setText(_translate("ivrMan", "Customer Phone:"))
        self.label_7.setText(_translate("ivrMan", "Order Details:"))
        self.plainTextEditOderDetils.setPlainText(_translate("ivrMan",
                                                             "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown pri"))
        self.labelAction.setText(_translate("ivrMan", "Waiting for New Order.........."))
        self.con_disconButton.setText(_translate("ivrMan", "  Connect"))
        self.con_disconButton.setShortcut(_translate("ivrMan", "Ctrl+S"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ivrMan", "OrderID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ivrMan", "Customer Phone No."))
        self.mainLabel_2.setText(_translate("ivrMan", "Order Queue:"))
        self.tableWidget.setItem(0, 0, QTableWidgetItem('oder'))
        self.flag = True
        if self.flag:
            print(self.flag)
            self.worker()
            self.flag = False
    def buttonAction(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem('oder'))

    def worker(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(3000)


    def showTime(self):
        self.timer.stop()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem('12345'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem('01973054376'))
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.updateinfo)
        self.timer1.start(2000)


    def updateinfo(self):
        self.timer1.stop()
        self.labelOrderID.setText('Order ID# ' + '12345')
        self.labelOrderDate.setText('Order Date: ' + '24-09-2021')
        self.labelCustomerName.setText('Customer Name: ' + 'Demo Customer')
        self.labelCustomerEmail.setText('Customer Email: ' + 'demo@demo.com')
        self.labelOrderStatus.setText('Order Status: ' + 'Pending')
        self.textEditCustomerPhone.setText('0197304376')

        self.labelOrderID.adjustSize()
        self.labelOrderDate.adjustSize()
        self.labelCustomerName.adjustSize()
        self.labelCustomerEmail.adjustSize()
        self.labelOrderStatus.adjustSize()

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.initiateCall)
        self.timer2.start(2000)


    def initiateCall(self):
        self.timer2.stop()
        _translate = QtCore.QCoreApplication.translate
        self.labelAction.setText(_translate('ivrMan', 'Calling Customer....'))
        self.con_disconButton.setText(_translate('ivrMan', '  Disconnect'))

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Assets/disconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.con_disconButton.setIcon(icon1)
        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.end)
        self.timer3.start(2000)



    def end(self):
        self.timer3.stop()
        print('chicken')
        _translate = QtCore.QCoreApplication.translate

        self.tableWidget.setRowCount(0)
        self.labelAction.setText(_translate('ivrMan', 'Waiting for New Order..........'))
        self.con_disconButton.setText(_translate('ivrMan', '  Connect'))
        self.labelOrderStatus.setText('Order Status: ' + 'Confirmed')
        self.labelOrderStatus.setStyleSheet("color:rgb(0, 100, 0)")
        self.labelOrderStatus.adjustSize()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Assets/connect2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.con_disconButton.setIcon(icon1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ivrMan = QtWidgets.QMainWindow()
    ui = Ui_ivrMan()
    ui.setupUi(ivrMan)
    ivrMan.show()
    sys.exit(app.exec_())
