# coding: utf-8
class Vertex:
    """
    Class to represent a vertex.
    """
    def __init__(self, name):
        """
        Constructor for Vertex, initializes class variables.
        :param name: name of the vertex, expected to be int
        """
        self.name = name  # Holds the name passed in
        self.adjacent_vertices = list()  # Hold the vertices that are adjacent to this vertex
        self.degree = 0  # Hold the degree for this vertex

    def add_adjacent(self, adjacent_vertex):
        """
        Adds the given vertex as adjacent to this vertex.
        :param adjacent_vertex: a vertex that is adjacent to this vertex
        """
        self.adjacent_vertices.append(adjacent_vertex)  # Adds adjacent vertex to adjacency list
        self.degree += 1  # Increase degree every time we add an adjacent vertex
        # self.adjacent_vertices = sorted(self.adjacent_vertices, key=lambda vertex: vertex.degree, reverse=True)


    def __eq__(self, other):
        """
        Overrides the built-in equals method to enable equating of two vertices base on it name.
        :param other: the vertex to compare aganist
        :return: the result of equality check between the names(ints) of both vertices
        """
        if isinstance(other, Vertex):
            return self.name == other.name
        return False

    def __str__(self):
        """
        Overrides the built-in str method to enable us to print out a vertex.
        :return: a string containing a human readable version of the vertex
        """

        """
        adjacent_vertices_str = ""
        for adjacent_vertex in self.adjacent_vertices:
            adjacent_vertices_str += str(adjacent_vertex.name) + ", "
        return "{} [{}]".format(self.name, adjacent_vertices_str)
        """
        return "Vertex {}".format(self.name)

