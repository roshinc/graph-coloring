from Vertex import Vertex

# Keeps track of all the vertices we have seen
seen_list = list()


def add_two_vertices(first_vertex_to_add, second_vertex_to_add):
    add_if_not_in(first_vertex_to_add)
    add_if_not_in(second_vertex_to_add)

    add_adjacent_vertex(first_vertex_to_add, second_vertex_to_add)
    add_adjacent_vertex(second_vertex_to_add, first_vertex_to_add)


def add_if_not_in(vertex_to_add_to_seen_list):
    if vertex_to_add_to_seen_list not in seen_list:
        seen_list.append(vertex_to_add_to_seen_list)


def get_index(vertex_to_find):
    for i in range(0, len(seen_list)):
        if seen_list[i] == vertex_to_find:
            return i


def add_adjacent_vertex(home_vertex, adjacent_vertex):
    seen_list[get_index(home_vertex)].add_adjacent(seen_list[get_index(adjacent_vertex)])


def try_to_color(color_to_set, vertex_to_color):
    for adjacent_vertex in vertex_to_color.adjacent_vertices:
        if adjacent_vertex.color == color_to_set:
            return
    vertex_to_color.set_color(color_to_set)


def color():
    """
    This algorithm can be used to color a simple graph:
    Continue this process until all vertices are colored.
    :return:
    """

    # First, list the vertices v1, v2, v3,..., vn in order of decreasing degree so that deg(v1) ≥ deg(v2) ≥···≥ deg(vn).
    seen_list.sort(key=lambda vertex: vertex.degree, reverse=True)

    # Holds the vertices that are not colored yet, at initialization it would be the whole seen list
    not_colored = seen_list
    # Color counter, used to identify the colors
    color_counter = 0
    # While we still have vertices left to color
    while not_colored:
        # Increment the color
        color_counter += 1
        # Assign this color to the first vertex in the uncolored list
        first_vertex_being_colored = not_colored[0]
        print("First to be colored {}".format(first_vertex_being_colored.name))
        first_vertex_being_colored.set_color(color_counter)

        # Assign the same color to the next vertex in the list not adjacent to the first vertex

        # Get a list of all vertices not adjacent to the vertex we just colored
        not_adjacent = [x for x in not_colored if x not in not_colored[0].adjacent_vertices]
        # Remove the vertex we already colored
        not_adjacent.remove(first_vertex_being_colored)

        print("Not adj to {}".format(first_vertex_being_colored.name))
        for vertex_in_list in not_adjacent:
            print("{}".format(vertex_in_list))

        # Color the non adjacent vertices with the same color
        for vertex_in_list in not_adjacent:
            try_to_color(color_counter, vertex_in_list)
        # Get the list of vertices still left to be colored (if any)
        not_colored = [x for x in seen_list if x.color is None]
        break


    """
    # Assign color 1 to v1 and to the next vertex in the list not adjacent to v1 (if one exists),
    # and successively to each vertex in the list not adjacent to a vertex already assigned color 1.
    color_counter = 1
    vertex_being_colored = seen_list[0]
    vertex_being_colored.add_color(color_counter)
    not_adjacent = [x for x in seen_list if x not in seen_list[0].adjacent_vertices]
    not_adjacent.remove(vertex_being_colored)

    for vertex_in_list in not_adjacent:
        vertex_in_list.add_color(color_counter)

    # Then assign color 2 to the first vertex in the list not already colored.
    # Successively assign color 2 to vertices in the list that have not already been colored
    # and are not adjacent to vertices assigned color 2.
    color_counter += 1

    not_colored = [x for x in seen_list if x.color is None]

    vertex_being_colored = not_colored[0]
    vertex_being_colored.add_color(color_counter)

    not_adjacent = [x for x in not_colored if x not in not_colored[0].adjacent_vertices]
    not_adjacent.remove(vertex_being_colored)

    for vertex_in_list in not_adjacent:
        vertex_in_list.add_color(color_counter)

    # If uncolored vertices remain, assign color 3 to the first vertex in the list not yet colored,
    #  and use color 3 to successively color those vertices not already colored and not adjacent to vertices
    #  assigned color 3.
    color_counter += 1

    not_colored = [x for x in seen_list if x.color is None]

    vertex_being_colored = not_colored[0]
    vertex_being_colored.add_color(color_counter)

    not_adjacent = [x for x in not_colored if x not in not_colored[0].adjacent_vertices]
    not_adjacent.remove(vertex_being_colored)

    for vertex_in_list in not_adjacent:
        vertex_in_list.add_color(color_counter)
    """


def main():
    # Open the input file reading
    with open("test/simple_two.graph") as graph_file:
        for edge in graph_file:
            # Ignore comments
            if '`' not in edge:
                (name_first_vertex, name_second_vertex) = edge.strip().split(",")
                first_vertex = Vertex(int(name_first_vertex))
                second_vertex = Vertex(int(name_second_vertex))

                # Add to seen list if not in there
                add_two_vertices(first_vertex, second_vertex)
                # print("{},{}".format(first_vertex, second_vertex))
    color()
    # seen_list.sort(key=lambda vertex: vertex.color)
    print("=======Colored==========")
    for vertex_in_list in seen_list:
        print("{}".format(vertex_in_list))


if __name__ == "__main__":
    main()
