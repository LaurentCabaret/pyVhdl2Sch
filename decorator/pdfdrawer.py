#!/usr/bin/python
# -*- coding: utf-8 -*-

import cairocffi as cairo

red = (1, 0, 0)
blue = (0, 0, 1)
green = (0, 1, 0)
contour = (0.2, .1, .0)

default_font = 'Jura'
radius = 3
rank_separation = 15
rank_top_margin = 20
line_length = 35
inout_margin = 7

bbox_w_margin = 7
bbox_h_margin = 7

multi_wire_symbol_size = 6
line_width = 1.0

wire_name_margin = 8
class PdfDrawer:

    def __init__(self, filename, entity):
        self.surface = cairo.PDFSurface(filename, 10,10)
        self.context = cairo.Context(self.surface)

        self.height = self.compute_height(entity)
        self.width = self.compute_width(entity)
        self.surface = cairo.PDFSurface(filename, self.width + line_length * 2 + bbox_w_margin * 2, self.height + bbox_h_margin * 2)
        self.context = cairo.Context(self.surface)
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
        pos_x = bbox_w_margin + line_length
        pos_y = bbox_h_margin
        height = self.compute_height(entity)
        width = self.compute_width(entity)
        self.draw_entity_box(pos_x, pos_y, width, height, radius)
        self.draw_entity_name(entity.name, pos_x, pos_y, width)
        for i in range(0, len(entity.inputs)):
            self.draw_wire(entity.inputs[i],i+1, pos_x - radius)

        for i in range(0, len(entity.inouts)):
            self.draw_wire(entity.inouts[i],len(entity.inputs) + i + 1, pos_x - radius)

        for i in range(0, len(entity.outputs)):
            self.draw_wire(entity.outputs[i],i+1, pos_x + width + radius)
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
        self.set_font()        
        with self.context:
            self.context.select_font_face(default_font,1,1)
            (x_bearing, y_bearing, width, height, x_advance, y_advance) = self.context.text_extents(name)
            delta = (x_bearing, y_bearing, width, height, x_advance, y_advance)
            self.context.move_to(x + box_width/2 - width/2, y + height)
            self.context.show_text(name)

    def compute_height(self, entity):
        height = max(len(entity.inputs) + len(entity.inouts),len(entity.outputs))
        if len(entity.inouts) == 0:
            return height*rank_separation + rank_top_margin
        else:
            return height*rank_separation + rank_top_margin  + inout_margin


    def compute_width(self, entity):
        self.set_font()
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

    def draw_wire(self, wire, rank, pos_x):
        self.go_invisible()
        
        self.context.stroke()    
        self.set_source_color(contour) 

        self.set_font()
        self.context.set_line_width(line_width)

        y_pos = rank_top_margin + rank * rank_separation
        if wire.dir == "inout":
            y_pos += inout_margin
        if wire.dir == "in" or wire.dir == "inout":
            
            self.context.move_to(pos_x, y_pos)
            self.context.rel_line_to(-line_length , 0)

            if wire.type == "clk":
                self.draw_clk(pos_x, y_pos)

            if wire.nb_wires != 1:
                self.context.move_to(pos_x - line_length/2 + multi_wire_symbol_size/2, y_pos - multi_wire_symbol_size/2)
                self.context.rel_line_to(-multi_wire_symbol_size , multi_wire_symbol_size)
                label = "%s" % wire.nb_wires
                with self.context:
                    self.context.set_font_size(8)
                    self.context.move_to(pos_x - line_length/2 - multi_wire_symbol_size/2, y_pos -multi_wire_symbol_size/2)
                    self.context.show_text(label)
        
            self.context.move_to(pos_x + wire_name_margin,y_pos + multi_wire_symbol_size/2)

        if wire.dir == "out":
            
            self.context.move_to(pos_x, y_pos)
            self.context.rel_line_to(line_length , 0)
            size = self.context.text_extents(wire.name)[4]

            if wire.nb_wires != 1:
                x_pos = pos_x + line_length/2 + multi_wire_symbol_size/2
                self.context.move_to(x_pos, y_pos - multi_wire_symbol_size/2)
                self.context.rel_line_to(-multi_wire_symbol_size , multi_wire_symbol_size)
                label = "%s" % wire.nb_wires
                with self.context:  
                    self.context.set_font_size(8)
                    wire_size = self.context.text_extents(label)[4]
                    height = self.context.text_extents(label)[3]
                    self.context.move_to(x_pos -multi_wire_symbol_size/2 -wire_size/2, y_pos - height)
                    self.context.show_text(label)            
        
            self.context.move_to(pos_x - wire_name_margin - size, y_pos + multi_wire_symbol_size/2)

        self.context.show_text(wire.name)
        self.context.stroke()

    def set_font(self):
        self.set_source_color(contour)
        self.context.select_font_face(default_font,0,0)
        self.context.set_font_size(12)