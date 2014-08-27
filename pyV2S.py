#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from file_manager.vhdl_reader import Vhdl_reader
from decorator.pdfdrawer import PdfDrawer

import sys

try:
	filename = str(sys.argv[1])
except:
	filename = "datas/test_files/demo.vhd"

reader = Vhdl_reader(filename)

drawer = PdfDrawer("%s.pdf" % reader.entity.name, reader.entity)

print "The schematic was generated and named : %s.pdf" % reader.entity.name