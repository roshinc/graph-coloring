# graph-coloring
### Team 2
Given the list of edges of an undirected graph, find a coloring of this graph

#### Question 18
> Q18: Given the list of edges of an undirected graph, find a coloring of this graph using the algorithm given in the exercise set of Section 10.8.

#### From Section 10.8 p.g.743 : 
> This algorithm can be used to color a simple graph: 

>    First, list the vertices v<sub>1</sub>, v<sub>2</sub>, v<sub>3</sub>,..., v<sub>n</sub> in order of decreasing degree so that deg(v<sub>1</sub>) ≥ deg(v<sub>2</sub>) ≥···≥ deg(v<sub>n</sub>). 

>    Assign color 1 to v<sub>1</sub> and to the next vertex in the list not adjacent to v<sub>1</sub> (if one exists), and successively to each vertex in the list not adjacent to a vertex already assigned color 1. 

>    Then assign color 2 to the first vertex in the list not already colored. Successively assign color 2 to vertices in the list that have not already been colored and are not adjacent to vertices assigned color 2. 

>    If uncolored vertices remain, assign color 3 to the first vertex in the list not yet colored, and use color 3 to successively color those vertices not already colored and not adjacent to vertices assigned color 3. Continue this process until all vertices are colored.

## Runnig 
_**This program requires Phython 3.6.0+**_

If you are in the of the program directory you can just do `python main.py`. It outputs the coloring of four graph that are read form the `./test` directory.

## Input
We represent a simple graph using an adjacency list, i.e a pair of vertices represents an edge.

Below is a simple graph with 4 edges:
```
1,2
1,3
3,5
2,4
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

#### simple_four.graph
##### Test File
![image](https://user-images.githubusercontent.com/2994406/33092726-fa26db46-cec8-11e7-81df-fa4412089105.png)
##### Result
![image](https://user-images.githubusercontent.com/2994406/33092602-a384a25a-cec8-11e7-85fc-a25a69f8ddd2.png)

<hr>
