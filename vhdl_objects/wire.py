#!/usr/bin/python
# -*- coding: utf-8 -*-

class Wire:

    def __init__(self, name, nb_wires, w_type):
        self.name = name
        self.type = w_type
        self.nb_wires = nb_wires
        self.dir = ""
        pass

    def verbose(self):
        sentence = " Wire: "
        sentence += self.name
        sentence += " - dir: %s" %self.dir
        sentence += " - nb_wires: %d" %self.nb_wires
        sentence += " - type: %s" %self.type
        print sentence
