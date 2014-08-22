#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from vhdl_objects.entity import Entity
from vhdl_objects.wire import Wire
from vhdl_objects.library import Library

class Vhdl_reader:

    def __init__(self, filename):
        self.state = "start"
        self.lib_part = ""
        self.entity_generic_part = ""
        self.entity_port_part = ""
        self.entity_part = ""

        self.long_file_name = filename
        self.extract_file_name(self.long_file_name)
        
        self.file = None
        self.entity = None
        self.entity_bloc = ""

        self.open_file()
        self.entity = Entity()
        # self.extract_entity_name()
        self.parse_vhdl_file()
        self.parse_entity_part()
        # self.parse_vhdl_file()
        self.verbose()
        self.close_file()

    def extract_file_name(self, long_file_name):
        self.filename = long_file_name.split("/")[-1]

    def parse_vhdl_file(self):
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
                        self.lib_part += self.remove_comment(raw_line)
                else:
                    if self.state == "entity":       
                        # print real_words    
                        try:
                            lindex = clean_words.index("end")
   
                            if real_words[lindex+1] == self.entity.name or real_words[lindex+1] == self.entity.name + ";":
                                self.state = "afterentity"
                        except:
                            self.entity_part += self.remove_comment(raw_line)
                    else:
                        if self.state == "afterentity":       
                            pass
        pass

    def parse_entity_part(self):
        state = "start"
        for raw_line in self.entity_part.split(";"):
            clean_line = self.clean_line(raw_line)
            clean_words = clean_line.split()
            # Generic not used so we neglect it 
            if state == "start":
                try:
                    lindex = clean_words.index("port")
                    state = "port"
                    raw_line = raw_line.split("(")[1]
                except:
                    nothing = None
    
            if state == "port":
                try:
                    lindex = clean_words.index(")")
                    if lindex > 0 :
                        raw_line = raw_line.split(")")[0]
                        state = "end"
                    self.extract_wire(raw_line)
                except:
                    self.extract_wire(raw_line)
        pass


    def extract_wire(self, text):
        real_words = text.split()
        if real_words[3].lower() == "integer":
            nb_wires = 32
        else:
            if real_words[3].lower() == "std_logic":
                nb_wires = 1
            else:
                if real_words[3].lower() == "std_logic_vector":
                    if real_words[5].lower() == "downto":
                        try:
                            size_sentence = real_words[4].split("(")[1]
                            try:
                                words = size_sentence.split("-")
                            except:
                                nb_wires = size_sentence
                            print size_sentence
                            nb_wires = words[0]
                            # if int(words[1]) 
                        except:
                            nb_wires = 3
                    # try: 
                    #     nb_wires = int(real_words[4])

                    # except:
                    #     nb_wires = real_words[4]
                        
                    #     try: 
                    #         words = nb_wires.split("-")
                    #         print words
                    #         print real_words
                            
                    #         the_minus_size = words[1]   
                    #         the_other_size = real_words[6].split(")")[0]
                    #         # print words
                    #         if int(the_minus_size) == int(the_other_size) + 1:
                    #             nb_wires = the_size
                    #         print int(the_size)
                    #         print int(the_other_size)
                    #     except: 
                    #         nothing = None
                    else:
                        try:
                            size_sentence = real_words[6].split(")")[0]
                            try:
                                words = size_sentence.split("-")
                                nb_wires = words[1]
                            except:
                                nb_wires = size_sentence
                            print size_sentence
                            
                            # if int(words[1]) 
                        except:
                            nb_wires = 3


        if real_words[2] == "in":
            self.entity.add_input(Wire(real_words[0], nb_wires, "classic"))
        if real_words[2] == "out" or real_words[2] == "buffer":
            self.entity.add_output(Wire(real_words[0], nb_wires, "classic"))
        if real_words[2] == "inout":
            self.entity.add_inout(Wire(real_words[0], nb_wires, "classic"))

    def clean_line(self, text):
        clean_line = self.remove_comment(text)
        return clean_line.lower()

    def remove_comment(self, text):
        words = text.split()
        clean_line = ""
        for i in range(0,len(words)):
            if words[i] == "--":
                break
            clean_line += words[i] + " "
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
