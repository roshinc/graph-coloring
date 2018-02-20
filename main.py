from Vertex import Vertex
# Keeps track of all the vertices we have seen
seen_list = list()
head_node = None

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


def handle_graph_file(input_file):
    """
    Given a file that gives edges in the form of pairs, print out the vertices and their colors
    :param input_file: a file with edges representing a simple graph
    """
    global seen_list
    global head_node
    seen_list = list()
    # Open the input file reading
    with open(input_file) as graph_file:
        for edge in graph_file:
            # Ignore comments
            if '`' not in edge:
                (name_first_vertex, name_second_vertex) = edge.strip().split(",")
                first_vertex = Vertex(str(name_first_vertex))
                if head_node is None:
                    head_node = first_vertex
                second_vertex = Vertex(str(name_second_vertex))

                # Add to seen list
                add_two_vertices(first_vertex, second_vertex)
                # print("{},{}".format(first_vertex, second_vertex))

    # Function to print a BFS of graph


def BFS(s, e):
    # Mark all the vertices as not visited
    visited = [False] * (len(seen_list))
    visitedDict = dict()
    # Create a queue for BFS
    queue = []
    # Mark the source node as visited and enqueue it
    queue.append(s)
    # visited[s] = True
    visitedDict[s.name] = True
    while queue:

        # Dequeue a vertex from queue and print it
        s = queue.pop(0)
        print(s)
        if s == e:
            return

        # Get all adjacent vertices of the dequeued
        # vertex s. If a adjacent has not been visited,
        # then mark it visited and enqueue it

        to_visit = None
        if s != head_node:
            to_visit = seen_list[get_index(s)].adjacent_vertices[1:]
        else:
            to_visit = seen_list[get_index(s)].adjacent_vertices

        for i in to_visit:
            if i.name not in visitedDict.keys():
                queue.append(i)
                visitedDict[i.name] = True


def main():
    #print("Printing example output based on input in ./test")
    #print()

    #print("●▬▬▬▬ simple_one.graph ▬▬▬▬▬●")
    #handle_graph_file("test/simple_one.graph")

    print("●▬▬▬▬ simple_two.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_two.graph")
    print(BFS(Vertex("b"), Vertex("h")))

    #print("●▬▬▬▬ simple_three.graph ▬▬▬▬▬●")
    #handle_graph_file("test/simple_three.graph")

    #print("●▬▬▬▬ simple_four.graph ▬▬▬▬▬●")
    #handle_graph_file("test/simple_four.graph")


if __name__ == "__main__":
    main()
