#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from file_manager.vhdl_reader import Vhdl_reader
from decorator.pdfdrawer import PdfDrawer
from tools.options import Options


"""
pyVhdl2Sch takes a .vhd file and return a pdf : name_of_the_entity.pdf.
"""
options = Options()
files = []

nb_args = len(sys.argv)
if nb_args == 1:
    print "No vhdl file given !"
    print "Usage : \n pyV2S.py filename.vhd"

    print " **** Enter Demo Mode **** "
    options.verbose = True
    options.color = "red"
    filename = "datas/test_files/demo.vhd"
    reader = Vhdl_reader(filename, options)
    drawer = PdfDrawer("%s.pdf" % reader.entity.name, reader.entity, options)
    print "The schematic was generated and named : %s.pdf" % reader.entity.name
else:
    options.verbose = False
    options.color = "black"

    # Analyse options
    for i in range(1, nb_args):

        if sys.argv[i]== "-v":
            options.verbose = True
            continue

        if "-fg" in sys.argv[i]:
            options.color = sys.argv[i].strip("-fg")

        if "-fg" in sys.argv[i]:
            options.background_color = sys.argv[i].strip("-fg")
            

        files.append(sys.argv[i])


    for i in range(1, len(files)):
        # ignore all options sentences
#        if "-" in sys.argv[i] :
#            continue
        
        filename = str(sys.argv[i])
        reader = Vhdl_reader(filename, options)
        drawer = PdfDrawer("%s.pdf" % reader.entity.name, reader.entity, options)
        print "The schematic was generated and named : %s.pdf" % reader.entity.name
