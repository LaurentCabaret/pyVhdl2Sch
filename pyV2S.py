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
    options.color = "black"
    options.background_color = "white"
    options.transparency = 0
    options.format ="pdf"        
    filename = "datas/test_files/demo.vhd"
    reader = Vhdl_reader(filename, options)
    options.filename = "%s." % reader.entity.name + "%s" % options.format
    drawer = PdfDrawer(
            "%s." % reader.entity.name + "%s" % options.format, reader.entity, options)
    print "The schematic was generated and named : %s.pdf" % reader.entity.name
else:
    options.verbose = False
    options.color = "black"
    options.background_color = "white"
    options.transparency = 0
    options.format ="pdf"
    options.width =1000
    # Analyse options
    for i in range(1, nb_args):

        if "-" in sys.argv[i]:
            if "-v" in sys.argv[i]:
                options.verbose = True

            if "-fg" in sys.argv[i]:
                options.color = sys.argv[i].strip("-fg")

            if "-bg" in sys.argv[i]:
                options.background_color = sys.argv[i].replace("-bg", "")
                options.transparency = 1

            if "-ft" in sys.argv[i]:
                options.format = sys.argv[i].replace("-ft", "")

            if "-w" in sys.argv[i]:
                options.width = float(sys.argv[i].replace("-w", ""))

        else:
            files.append(sys.argv[i])

    if len(files) == 0:
        print_usage()
        
    for i in range(0, len(files)):
        filename = files[i]
        reader = Vhdl_reader(filename, options)
        options.filename = "%s." % reader.entity.name + "%s" % options.format
        drawer = PdfDrawer(
            "%s." % reader.entity.name + "%s" % options.format, reader.entity, options)
        print "The schematic was generated and named : %s." % reader.entity.name + "%s" % options.format
