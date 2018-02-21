# coding: utf-8
from Vertex import Vertex
from Edge import Edge

# Keeps track of all the vertices we have seen
seen_list = list()
# Keep track of the head
head_node = None


def add_two_vertices(first_vertex_to_add, second_vertex_to_add, cost_of_travel):
    """
    Ensure that the given vertices are in the seen list and are aware of their adjacent relation
    :param first_vertex_to_add: the first vertex given
    :param second_vertex_to_add: the second vertex given
    :param cost_of_travel: the cost of the edge
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
    # Since this method would only work if you passed in a vertex, ensure it.
    if not isinstance(vertex_to_find, Vertex):
        raise ValueError('Non-Vertex passed to get_index')
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
    :param cost_of_travel: the cost of the edge
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


def breadth_first_search(source_bfs, goal_bfs):
    """
    Function to find a path using BFS from s to e, if it exist
    :param s: Start Vertex
    :param e: End Vertex
    """
    # Dict to keep track of the visited nodes
    visited_dict = dict()
    # List of nodes to visit next
    queue_bfs = list()
    # List to keep track of the path taken
    path_bfs = list()
    # Keep track of the cost
    cost_bfs = 0
    # Mark the source node as visited and enqueue it
    queue_bfs.append(source_bfs)
    visited_dict[source_bfs.name] = True

    while queue_bfs:

        # pop a vertex from queue_bfs
        source_bfs = queue_bfs.pop(0)

        # if source_bfs is an Edge increment the cost
        if isinstance(source_bfs, Edge):
            cost_bfs += source_bfs.get_cost()
            path_bfs.append(source_bfs.get_vertex().name)
            # turn source_bfs back into a Vertex for use below
            source_bfs = seen_list[get_index(source_bfs.get_vertex())]
        else:
            # If it is not a Edge, it is the sourse node
            path_bfs.append(source_bfs.name)
        # check if goal state is reached
        if source_bfs == goal_bfs:
            # print out the path and cost
            print("BFS Path: {}".format(path_bfs))
            print("Cost of BFS: " + str(cost_bfs))
            return

        # Get all adjacent vertices of the vertex source_bfs. 

        # if source_bfs is not the head remove the first element as it references the parent
        if source_bfs != head_node:
            to_visit = seen_list[get_index(source_bfs)].adjacent_vertices[1:]
        else:
            to_visit = seen_list[get_index(source_bfs)].adjacent_vertices

        # If a adjacent has not been visited, then mark it visited and enqueue it
        for i in to_visit:
            if seen_list[get_index(i.get_vertex())].name not in visited_dict.keys():
                queue_bfs.append(i)
                visited_dict[seen_list[get_index(i.get_vertex())].name] = True

    # If the search has finished and no path has been found
    print("Path does not exist")


def depth_first_search_recurr(source_dfs, cost_dfs, path_dfs, visited_dfs, goal_dfs):
    """
    Recursive method used by DFS
    :param source_dfs: the current node
    :param cost_dfs: the running total of the cost
    :param path_dfs: the running list of the path
    :param visited_dfs: the running list of the visited nodes
    :param goal_dfs: the goal
    """

    # Mark the current node as visited

    # if source_dfs is an Edge increments the cost
    if isinstance(source_dfs, Edge):
        visited_dfs[seen_list[get_index(source_dfs.get_vertex())].name] = True
        cost_dfs += source_dfs.get_cost()
        path_dfs.append(source_dfs.get_vertex().name)
        # turn source_dfs back into a Vertex for use below
        source_dfs = seen_list[get_index(source_dfs.get_vertex())]
    else:
        # If it is not a Edge, it is the start node
        visited_dfs[source_dfs.name] = True
        path_dfs.append(source_dfs.name)

    # check if goal state is reached
    if source_dfs == goal_dfs:
        print("DFS Path {}".format(path_dfs))
        print("Cost of DFS: " + str(cost_dfs))
        return

    # Get all adjacent vertices of the poped vertex s.
    # if it is not the head remove the first element as it will reference the parent

    if source_dfs != head_node:
        to_visit = seen_list[get_index(source_dfs)].adjacent_vertices[1:]
    else:
        to_visit = seen_list[get_index(source_dfs)].adjacent_vertices

    # If a adjacent has not been visited, then mark it visited and enqueue it

    # Recur for all the vertices adjacent to this vertex
    for i in to_visit:
        if seen_list[get_index(i.get_vertex())].name not in visited_dfs.keys():
            # recursive call with adjacent vertex
            depth_first_search_recurr(i, cost_dfs, path_dfs, visited_dfs, goal_dfs)


def depth_first_search(v, e):
    """
    Function to print a BFS of graph from v to e, if it exist
    :param v: Start Vertex
    :param e: End Vertex
    """
    # dictionary to keep track of visited node
    visited_dict_dfs = dict()

    # Keep track of the cost
    cost = 0
    # List to keep track of the path taken
    path = list()

    # Call the recursive helper function to print
    # DFS traversal
    depth_first_search_recurr(v, cost, path, visited_dict_dfs, e)


def depth_first_search_with_timsort_recurr(source_greedy_dfs, cost_greedy_dfs, path_greedy_dfs, visited_greedy_dfs, e):
    """
    Recursive method used by greedy DFS
    :param source_greedy_dfs: the current node
    :param cost_greedy_dfs: the running total of the cost
    :param path: the running list of the path
    :param visited: the running list of the visited nodes
    :param e: the goal
    """

    # Mark the current node as visited and print it

    if isinstance(source_greedy_dfs, Edge):
        visited_greedy_dfs[seen_list[get_index(source_greedy_dfs.get_vertex())].name] = True

        cost_greedy_dfs += source_greedy_dfs.get_cost()
        path_greedy_dfs.append(source_greedy_dfs.get_vertex().name)
        source_greedy_dfs = seen_list[get_index(source_greedy_dfs.get_vertex())]
    else:
        visited_greedy_dfs[source_greedy_dfs.name] = True
        path_greedy_dfs.append(source_greedy_dfs.name)

    if source_greedy_dfs == e:
        print("Greedy DFS Path: {}".format(path_greedy_dfs))
        print("Cost of Greedy DFS: {}".format(cost_greedy_dfs))
        return

    # Get all adjacent vertices of the poped vertex. 

    # if it is not the head remove the first element as it will reference the parent
    if source_greedy_dfs != head_node:
        to_visit = seen_list[get_index(source_greedy_dfs)].adjacent_vertices[1:]
    else:
        to_visit = seen_list[get_index(source_greedy_dfs)].adjacent_vertices

    # Python uses timsort to complete the sorted call
    to_visit = sorted(to_visit, key=lambda ege: ege.cost)

    # Recur for all non visited  vertices adjacent to this vertex
    for i in to_visit:
        if seen_list[get_index(i.get_vertex())].name not in visited_greedy_dfs.keys():
            depth_first_search_with_timsort_recurr(i, cost_greedy_dfs, path_greedy_dfs, visited_greedy_dfs, e)

#


def depth_first_search_with_timsort(v, e):
    """
    Function to find a path using greedy DFS from s to e, if it exist
    :param v: Start Vertex
    :param e: End Vertex
    """

    # dictionary to keep track of visited node
    visited_dict_dfs = dict()
    cost = 0
    path = list()

    # Call the recursive helper function to do
    # DFS traversal
    depth_first_search_with_timsort_recurr(v, cost, path, visited_dict_dfs, e)


def main():
    print("Printing example output based on input in ./test")
    print()

    print("●▬▬▬▬ simple_one.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_one.graph")
    print("+   breadth_first_search   +")
    breadth_first_search(Vertex("a"), Vertex("f"))
    print("+   depth_first_search   +")
    depth_first_search(Vertex("a"), Vertex("f"))
    print("+   depth_first_search_with_timsort   +")
    depth_first_search_with_timsort(Vertex("a"), Vertex("f"))

    print("●▬▬▬▬ simple_two.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_two.graph")
    print("++++++breadth_first_search++++++")
    breadth_first_search(Vertex("a"), Vertex("h"))
    print("+++++depth_first_search++++++")
    depth_first_search(Vertex("a"), Vertex("h"))
    print("+   depth_first_search_with_timsort   +")
    depth_first_search_with_timsort(Vertex("a"), Vertex("h"))

    print("●▬▬▬▬ simple_three.graph ▬▬▬▬▬●")
    handle_graph_file("test/simple_three.graph")
    print("++++++breadth_first_search++++++")
    breadth_first_search(Vertex("a"), Vertex("f"))
    print("+++++depth_first_search+++++")
    depth_first_search(Vertex("a"), Vertex("f"))
    print("+   depth_first_search_with_timsort   +")
    depth_first_search_with_timsort(Vertex("a"), Vertex("f"))


if __name__ == "__main__":
    main()
