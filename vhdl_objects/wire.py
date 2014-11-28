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
        self.serialized = ""
        self.serialize()
        print self.serialized
        pass

    def verbose(self):
        sentence = " Wire: "
        sentence += self.name
        sentence += " - dir: %s" % self.dir
        sentence += " - nb_wires: %s" % self.nb_wires
        sentence += " - type: %s" % self.type
        print(sentence)

    def serialize(self):
        self.serialized = "Wire_"
        self.serialized += self.name
        self.serialized += "_"
        self.serialized += self.type
        self.serialized += "_"
        self.serialized += str(self.nb_wires)
        self.serialized += "_"
        self.serialized += str(self.start)
        self.serialized += "_"
        self.serialized += str(self.stop)
        self.serialized += "_"
        self.serialized += self.dir
        self.serialized += "_"
        self.serialized += str(self.written_term)
        self.serialized += "_"
        self.serialized += str(self.to)


