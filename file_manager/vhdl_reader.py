#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from vhdl_objects.entity import Entity
from vhdl_objects.wire import Wire
from vhdl_objects.library import Library

class Vhdl_reader:

    def __init__(self, filename):
        self.long_file_name = filename
        self.extract_file_name(self.long_file_name)
        
        self.file = None
        self.entity = None
        self.entity_bloc = ""

        self.open_file()
        self.entity = Entity()
        self.extract_entity_name()
        # self.parse_vhdl_file()
        self.verbose()
        self.close_file()

    def extract_file_name(self, long_file_name):
        self.filename = long_file_name.split("/")[-1]

    def parse_vhdl_file(self):
        for ligne in self.file:
            clean_line = self.clean_line(ligne)
            words = ligne.split()
            print clean_line.lower()
        pass

    def clean_line(self, text):
        words = text.split()
        clean_line = ""
        for i in range(0,len(words)):
            if words[i] == "--":
                break
            clean_line += words[i].lower() + " "
        return clean_line

    def extract_entity_name(self):
        for ligne in self.file:
            clean_line = self.clean_line(ligne)
            words = clean_line.split()
            real_words = ligne.split()
            if len(words)>1:                
                try:
                    lindex = words.index("entity")
                    self.entity.set_name(real_words[lindex+1])
                except:
                    lindex = None

        self.entity.add_input(Wire("Clk",1,"in","clk"))
        self.entity.add_input(Wire("Abs",8,"in","classic"))
        self.entity.add_output(Wire("EN",1,"out","classic"))
        self.entity.add_output(Wire("S",8,"out","classic"))
        self.entity.add_inout(Wire("Clk",1,"inout","clk"))
        self.entity.add_input(Wire("Abs",7,"in","classic"))
        self.entity.add_output(Wire("EN",1,"out","classic"))
        self.entity.add_output(Wire("S",8,"out","classic"))
        self.entity.add_input(Wire("Clk",1,"in","clk"))
        self.entity.add_input(Wire("Abs",3,"in","classic"))
        self.entity.add_output(Wire("EN ou not EN or finaly EN",1,"out","classic"))
        self.entity.add_inout(Wire("ShadowClk",8,"inout","classic"))

        pass

    def verbose(self):
        print "input file: %s" % self.filename
        print "entity name: %s" % self.entity.name
        print "%d inputs" % len(self.entity.inputs)
        for i in range(0, len(self.entity.inputs)):
            self.entity.inputs[i].verbose()
        
        print "%d outputs" % len(self.entity.outputs)
        for i in range(0, len(self.entity.outputs)):
            self.entity.outputs[i].verbose()

        print "%d inouts" % len(self.entity.inouts)
        for i in range(0, len(self.entity.inouts)):
            self.entity.inouts[i].verbose()

        pass

    def open_file(self):
        self.file = open(self.long_file_name, "r")
        pass

    def close_file(self):
        self.file.close()
        pass
