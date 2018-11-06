class Atom:
    def __init__(self, s, v, t):
        self.sign = s
        self.vertex = v
        self.time = t

    def __repr__(self):
        return ("" if self.sign else "~") + self.vertex + str(self.time)
    
class Edges: 
    def __init__(self):
        self.list = []

    def add(self, S, E):
        self.list.append([S, E])

    def isIn(self, S, E):
        return [S, E] in self.list