class Edge:
    name = ""
    vertex_one = None
    vertex_two = None

    def __init__(self, name, vertecies):
        self.name = name
        (self.vertex_one, self.vertex_two) = vertecies
        self.vertex_one.add_vertex(self.vertex_two)
        self.vertex_two.add_vertex(self.vertex_one)
