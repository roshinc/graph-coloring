from Vertex import Vertex
from Edge import Edge
# Keeps track of all the vertices we have seen
seen_list = list()
head_node = None


def add_two_vertices(first_vertex_to_add, second_vertex_to_add, cost_of_travel):
    """
    Ensure that the given vertices are in the seen list and are aware of their adjacent relation
    :param first_vertex_to_add: the first vertex given
    :param second_vertex_to_add: the second vertex given
    """
    # If these vertices are not in the seen list add them
    add_if_not_in(first_vertex_to_add)
    add_if_not_in(second_vertex_to_add)
    # Add the vertex as adjacent to each other
    add_adjacent_vertex(first_vertex_to_add, second_vertex_to_add, cost_of_travel)
    add_adjacent_vertex(second_vertex_to_add, first_vertex_to_add, cost_of_travel)


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
    if not isinstance(vertex_to_find, Vertex):
        raise ValueError('Non Vertex passed to get_index')
    # Look through the seen list
    for i in range(0, len(seen_list)):
        # Find a vertex we were given
        if seen_list[i] == vertex_to_find:
            return i  # Return its index


def add_adjacent_vertex(home_vertex, adjacent_vertex, cost_of_travel):
    """
    Adds a vertex as adjacent to another vertex
    :param home_vertex: the vertex to add the other vertex to
    :param adjacent_vertex: the adjacent vertex
    """
    seen_list[get_index(home_vertex)].add_adjacent(Edge(seen_list[get_index(adjacent_vertex)], cost_of_travel))


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
                (name_first_vertex, name_second_vertex, cost_of_travel) = edge.strip().split(",")
                cost_of_travel = float(cost_of_travel)
                first_vertex = Vertex(str(name_first_vertex))
                if head_node is None:
                    head_node = first_vertex
                second_vertex = Vertex(str(name_second_vertex))

                # Add to seen list
                add_two_vertices(first_vertex, second_vertex, cost_of_travel)
                # print("{},{}".format(first_vertex, second_vertex))


def breadth_first_search(s, e):
    """
    Function to print a BFS of graph from s to e, if it exist
    :param s: Start Vertex
    :param e: End Vertex
    """
    # Mark all the vertices as not visited
    visited_dict = dict()
    # Create a queue for BFS
    queue = list()
    # Create track of the path taken
    path = list()
    # Keep track of the cost
    cost = 0
    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited_dict[s.name] = True

    while queue:

        # pop a vertex from queue and print it
        s = queue.pop(0)

        # if s is an Edge increment the cost
        if isinstance(s, Edge):
            cost += s.get_cost()
            path.append(s.get_vertex().name)
            # turn s back into a Vertex for use below
            s = seen_list[get_index(s.get_vertex())]
        else:
            # If it is not a Edge, it is the start node
            path.append(s.name)
        # check if goal state is reached
        if s == e:
            # print out the path and cost
            print(path)
            print(cost)
            return

        # Get all adjacent vertices of the pop
        # vertex s. If a adjacent has not been visited,
        # then mark it visited and enqueue it

        # if it is not the head remove the first element as it will reference the parent
        if s != head_node:
            to_visit = seen_list[get_index(s)].adjacent_vertices[1:]
        else:
            to_visit = seen_list[get_index(s)].adjacent_vertices

        for i in to_visit:
            if seen_list[get_index(i.get_vertex())].name not in visited_dict.keys():
                queue.append(i)
                visited_dict[seen_list[get_index(i.get_vertex())].name] = True

    # If the search has finished and no path has been found
    print("Path does not exist")


def depth_first_search_recurr(v, cost, path, visited, e):
    """
    Recursive method used by DFS
    :param v: the current node
    :param cost: the running total of the cost
    :param path: the running list of the path
    :param visited: the running list of the visited nodes
    :param e: the goal
    """

    # Mark the current node as visited

    # if v is an Edge increments the cost
    if isinstance(v, Edge):
        visited[seen_list[get_index(v.get_vertex())].name] = True
        cost += v.get_cost()
        path.append(v.get_vertex().name)
        v = seen_list[get_index(v.get_vertex())]
    else:
        visited[v.name] = True
        # print(v.name)
        path.append(v.name)
    if v == e:
        print(path)
        print(cost)
        return


    # to_visit = None
    if v != head_node:
        to_visit = seen_list[get_index(v)].adjacent_vertices[1:]
    else:
        to_visit = seen_list[get_index(v)].adjacent_vertices

    # Recur for all the vertices adjacent to this vertex
    for i in to_visit:
        if seen_list[get_index(i.get_vertex())].name not in visited.keys():
            depth_first_search_recurr(i, cost, path, visited, e)

# The function to do DFS traversal. It uses
# recursive DFSUtil()


def depth_first_search_cost_recurr(v, cost, path, visited, e):

    # Mark the current node as visited and print it

    if isinstance(v, Edge):
        visited[seen_list[get_index(v.get_vertex())].name] = True
        # print(seen_list[get_index(v.get_vertex())].name)
        cost += v.get_cost()
        path.append(v.get_vertex().name)
        v = seen_list[get_index(v.get_vertex())]
    else:
        visited[v.name] = True
        # print(v.name)
        path.append(v.name)
    if v == e:
        print(path)
        print(cost)
        return


    # to_visit = None
    if v != head_node:
        to_visit = seen_list[get_index(v)].adjacent_vertices[1:]
    else:
        to_visit = seen_list[get_index(v)].adjacent_vertices

    to_visit = sorted(to_visit, key=lambda ege: ege.get_vertex().degree)
    # Recur for all the vertices adjacent to this vertex
    for i in to_visit:
        if seen_list[get_index(i.get_vertex())].name not in visited.keys():
            depth_first_search_cost_recurr(i, cost, path, visited, e)

# The function to do DFS traversal. It uses
# recursive DFSUtil()


def depth_first_search_cost(v, e):

    # Mark all the vertices as not visited
    # visited = [False] * (len(self.graph))
    visited_dict_dfs = dict()
    cost = 0
    path = list()

    # Call the recursive helper function to print
    # DFS traversal
    depth_first_search_cost_recurr(v, cost, path, visited_dict_dfs, e)


def depth_first_search(v, e):

    # Mark all the vertices as not visited
    # visited = [False] * (len(self.graph))
    visited_dict_dfs = dict()
    cost = 0
    path = list()

    # Call the recursive helper function to print
    # DFS traversal
    depth_first_search_recurr(v, cost, path, visited_dict_dfs, e)


def main():
    # print("Printing example output based on input in ./test")
    # print()

    # print("●▬▬▬▬ simple_one.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_one.graph")
    breadth_first_search(Vertex("a"), Vertex("f"))
    print("+++++++++++++++++++++++++++++++++++++")
    depth_first_search(Vertex("a"), Vertex("f"))
    print("+++++++++++++++++++++++++++++++++++++")
    depth_first_search_cost(Vertex("a"), Vertex("f"))

    # print("●▬▬▬▬ simple_two.graph ▬▬▬▬▬●")
    # handle_graph_file("test/simple_two.graph")
    # breadth_first_search(Vertex("a"), Vertex("h"))
    # print("+++++++++++++++++++++++++++++++++++++")
    # depth_first_search(Vertex("a"), Vertex("h"))
    # print("+++++++++++++++++++++++++++++++++++++")
    # depth_first_search_cost(Vertex("a"), Vertex("h"))

    # print("●▬▬▬▬ simple_three.graph ▬▬▬▬▬●")
    # handle_graph_file("test/simple_three.graph")

    # print("●▬▬▬▬ simple_four.graph ▬▬▬▬▬●")
    # handle_graph_file("test/simple_four.graph")


if __name__ == "__main__":
    main()
