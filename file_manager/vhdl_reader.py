#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from vhdl_objects.entity import Entity
from vhdl_objects.wire import Wire
from vhdl_objects.library import Library


class Vhdl_reader:

    """
    Vhdl_reader take the .vhd file and return a full entity
    """

    def __init__(self, filename):
        self.state = "start_parsing"
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
        self.parse_vhdl_file()
        self.parse_entity_part()
        self.verbose()
        self.close_file()

    def extract_file_name(self, long_file_name):
        self.filename = long_file_name.split("/")[-1]

    def parse_vhdl_file(self):
        for raw_line in self.file:
            raw_line = self.clean_line(raw_line)
            real_words = raw_line.split()
            # remove comment
            clean_words = raw_line.lower().split()

            # remove blank line
            if len(clean_words) == 0:
                continue

            if self.state == "start_parsing":
                if "entity" in clean_words:
                    if "is" in clean_words:
                        the_index = clean_words.index("entity")
                        self.entity.set_name(real_words[the_index + 1])
                        self.state = "parse_entity"
                        if "port" in clean_words:
                            self.entity_part += "port"
                            if "(" in clean_words:
                                self.entity_part += "(\n"
                            else:
                                self.entity_part += "\n"
                else:
                    self.lib_part += self.remove_comment(raw_line)
            else:
                if self.state == "parse_entity":
                    if "end" in clean_words:
                        the_index = clean_words.index("end")

                        if real_words[the_index + 1] == self.entity.name or\
                                real_words[the_index + 1] == self.entity.name + ";":
                            self.state = "after_entity"
                    else:
                        self.entity_part += self.remove_comment(raw_line)
                else:
                    if self.state == "after_entity":
                        # To continue
                        break

    def parse_entity_part(self):
        state = "start_parsing"
        for raw_line in self.entity_part.split(";"):
            raw_line = self.clean_line(raw_line)
            clean_words = raw_line.lower().split()
            # Generic not used so we neglect it
            if state == "start_parsing":
                if "port" in clean_words:
                    state = "parse_port"
                    raw_line = self.remove_port_from_text(raw_line)

            if state == "parse_port":
                clean_words = self.clean_line(raw_line).split()
                if len(clean_words) == 0:
                    continue
                self.extract_wire(raw_line)

        pass

    def remove_port_from_text(self, text):
        words_lower = text.split()
        index = words_lower.index("(")
        words = words_lower[index + 1:]
        return " ".join(words)

    def extract_wire(self, text):
        if "clk" in text.lower():
            wire_property = "clk"
        else:
            wire_property = "classic"

        real_words = text.split()
        wire_type = real_words[3].lower()
        if wire_type == "integer" or\
                wire_type == "natural" or\
                wire_type == "positive":

            nb_wires = 32

        if wire_type == "std_logic":
            nb_wires = 1

        if wire_type == "std_logic_vector" or\
                wire_type == "unsigned" or\
                wire_type == "signed":

            bus_direction = real_words[6].lower()
            bus_description = real_words[5:8]
            if bus_direction == "downto":
                upper_val = bus_description[0]
                lower_val = bus_description[2]
                try:  # if upper_val and lower_val are integers
                    nb_wires = int(upper_val) - int(lower_val) + 1
                except:
                    nb_wires = self.compute_wire_number(
                        upper_val, lower_val)

            else:
                upper_val = bus_description[2]
                lower_val = bus_description[0]
                try:  # if upper_val and lower_val are integers
                    nb_wires = int(upper_val) - int(lower_val) + 1
                except:
                    nb_wires = self.compute_wire_number(
                        upper_val, lower_val)

        if real_words[2] == "in":
            self.entity.add_input(Wire(real_words[0], nb_wires, wire_property))

        if real_words[2] == "out" or real_words[2] == "buffer":
            self.entity.add_output(
                Wire(real_words[0], nb_wires, wire_property))

        if real_words[2] == "inout":
            self.entity.add_inout(Wire(real_words[0], nb_wires, wire_property))

    def compute_wire_number(self, up, low):
        low = low.replace(" ", "")
        try:
            upper_val = int(up)
            return self.wire_number_upper_is_int(upper_val, low)
        except:
            left_up = up.split("-")[0]
            right_up = up.split("-")[1]
            lower_val = int(low)
            return self.wire_number_upper_is_not_int(left_up, right_up, lower_val)

    def wire_number_upper_is_not_int(self, left_up, right_up, lower_val):
        if -int(right_up) - lower_val + 1 == 0:
            return left_up
        else:
            return left_up + "-" + "%s" % -(-int(right_up) - lower_val + 1)

    def wire_number_upper_is_int(self, upper_val, low):
        try:
            lower_val = int(low)
            return int(upper_val) - int(lower_val) + 1
        except:
            left_low = low.split("-")[0]
            right_low = low.split("-")[1]
            return - int(right_low) + 1 + "-" + upper_val

    def clean_line(self, text):
        clean_line = self.remove_comment(text)
        clean_line = clean_line.replace(':', ' : ')
        clean_line = clean_line.replace('(', ' ( ')
        clean_line = clean_line.replace(')', ' ) ')
        clean_line = clean_line.replace(' -', '-')
        clean_line = clean_line.replace('- ', '-')
        clean_line = clean_line.replace(' ;', ';')
        return clean_line

    def remove_comment(self, text):
        words = text.split()
        clean_line = ""
        for i in range(0, len(words)):
            if words[i] == "--":
                break
            clean_line += words[i] + " "
        return clean_line

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
