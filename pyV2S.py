#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from file_manager.vhdl_reader import Vhdl_reader
from decorator.pdfdrawer import PdfDrawer

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filename = str(sys.argv[1])

reader = Vhdl_reader(filename)

drawer = PdfDrawer("%s.pdf" % reader.entity.name, reader.entity)