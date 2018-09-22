#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
# from gui import Ui_MainWindow

"""
pyVHDL2... Gui
This object call all the pyVHDL2... tools
author: Laurent Cabaret
website: http://perso.ecp.fr/~cabaretl/
last edited: Januay 2016
"""
Ui_MainWindow, QtBaseClass = uic.loadUiType("gui.ui")

from file_manager.flat_vhdl_reader import Vhdl_reader
from decorator.tbGenerator import TestBenchGenerator
from tools.options import Options
from decorator.pdfdrawer import PdfDrawer

class PyVHDL_TOOLS(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_vars()
        self.init_texts()
        self.init_connexions()

    def init_texts(self):
        self.ui.textEdit_Input.setText("Paste your VHDL here code or load a file")
        self.ui.textEdit_TB.setText("No VHDL code loaded")

    def init_connexions(self):
        self.ui.pushButton_Analyse.clicked.connect(self.Analyse_vhdl_code)
        self.ui.pushButton_LoadFile.clicked.connect(self.selectFile)
        self.ui.pushButton_Drawsch.clicked.connect(self.draw_sch)
        a = 42




    def init_vars(self):
        self.Vhdl_Code = ""
        self.options = Options()
        # self.options.analyse_args(sys.argv)

    def Analyse_vhdl_code(self):
        sender = self.sender()
        self.Vhdl_Code = str(self.ui.textEdit_Input.toPlainText())
        print((self.Vhdl_Code))
        self.reader = Vhdl_reader(self.Vhdl_Code)

        self.TestBenchGenerator = TestBenchGenerator("tb_" + self.reader.entity.name + ".vhd",self.reader.entity)
        print((self.TestBenchGenerator.text))
        self.ui.textEdit_TB.setText(self.TestBenchGenerator.text)
        self.statusBar().showMessage('VHDL file is loaded')

    def selectFile(self):
        self.filename,_ = QtWidgets.QFileDialog.getOpenFileName()
        self.ui.textEdit_Input.setPlainText(open(self.filename).read())

    def draw_sch(self):
        self.options.format = "png"
        self.options.width = 1000.0
        self.options.filename = "%s." % self.reader.entity.name + "%s" % self.options.format
        print((self.options.filename))
        self.drawer = PdfDrawer("%s." % self.reader.entity.name + "%s" % self.options.format, self.reader.entity, self.options)
        del self.drawer
        # self.ui.graphicsView.set
        w_vue, h_vue = self.ui.graphicsView.width(), self.ui.graphicsView.height()


        self.current_image = QtGui.QImage(self.options.filename)

        self.fondPlan = QtGui.QPixmap.fromImage(self.current_image.scaled(w_vue, h_vue,
                                    QtCore.Qt.KeepAspectRatio,
                                    QtCore.Qt.SmoothTransformation))

        w_pix, h_pix = self.fondPlan.width(), self.fondPlan.height()
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, w_pix, h_pix)
        self.scene.addPixmap(self.fondPlan)

        self.ui.graphicsView.setScene(self.scene)

    def draw_sch_svg(self): #Ne fonctionne pas car la lib QtSvg ne supporte que TinySVG !
        self.options.format = "svg"
        self.options.filename = "%s." % self.reader.entity.name + "%s" % self.options.format
        print((self.options.filename))
        self.drawer = PdfDrawer("%s." % self.reader.entity.name + "%s" % self.options.format, self.reader.entity, self.options)
        del self.drawer
        # self.ui.graphicsView.set
        w_vue, h_vue = self.ui.graphicsView.width(), self.ui.graphicsView.height()


        # renderer = QtSvg.QSvgRenderer(QtCore.QString("InputGate.svg"))
        renderer = QtSvg.QSvgRenderer(QtCore.QString(self.options.filename))
        if not renderer.isValid():
                raise ValueError('Invalid SVG data.')

        size = renderer.defaultSize()
        image = QtWidgets.QImage(size, QtGui.QImage.Format_ARGB32)
        painter = QtWidgets.QPainter(image)
        renderer.render(painter)

        self.current_image = image

        self.fondPlan = QtWidgets.QPixmap.fromImage(self.current_image.scaled(w_vue, h_vue,
                                    QtCore.Qt.KeepAspectRatio,
                                    QtCore.Qt.SmoothTransformation))

        w_pix, h_pix = self.fondPlan.width(), self.fondPlan.height()
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, w_pix, h_pix)
        self.scene.addPixmap(self.fondPlan)

        self.ui.graphicsView.setScene(self.scene)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = PyVHDL_TOOLS()
    myapp.show()
    sys.exit(app.exec_())
