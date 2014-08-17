#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class Vhdl_reader:

    def __init__(self, filename):
        self.long_file_name = filename
        self.extract_file_name(self.long_file_name)
        
        self.file = None

        self.open_file()
        self.entity_name = ""
        self.extract_entity_name()
        self.verbose()
        self.close_file()



    def open_file(self):
      self.file = open(self.long_file_name, "r")
      pass

    def close_file(self):
      self.file.close()
      pass

    def extract_entity_name(self):
        for ligne in self.file:
            words = ligne.split()
            if len(words)>1:
                if "entity" in words[0].lower():
                    self.entity_name = words[1]

    def extract_file_name(self, long_file_name):
        self.filename = long_file_name.split("/")[-1]

    def verbose(self):
        print "input file: %s" % self.filename
        print "entity name: %s" % self.entity_name