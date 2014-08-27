#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from file_manager.vhdl_reader import Vhdl_reader
from decorator.pdfdrawer import PdfDrawer

import sys

nb_args = len(sys.argv)
if nb_args == 1:
	print "No vhdl file given !"
	print "Usage : \n pyV2S.py filename.vhd"

	print " **** Enter Demo Mode **** "
	filename = "datas/test_files/demo.vhd"
	reader = Vhdl_reader(filename)
	drawer = PdfDrawer("%s.pdf" % reader.entity.name, reader.entity)
	print "The schematic was generated and named : %s.pdf" % reader.entity.name
else:
	for i in range(1, nb_args):
		filename = str(sys.argv[i])
		reader = Vhdl_reader(filename)
		drawer = PdfDrawer("%s.pdf" % reader.entity.name, reader.entity)
		print "The schematic was generated and named : %s.pdf" % reader.entity.name