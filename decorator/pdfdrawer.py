#!/usr/bin/python
# -*- coding: utf-8 -*-

import cairocffi as cairo

red = (1, 0, 0)
blue = (0, 0, 1)
green = (0, 1, 0)
contour = (0.2, .1, .0)

default_font = 'Jura'
radius = 5
class PdfDrawer:

    def __init__(self, filename, entity):
        self.surface = cairo.PDFSurface(filename, 400, 500)
        self.context = cairo.Context(self.surface)
        # self.draw_not(10,10)
        # self.draw_clk(10,20)
        self.draw_entity(entity)

    def draw_background(self, context):
        with context:
            context.set_source_rgba(1, 1, 1, 0)
            context.paint()
        pass

    def set_source_color(self, color):
        self.context.set_source_rgba(color[0], color[1], color[2],1)
        pass

    def go_invisible(self):
        self.context.set_source_rgba(0,0,0,0)

    def draw_not(self, x, y, radius):
        self.go_invisible()
        self.context.stroke()
        self.context.arc(x, y, radius, 0, 2 * 3.14169)
        self.set_source_color(contour)
        self.context.stroke()

    def draw_clk(self, x, y):
        self.context.move_to(x, y-5)
        self.context.rel_line_to(5 , 5)
        self.context.rel_line_to(-5 , 5)
        self.set_source_color(contour)
        self.context.stroke()

    def draw_entity(self, entity):
        pos_x = 100
        pos_y = 10
        height = self.compute_height(entity)
        width = self.compute_width(entity)
        self.draw_entity_box(pos_x, pos_y, width, height, radius)
        self.draw_entity_name(entity.name, pos_x, pos_y, width)
        for i in range(0, len(entity.inputs)):
            self.draw_wire(entity.inputs[i],i+1)

        for i in range(0, len(entity.outputs)):
            self.draw_wire(entity.outputs[i],i+1)
        pass

    def draw_entity_box(self, x, y, width, height, radius):        
        self.go_invisible()
        self.context.stroke()
        self.context.arc(x, y, radius, 3.14169, -0.5 * 3.14169)
        self.context.rel_line_to(width , 0)
        self.context.arc(x+width, y, radius, -0.5 * 3.14169, 0 * 3.14169 )
        self.context.rel_line_to(0 , height)
        self.context.arc(x+width, y+height, radius, 0 * 3.14169, 0.5 * 3.14169 )
        self.context.rel_line_to(-width , 0)
        self.context.arc(x, y+height, radius, 0.5 * 3.14169, 1 * 3.14169 )
        self.context.rel_line_to(0 , -height)
        self.set_source_color(contour)
        self.context.stroke()

    def draw_entity_name(self, name, x, y, box_width):
        self.set_source_color(contour)
        # options = cairo.FontOptions()
        # options.set_antialias(cairo.ANTIALIAS_BEST)
        # assert cairo.FontOptions(antialias=cairo.ANTIALIAS_BEST) == options
        self.context.select_font_face(default_font,0,0)
        self.context.set_font_size(12)
        (x_bearing, y_bearing, width, height, x_advance, y_advance) = self.context.text_extents(name)
        delta = (x_bearing, y_bearing, width, height, x_advance, y_advance)
        self.context.move_to(x + box_width/2 - width/2, y + height)

        self.context.show_text(name)

    def compute_height(self, entity):
        height = max(len(entity.inputs)+len(entity.inouts),len(entity.outputs))
        return height*20+20

    def compute_width(self, entity):
        self.context.select_font_face(default_font,0,0)
        self.context.set_font_size(12)
        maximum_width_left = -1
        maximum_width_right = -1        
        for i in range(0, len(entity.inputs)):
            size = self.context.text_extents(entity.inputs[i].name)[4]
            if maximum_width_left < size:
                maximum_width_left = size

        for i in range(0, len(entity.inouts)):
            size = self.context.text_extents(entity.inouts[i].name)[4]
            if maximum_width_left < size:
                maximum_width_left = size

        for i in range(0, len(entity.outputs)):
            size = self.context.text_extents(entity.outputs[i].name)[4]
            if maximum_width_right < size:
                maximum_width_right = size

        title_size = self.context.text_extents(entity.name)[4]
        global_width = max(maximum_width_left + maximum_width_right + 20, title_size+20)

        return global_width

    def draw_wire(self, wire, rank):
        pos_x = 100
        self.go_invisible()
        
        self.context.stroke()    
        self.set_source_color(contour) 
        self.context.move_to(pos_x- radius, 20+rank * 10)     
        self.context.rel_line_to(-20 , 0)

        if wire.type == "clk":
            self.draw_clk(pos_x- radius,20+rank * 10)
            delta = 9
        else:
            delta = 9

        self.context.select_font_face(default_font,0,0)
        self.context.set_font_size(12)
        self.set_source_color(contour)
        
        self.context.move_to(pos_x- radius + delta, 20+rank * 10+2.5)
        self.context.show_text(wire.name)

        self.context.stroke()

