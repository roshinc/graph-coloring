# greedy-algorithm
### Team 1
We implement Breath-first search, Depth-first search and then our modified DFS with timsort.
## Runnig 
_**This program requires Phython 3.6.0+**_

If you are in the of the program directory you can just do `python main.py`. It outputs the path taken by each algorithm for each of the three graph that are read form the `./test` directory.

## Input
We represent a graph using an adjacency list, i.e a pair of vertices represents an edge and a cost for the path.

Below is a simple graph with 4 edges:
```
a,b,.2
c,d,.4
e,f,.8
g,h,.3
```
The program takes a graph as a file. Few examples can be see in the `./test` directory which it currently reads form.

## Output
For each vertices in the graph we output in the form `Vertex VertexName has Color ColorName`.

Below is the result of running the program of the graph in the [**Input**](https://github.com/roshinc/graph-coloring/blob/master/README.md#input) section:
```
Vertex 1 has Color 1
Vertex 5 has Color 1
Vertex 4 has Color 1
Vertex 2 has Color 2
Vertex 3 has Color 2
```
## Examples

#### simple_one.graph
##### Test File
![image](https://user-images.githubusercontent.com/2994406/33092367-f55556d4-cec7-11e7-9169-1c3a3b2bafdc.png)

_We also allow comments in the test file using back-ticks(\`) as demonstrated above._
##### Result
![image](https://user-images.githubusercontent.com/2994406/33092493-4749b070-cec8-11e7-8e08-baa940761d7c.png)

<hr>

#### simple_two.graph
##### Test File
![image](https://user-images.githubusercontent.com/2994406/33092656-c51e58d4-cec8-11e7-8ce5-e3d72740bfca.png)
##### Result
![image](https://user-images.githubusercontent.com/2994406/33092540-6b7b00ca-cec8-11e7-8666-7f16600da6e9.png)

<hr>

#### simple_three.graph
##### Test File
![image](https://user-images.githubusercontent.com/2994406/33092699-e3430d1e-cec8-11e7-9c34-e2b206470e36.png)
##### Result
![image](https://user-images.githubusercontent.com/2994406/33092568-85b24f66-cec8-11e7-8b23-55089645df44.png)

<hr>
