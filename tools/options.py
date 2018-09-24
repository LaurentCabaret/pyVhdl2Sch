#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


class Options:

    def __init__(self):
        self.color = "black"
        self.verbose = False
        self.background_color = "white"
        self.transparency = 1
        self.filename = ""
        self.format = "pdf"
        self.width = 500
        self.files = []
        pass

    def no_args_go_demo(self):
        print("No vhdl file given !")
        print("Usage : \n pyV2S.py filename.vhd")

        print(" **** Enter Demo Mode **** ")
        self.files.append("datas/test_files/demo.vhd")

    def analyse_args(self, args):
        nb_args = len(args)
        if nb_args == 1:
            self.no_args_go_demo()
        else:
            for i in range(1, nb_args):

                if "-" in args[i]:
                    if "-v" in args[i]:
                        self.verbose = True

                    if "-fg" in args[i]:
                        self.color = args[i].strip("-fg")

                    if "-bg" in args[i]:
                        self.background_color = args[i].replace("-bg", "")
                        self.transparency = 1

                    if "-ft" in args[i]:
                        self.format = args[i].replace("-ft", "")

                    if "-w" in args[i]:
                        self.width = float(args[i].replace("-w", ""))

                else:
                    self.files.append(args[i])

        if len(self.files) == 0:
            self.print_usage()

    def print_usage(self):
        print(" --- Usage: ----")
        print(" -v : verbose mode")
        print("-fg : foreground color -- example '-fgred' or '-fg#123456'")
        print("-bg : background color -- example '-bgred' or '-bg#123456'")
        print("      !! important if -bg is not present background is transparent in png mode")
        print("-ft : format mode, pdf, svg, ps, png -- example : '-ftpng'")
        print(" -w : width of the image in pixels -- only usefull for png format")
        print("")
        print("example : ")
        print("     ./pyV2S.py -v -ftpng -w1000 -fgred -bgblue testfile.vhd")
