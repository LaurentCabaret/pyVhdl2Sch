#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from file_manager.vhdl_reader import Vhdl_reader
from decorator.pdfdrawer import PdfDrawer
from decorator.tbGenerator import TestBenchGenerator
from tools.options import Options


"""
pyVhdl2Sch takes a .vhd file and return a testbench : tb_name_of_the_entity.vhd.
"""
options = Options()
files = []

options.analyse_args(sys.argv)

for i in range(0, len(options.files)):
    filename = options.files[i]
    try:
        os.path.isfile(filename)
    except:
        print "File do not exist!\n"
        options.print_usage()
        sys.exit

    reader = Vhdl_reader(filename, options)
    options.filename = "%s." % reader.entity.name + "%s" % options.format

    testbench = TestBenchGenerator(
        "tb_%s" % reader.entity.name + ".vhd", reader.entity)

    print "The testbench was generated and named : tb_%s." % reader.entity.name + "vhd"
