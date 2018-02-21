# greedy-algorithm

### Team 1
We implement Breath-first search, Depth-first search and then our modified DFS with timsort.


## Runnig 
_**This program requires Phython 3.6.0+**_

If you are in the of the program directory you can just do `python main.py`. It outputs the path taken by each algorithm for each of the three graph that are read form the `./test` directory.

## Input
We represent a graph using an adjacency list, i.e a pair of vertices represents an edge and a cost for the path.

Below is a simple graph:
```
a,b,.5
b,c,.6
c,f,.7
a,d,.1
d,e,.2
e,f,.4
```
The program takes a graph as a file. Few examples can be see in the `./test` directory which it currently reads form.

Depending on which file you want to use, you call `handle_graph_file("test/simple_one.graph")`. This loads the contents of the file `test/simple_one.graph` as a graph

Then you call the function you want in the main method like `depth_first_search(Vertex("a"), Vertex("f"))`. Here depth_first_search refers to our implementation of the DFS algorithm and prints out a path from "a" to "b" based on the graph we loaded in.

As an example all three algorithms are being called and there outputs printed when you run `main.py`


## Output

Below is the result of running all three algorithms on the graph in the **Input** section:
```
+   breadth_first_search   +
BFS Path: ['a', 'b', 'd', 'c', 'e', 'f']
Cost of BFS: 2.0999999999999996
+   depth_first_search   +
DFS Path ['a', 'b', 'c', 'f']
Cost of DFS: 1.8
+   depth_first_search_with_timsort   +
Greedy DFS Path: ['a', 'd', 'e', 'f']
Cost of Greedy DFS: 0.7000000000000001
```
## Examples

#### simple_one.graph
##### Test File
![image](https://i.imgur.com/vUJYlcp.png)

_We also allow comments in the test file using back-ticks(\`) as demonstrated above._
##### Result
![image](https://i.imgur.com/ZRYnmTw.png)

<hr>
<br>
<br>

#### simple_two.graph
##### Test File
![image](https://i.imgur.com/j1jLzfo.png)
##### Result
![image](https://i.imgur.com/pWvE9lQ.png)

<hr>

#### simple_three.graph
##### Test File
![image](https://i.imgur.com/D7pcQz4.png)
##### Result
![image](https://i.imgur.com/1cf20L2.pngg)

