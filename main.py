from Vertex import Vertex

# Keeps track of all the vertices we have seen
seen_list = list()


def add_two_vertices(first_vertex_to_add, second_vertex_to_add):
    """
    Ensure that the given vertices are in the seen list and are aware of their adjacent relation
    :param first_vertex_to_add: the first vertex given
    :param second_vertex_to_add: the second vertex given
    """
    # If these vertices are not in the seen list add them
    add_if_not_in(first_vertex_to_add)
    add_if_not_in(second_vertex_to_add)
    # Add the vertex as adjacent to each other
    add_adjacent_vertex(first_vertex_to_add, second_vertex_to_add)
    add_adjacent_vertex(second_vertex_to_add, first_vertex_to_add)


def add_if_not_in(vertex_to_add_to_seen_list):
    """
    Add the vertex to seen list if its not there
    :param vertex_to_add_to_seen_list: vertex to add
    """
    if vertex_to_add_to_seen_list not in seen_list:
        seen_list.append(vertex_to_add_to_seen_list)


def get_index(vertex_to_find):
    """
    Gets the index of the given vertex
    :param vertex_to_find: the vertex to look for
    :return: the index of the vertex in the seen list; can assume that this will always find it
    """
    # Look through the seen list
    for i in range(0, len(seen_list)):
        # Find a vertex we were given
        if seen_list[i] == vertex_to_find:
            return i  # Return its index


def add_adjacent_vertex(home_vertex, adjacent_vertex):
    """
    Adds a vertex as adjacent to another vertex
    :param home_vertex: the vertex to add the other vertex to
    :param adjacent_vertex: the adjacent vertex
    """
    seen_list[get_index(home_vertex)].add_adjacent(seen_list[get_index(adjacent_vertex)])


def try_to_color(color_to_set, vertex_to_color):
    """
    Colors the vertex with the given color given that none of its adjacent vertices have the same color
    :param color_to_set: the color
    :param vertex_to_color: the vertex to color
    """
    for adjacent_vertex in vertex_to_color.adjacent_vertices:
        if adjacent_vertex.color == color_to_set:
            return
    vertex_to_color.set_color(color_to_set)


def color():
    """
    Colors a simple graph. Algorithm to color a simple graph from Section 10.8 p.g.743.
    """

    # First, list the vertices v1, v2, v3,..., vn in order of decreasing degree so that deg(v1) ≥ deg(v2) ≥···≥ deg(vn).
    seen_list.sort(key=lambda vertex: vertex.degree, reverse=True)

    # Holds the vertices that are not colored yet, at initialization it would be the list of all vertices
    not_colored = seen_list
    # Color counter, used to assign different colors
    color_counter = 0
    # While we still have vertices left to color
    while not_colored:
        # Increment the color
        color_counter += 1
        # Assign this color to the first vertex in the uncolored list
        first_vertex_being_colored = not_colored[0]
        first_vertex_being_colored.set_color(color_counter)

        # Assign the same color to the next vertex in the list not adjacent to the first vertex
        # Get a list of all vertices not adjacent to the vertex we just colored
        not_adjacent = [x for x in not_colored if x not in not_colored[0].adjacent_vertices]
        # Remove the vertex we already colored
        not_adjacent.remove(first_vertex_being_colored)

        # Color the non adjacent vertices with the same color
        for vertex_in_list in not_adjacent:
            try_to_color(color_counter, vertex_in_list)
        # Get the list of vertices still left to be colored (if any)
        not_colored = [x for x in seen_list if x.color is None]


def handle_graph_file(input_file):
    """
    Given a file that gives edges in the form of pairs, print out the vertices and their colors
    :param input_file: a file with edges representing a simple graph
    """
    global seen_list

    seen_list = list()
    # Open the input file reading
    with open(input_file) as graph_file:
        for edge in graph_file:
            # Ignore comments
            if '`' not in edge:
                (name_first_vertex, name_second_vertex) = edge.strip().split(",")
                first_vertex = Vertex(int(name_first_vertex))
                second_vertex = Vertex(int(name_second_vertex))

                # Add to seen list
                add_two_vertices(first_vertex, second_vertex)
                # print("{},{}".format(first_vertex, second_vertex))
    # Color the graph
    color()
    # Sort it based on colors
    seen_list.sort(key=lambda vertex: vertex.color)
    # Print out the list of vertices
    for vertex_in_list in seen_list:
        print("{}".format(vertex_in_list))


def main():
    print("Printing example output based on input in ./test")
    print()

    print("●▬▬▬▬ simple_one.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_one.graph")

    print("●▬▬▬▬ simple_two.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_two.graph")

    print("●▬▬▬▬ simple_three.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_three.graph")

    print("●▬▬▬▬ simple_four.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_four.graph")


if __name__ == "__main__":
    main()
