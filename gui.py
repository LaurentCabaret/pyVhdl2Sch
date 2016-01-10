# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1044, 674)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(3840, 2048))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit_Input = QtGui.QTextEdit(self.tab)
        self.textEdit_Input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_Input.setObjectName(_fromUtf8("textEdit_Input"))
        self.horizontalLayout.addWidget(self.textEdit_Input)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_LoadFile = QtGui.QPushButton(self.groupBox)
        self.pushButton_LoadFile.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_LoadFile.setObjectName(_fromUtf8("pushButton_LoadFile"))
        self.verticalLayout.addWidget(self.pushButton_LoadFile)
        self.pushButton_Analyse = QtGui.QPushButton(self.groupBox)
        self.pushButton_Analyse.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_Analyse.setObjectName(_fromUtf8("pushButton_Analyse"))
        self.verticalLayout.addWidget(self.pushButton_Analyse)
        self.pushButton_Drawsch = QtGui.QPushButton(self.groupBox)
        self.pushButton_Drawsch.setObjectName(_fromUtf8("pushButton_Drawsch"))
        self.verticalLayout.addWidget(self.pushButton_Drawsch)
        spacerItem = QtGui.QSpacerItem(20, 430, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textEdit_TB = QtGui.QTextEdit(self.tab_2)
        self.textEdit_TB.setGeometry(QtCore.QRect(10, 10, 661, 491))
        self.textEdit_TB.setObjectName(_fromUtf8("textEdit_TB"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.graphicsView = QtGui.QGraphicsView(self.tab_3)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 501, 491))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyVHDL2STE", None))
        self.groupBox.setTitle(_translate("MainWindow", "Tools", None))
        self.pushButton_LoadFile.setText(_translate("MainWindow", "Load file", None))
        self.pushButton_Analyse.setText(_translate("MainWindow", "Analyze", None))
        self.pushButton_Drawsch.setText(_translate("MainWindow", "Generate Sch", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "VHDL Input Code", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "TestBench VHDL Code", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "SchOptions", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

