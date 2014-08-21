#!/usr/bin/python
# -*- coding: utf-8 -*-

class Entity:

    def __init__(self):
        self.name = None
        self.inputs = []
        self.outputs = []
        self.inouts = []
        self.is_generic = False
        pass

    def set_name(self, name):
        self.name = name
        pass

    def add_input(self, wire):
        wire.dir = "in"
        self.inputs.append(wire)
        pass

    def add_output(self, wire):
        wire.dir = "out"
        self.outputs.append(wire)
        pass

    def add_inout(self, wire):
        wire.dir = "inout"
        self.inouts.append(wire)
        pass


