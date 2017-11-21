class Vertex:
    name = 0
    degree = 0
    adjacent = 
    color = -1

    def __init__(self, name):
        self.name = name

    def add_vertex(self, adjacent_vertex):
        self.degree += 1
        self.adjacent.append(adjacent_vertex)

    def add_color(self, color):
        self.color = color

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        # return str(self.name) + "[Color " + str(self.color) + "]"
        string = ""

        for vertex in self.adjacent:
            string += str(vertex.name) + ", "

        return str(self.name) + "{ " + str(string) + " }"

