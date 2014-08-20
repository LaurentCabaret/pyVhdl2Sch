#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from file_manager.vhdl_reader import Vhdl_reader
from decorator.pdfdrawer import PdfDrawer


reader = Vhdl_reader("datas/test_files/demo.vhd")

drawer = PdfDrawer("datas/generated_files/demo.pdf", reader.entity)