from Vertex import Vertex
import Edge

seen_list = list()


def get_index(vertex_to_find):
    for found_index in range(0, len(seen_list)):
        if seen_list[found_index] == vertex_to_find:
            return found_index


def get_degree(vertex_to_get_degree_of):
    return vertex_to_get_degree_of.degree


def find_uncolored(partially_colored):
    uncolored = list()
    for vertex_to_check_color in partially_colored:
        if vertex_to_check_color.color == -1:
            uncolored.append(vertex_to_check_color)
    return uncolored


with open("input") as input_file:
    # For every edge in file
    for edges in input_file:

        # Get the first and second vertices of the edge
        (raw_vertice_one, raw_vertice_two) = edges.split(",")

        first_vertex_obj = Vertex(int(raw_vertice_one))
        second_vertex_obj = Vertex(int(raw_vertice_two))

        if first_vertex_obj not in seen_list:
            seen_list.append(first_vertex)
        if second_vertex not in seen_list:
            seen_list.append(second_vertex)




# This algorithm can be used to color a simple graph:

# First, list the vertices v1, v2, v3,..., vn in order of decreasing degree so that deg(v1) ≥ deg(v2) ≥···≥ deg(vn).




"""

# Continue this process until all vertices are colored.

seen_list.sort(key=get_degree, reverse=True)
color = 1

# Assign color 1 to v1 and to the next vertex in the list not adjacent to v1 (if one exists), and successively to
# each vertex in the list not adjacent to a vertex already assigned color 1.
the_first_vertex = seen_list[0]
the_first_vertex.add_color(color)
for i in range(0, len(seen_list)):
    if i != 0:
        if seen_list[i] not in the_first_vertex.adjacent:
            seen_list[i].add_color(color)

# Then assign color 2 to the first vertex in the list not already colored.
# Successively assign color 2 to vertices in the list that have not already been colored and are not adjacent to
# vertices assigned color 2.
color += 1
list_left = find_uncolored(seen_list)

the_first_vertex = list_left[0]
the_first_vertex.add_color(color)
for i in range(0, len(list_left)):
    if i != 0:
        if list_left[i] not in the_first_vertex.adjacent:
            list_left[i].add_color(color)

# If uncolored vertices remain, assign color  3 to the first vertex in the list not yet colored,
# and use color 3 to successively color those vertices not already colored and not adjacent to vertices
# assigned color 3.
color += 1
list_left = find_uncolored(seen_list)
print("-----------")
for vertex in list_left[0].adjacent:
    print(vertex)
#print(list_left[1])
print("-----------")
the_first_vertex = list_left[0]
the_first_vertex.add_color(color)
for i in range(0, len(list_left)):
    if i != 0:
        if list_left[i] not in the_first_vertex.adjacent:
            list_left[i].add_color(color)


"""

""""
for i in range(0, len(seen_list)):
    color += 1
    
    vertex_in_question = seen_list[i]
    vertex_in_question.add_color(color)
    for j in range(0, len(seen_list)):
        if i != j:
            if seen_list[i] not in vertex_in_question.adjacent:
                seen_list[i].add_color(color)

"""
"""
for vertex in seen_list:
    print(vertex)

"""


