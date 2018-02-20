# coding: utf-8
class Edge:
    """
    Class to represent an edge.
    """
    def __init__(self, to_vertex, cost):
        """
        Constructor for Vertex, initializes class variables.
        :param name: name of the vertex, expected to be int
        """
        self.to_vertex = to_vertex  # Hold the vertex that is adjacent to this vertex
        self.cost = cost  # Hold the cost to travel to this vertex

    def get_vertex(self):
        """
        Gets the vertex that is adjacent to this vertex.
        """
        return self.to_vertex

    def get_cost(self):
        """
        Gets the traveling cost.
        """
        return self.cost

    def __eq__(self, other):
        """
        Overrides the built-in equals method to enable equating of two vertices base on it name.
        :param other: the edge to compare against
        :return: the result of equality check between both vertices
        """
        if isinstance(other, Edge):
            return self.to_vertex == other.to_vertex
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
        return "Edge has Vertex {} with cost {}".format(self.to_vertex.name, self.to_vertex.cost)

