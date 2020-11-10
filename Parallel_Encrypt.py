# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Parallel_Encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import Images.clear
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(592, 380)
        widget.setMaximumSize(QtCore.QSize(640, 380))
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.frameOut = QtWidgets.QFrame(widget)
        self.frameOut.setEnabled(True)
        self.frameOut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameOut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOut.setObjectName("frameOut")
        self.label = QtWidgets.QLabel(self.frameOut)
        self.label.setGeometry(QtCore.QRect(180, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.grbox_ToolFile = QtWidgets.QGroupBox(self.frameOut)
        self.grbox_ToolFile.setGeometry(QtCore.QRect(30, 50, 161, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grbox_ToolFile.setFont(font)
        self.grbox_ToolFile.setObjectName("grbox_ToolFile")
        self.frameTool = QtWidgets.QFrame(self.grbox_ToolFile)
        self.frameTool.setGeometry(QtCore.QRect(0, 10, 171, 111))
        self.frameTool.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTool.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTool.setObjectName("frameTool")
        self.toolButton_2 = QtWidgets.QToolButton(self.frameTool)
        self.toolButton_2.setGeometry(QtCore.QRect(50, 60, 61, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/floppy-disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(18, 18))
        self.toolButton_2.setObjectName("toolButton_2")
        self.btnFileOpen = QtWidgets.QToolButton(self.frameTool)
        self.btnFileOpen.setGeometry(QtCore.QRect(50, 10, 61, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnFileOpen.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/folder (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFileOpen.setIcon(icon1)
        self.btnFileOpen.setIconSize(QtCore.QSize(20, 20))
        self.btnFileOpen.setObjectName("btnFileOpen")
        self.frameType = QtWidgets.QFrame(self.frameOut)
        self.frameType.setGeometry(QtCore.QRect(30, 170, 161, 81))
        self.frameType.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameType.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameType.setObjectName("frameType")
        self.grbox_Types = QtWidgets.QGroupBox(self.frameType)
        self.grbox_Types.setGeometry(QtCore.QRect(0, 0, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grbox_Types.setFont(font)
        self.grbox_Types.setObjectName("grbox_Types")
        self.rdo_Enc = QtWidgets.QRadioButton(self.grbox_Types)
        self.rdo_Enc.setGeometry(QtCore.QRect(20, 20, 82, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rdo_Enc.setFont(font)
        self.rdo_Enc.setObjectName("rdo_Enc")
        self.rdo_Dec = QtWidgets.QRadioButton(self.grbox_Types)
        self.rdo_Dec.setGeometry(QtCore.QRect(20, 50, 81, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rdo_Dec.setFont(font)
        self.rdo_Dec.setObjectName("rdo_Dec")
        self.btnSequential = QtWidgets.QPushButton(self.frameOut)
        self.btnSequential.setGeometry(QtCore.QRect(30, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSequential.setFont(font)
        self.btnSequential.setObjectName("btnSequential")
        self.btnParallel = QtWidgets.QPushButton(self.frameOut)
        self.btnParallel.setGeometry(QtCore.QRect(30, 310, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnParallel.setFont(font)
        self.btnParallel.setObjectName("btnParallel")
        self.lineTextSequent = QtWidgets.QLineEdit(self.frameOut)
        self.lineTextSequent.setEnabled(False)
        self.lineTextSequent.setGeometry(QtCore.QRect(110, 260, 81, 41))
        self.lineTextSequent.setObjectName("lineTextSequent")
        self.lineTextParar = QtWidgets.QLineEdit(self.frameOut)
        self.lineTextParar.setEnabled(False)
        self.lineTextParar.setGeometry(QtCore.QRect(110, 310, 81, 41))
        self.lineTextParar.setObjectName("lineTextParar")
        self.btnSave = QtWidgets.QPushButton(self.frameOut)
        self.btnSave.setGeometry(QtCore.QRect(280, 300, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSave.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon2)
        self.btnSave.setObjectName("btnSave")
        self.frameOut_2 = QtWidgets.QFrame(self.frameOut)
        self.frameOut_2.setEnabled(True)
        self.frameOut_2.setGeometry(QtCore.QRect(480, 340, 574, 362))
        self.frameOut_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameOut_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOut_2.setObjectName("frameOut_2")
        self.label_2 = QtWidgets.QLabel(self.frameOut_2)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.grbox_ToolFile_2 = QtWidgets.QGroupBox(self.frameOut_2)
        self.grbox_ToolFile_2.setGeometry(QtCore.QRect(30, 50, 161, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grbox_ToolFile_2.setFont(font)
        self.grbox_ToolFile_2.setObjectName("grbox_ToolFile_2")
        self.frameTool_2 = QtWidgets.QFrame(self.grbox_ToolFile_2)
        self.frameTool_2.setGeometry(QtCore.QRect(0, 10, 171, 111))
        self.frameTool_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTool_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTool_2.setObjectName("frameTool_2")
        self.btnFileOpen_2 = QtWidgets.QToolButton(self.frameTool_2)
        self.btnFileOpen_2.setGeometry(QtCore.QRect(34, 10, 71, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnFileOpen_2.setFont(font)
        self.btnFileOpen_2.setObjectName("btnFileOpen_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frameTool_2)
        self.toolButton_3.setGeometry(QtCore.QRect(34, 60, 71, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setObjectName("toolButton_3")
        self.frameType_2 = QtWidgets.QFrame(self.frameOut_2)
        self.frameType_2.setGeometry(QtCore.QRect(30, 170, 161, 81))
        self.frameType_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameType_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameType_2.setObjectName("frameType_2")
        self.grbox_Types_2 = QtWidgets.QGroupBox(self.frameType_2)
        self.grbox_Types_2.setGeometry(QtCore.QRect(0, 0, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grbox_Types_2.setFont(font)
        self.grbox_Types_2.setObjectName("grbox_Types_2")
        self.rdo_Enc_2 = QtWidgets.QRadioButton(self.grbox_Types_2)
        self.rdo_Enc_2.setGeometry(QtCore.QRect(20, 20, 82, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rdo_Enc_2.setFont(font)
        self.rdo_Enc_2.setObjectName("rdo_Enc_2")
        self.rdo_Dec_2 = QtWidgets.QRadioButton(self.grbox_Types_2)
        self.rdo_Dec_2.setGeometry(QtCore.QRect(20, 50, 81, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rdo_Dec_2.setFont(font)
        self.rdo_Dec_2.setObjectName("rdo_Dec_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frameOut_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(310, 60, 211, 221))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.btnSequential_2 = QtWidgets.QPushButton(self.frameOut_2)
        self.btnSequential_2.setGeometry(QtCore.QRect(30, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSequential_2.setFont(font)
        self.btnSequential_2.setObjectName("btnSequential_2")
        self.btnParallel_2 = QtWidgets.QPushButton(self.frameOut_2)
        self.btnParallel_2.setGeometry(QtCore.QRect(30, 310, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnParallel_2.setFont(font)
        self.btnParallel_2.setObjectName("btnParallel_2")
        self.lineTextSequent_2 = QtWidgets.QLineEdit(self.frameOut_2)
        self.lineTextSequent_2.setEnabled(False)
        self.lineTextSequent_2.setGeometry(QtCore.QRect(110, 260, 81, 41))
        self.lineTextSequent_2.setObjectName("lineTextSequent_2")
        self.lineTextParar_2 = QtWidgets.QLineEdit(self.frameOut_2)
        self.lineTextParar_2.setEnabled(False)
        self.lineTextParar_2.setGeometry(QtCore.QRect(110, 310, 81, 41))
        self.lineTextParar_2.setObjectName("lineTextParar_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frameOut_2)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 300, 91, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frameOut_2)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 110, 91, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.btnClear = QtWidgets.QPushButton(self.frameOut)
        self.btnClear.setGeometry(QtCore.QRect(430, 300, 91, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Images/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClear.setIcon(icon3)
        self.btnClear.setIconSize(QtCore.QSize(17, 17))
        self.btnClear.setObjectName("btnClear")
        self.tableWidget = QtWidgets.QTableWidget(self.frameOut)
        self.tableWidget.setGeometry(QtCore.QRect(255, 60, 291, 231))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"background-color: #F2F5A9;\n"
"alternate-background-color: #CEECF5;\n"
"selection-background-color: #81DAF5;\n"
"}")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        self.gridLayout.addWidget(self.frameOut, 0, 1, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)
        widget.setTabOrder(self.toolButton_2, self.btnFileOpen)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Pararrel Encrypt"))
        self.label.setText(_translate("widget", "Parallel Encrypt"))
        self.grbox_ToolFile.setTitle(_translate("widget", "Tool File"))
        self.toolButton_2.setText(_translate("widget", "File Save"))
        self.btnFileOpen.setText(_translate("widget", "File Open"))
        self.grbox_Types.setTitle(_translate("widget", "Types"))
        self.rdo_Enc.setText(_translate("widget", "Encrypt"))
        self.rdo_Dec.setText(_translate("widget", "Decrypt"))
        self.btnSequential.setText(_translate("widget", "Sequential"))
        self.btnParallel.setText(_translate("widget", "Parallel"))
        self.btnSave.setText(_translate("widget", "Save"))
        self.label_2.setText(_translate("widget", "Parallel encrypt"))
        self.grbox_ToolFile_2.setTitle(_translate("widget", "Tool File"))
        self.btnFileOpen_2.setText(_translate("widget", "File Open"))
        self.toolButton_3.setText(_translate("widget", "File Save"))
        self.grbox_Types_2.setTitle(_translate("widget", "Types"))
        self.rdo_Enc_2.setText(_translate("widget", "Encrypt"))
        self.rdo_Dec_2.setText(_translate("widget", "Decrypt"))
        self.btnSequential_2.setText(_translate("widget", "Sequential"))
        self.btnParallel_2.setText(_translate("widget", "Parallel"))
        self.pushButton_2.setText(_translate("widget", "PushButton"))
        self.pushButton_3.setText(_translate("widget", "PushButton"))
        self.btnClear.setText(_translate("widget", "Clear"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("widget", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("widget", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("widget", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("widget", "4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("widget", "Types"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("widget", "Sequential"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("widget", "Pararrel"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("widget", "Encrypt"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("widget", "0.150"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("widget", "0.02"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("widget", "Decrypt"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("widget", "12.4"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("widget", "5.01"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
