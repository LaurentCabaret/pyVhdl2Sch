#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

from file_manager.flat_vhdl_reader import Vhdl_reader
from decorator.tbGenerator import TestBenchGenerator
from tools.options import Options

fenetre = Tk()
options = Options()
files = []

label = Label(fenetre, text="Hello World")
label.pack()

class vhdl_container(object):
    """docstring for vhdl_container"""
    def __init__(self, arg, root):
        super(vhdl_container, self).__init__()
        self.inT = Text(root, height=40, width=60)
        self.outT = Text(root, height=40, width=60)
        self.inT.pack(side=LEFT, fill=Y)
        self.outT.pack(side=RIGHT, fill=Y)
        self.arg = arg


    def process(self):
        text = self.inT.get(1.0, END)
        reader = Vhdl_reader(text)
        print reader.entity.name
        self.TestBenchGenerator = TestBenchGenerator("yop",reader.entity)

        self.outT.delete(1.0, END)
        self.outT.insert(END, self.TestBenchGenerator.text)

vhdl_text = vhdl_container("toto", fenetre)

options.analyse_args(sys.argv)

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# bouton de sortie
Generate=Button(fenetre, text="generate", command=vhdl_text.process)
Generate.pack()

# checkbutton
bouton = Checkbutton(fenetre, text="Test_bench?")
bouton.pack()



fenetre.mainloop()
