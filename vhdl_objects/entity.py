#!/usr/bin/python
# -*- coding: utf-8 -*-

class Entity:

    def __init__(self):
        self.name = None
        self.inputs = []
        self.outputs = []
        self.inouts = []        
        pass

    def set_name(self, name):
        self.name = name
        pass

    def add_input(self, wire):
        self.inputs.append(wire)
        pass

    def add_output(self, wire):
        self.outputs.append(wire)
        pass

    def add_inout(self, wire):
        self.inouts.append(wire)
        pass


