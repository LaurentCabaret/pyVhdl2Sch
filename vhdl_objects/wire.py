class Wire:

    def __init__(self, name, nb_wires, w_type, direction, written_term, start, stop, up):
        self.name = name
        self.type = w_type
        self.nb_wires = nb_wires
        self.start = start
        self.stop = stop
        self.dir = direction.upper()
        self.written_term = written_term
        self.to = up
        pass

    def verbose(self):
        sentence = " Wire: "
        sentence += self.name
        sentence += " - dir: %s" % self.dir
        sentence += " - nb_wires: %s" % self.nb_wires
        sentence += " - type: %s" % self.type
        print(sentence)
