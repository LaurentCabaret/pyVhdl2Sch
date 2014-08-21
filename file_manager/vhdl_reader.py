#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from vhdl_objects.entity import Entity
from vhdl_objects.wire import Wire
from vhdl_objects.library import Library

class Vhdl_reader:

    def __init__(self, filename):
        self.state = "start"
        self.long_file_name = filename
        self.extract_file_name(self.long_file_name)
        
        self.file = None
        self.entity = None
        self.entity_bloc = ""

        self.open_file()
        self.entity = Entity()
        # self.extract_entity_name()
        self.parse_vhdl_file()
        # self.parse_vhdl_file()
        self.verbose()
        self.close_file()

    def extract_file_name(self, long_file_name):
        self.filename = long_file_name.split("/")[-1]

    def parse_vhdl_file(self):
        self.entity.name = "testing"
        lib_part = ""
        entity_generic_part = ""
        entity_port_part = ""
        entity_part = ""
        for raw_line in self.file:
            real_words = raw_line.split()
            # remove comment
            clean_line = self.clean_line(raw_line) 
            # remove blank line
            clean_words = clean_line.split()

            if len(clean_words) > 0:           
                if self.state == "start":           
                    try:
                        lindex = clean_words.index("entity")

                        if clean_words[lindex+2] == "is":
                            self.entity.set_name(real_words[lindex+1])
                            self.state = "entity"
                    except:
                        lib_part += raw_line
            
                if self.state == "entity":       
                    # print real_words    
                    try:
                        lindex = clean_words.index("end")
   
                        if real_words[lindex+1] == self.entity.name or real_words[lindex+1] == self.entity.name + ";":
                            self.state = "afterentity"
                    except:
                        entity_part += raw_line

                if self.state == "afterentity":       
                    pass
        print lib_part
        print entity_part

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
           
            if self.state == "start":           
                try:
                    lindex = words.index("entity")
                    if words[lindex+2] == "is":
                        self.entity.set_name(real_words[lindex+1])
                        self.state == "entity"
                except:
                    lindex = None

                # try:
                #     lindex = words.index("entity")

        # self.entity.add_input(Wire("Clk",1,"clk"))
        # self.entity.add_input(Wire("Abs",8,"classic"))
        # self.entity.add_output(Wire("EN",1,"classic"))
        # self.entity.add_output(Wire("S",8,"classic"))
        # self.entity.add_inout(Wire("Clk",1,"clk"))
        # self.entity.add_inout(Wire("Abs",7,"classic"))
        # self.entity.add_output(Wire("EN",1,"classic"))
        # self.entity.add_output(Wire("S",8,"classic"))
        # self.entity.add_inout(Wire("Clk",1,"clk"))
        # self.entity.add_inout(Wire("Abs",3,"classic"))
        # self.entity.add_output(Wire("A complex EN",1,"classic"))
        # self.entity.add_inout(Wire("ShadowClk",8,"classic"))

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
