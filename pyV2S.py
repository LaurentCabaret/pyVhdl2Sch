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

options.analyse_args(sys.argv)

for i in range(0, len(options.files)):
    filename = options.files[i]
    try:
        os.path.isfile(filename)
    except:
        print("File do not exist!\n")
        options.print_usage()
        sys.exit

    reader = Vhdl_reader(filename, options)
    options.filename = "%s." % reader.entity.name + "%s" % options.format
    drawer = PdfDrawer("%s." % reader.entity.name + "%s" %
                       options.format, reader.entity, options)

    print(("The schematic was generated and named : %s." % reader.entity.name + "%s" % options.format))
