'''

>>> what is graphs : Graphs can be used to represent many real-world things such as systems of roads, airline flights from city to city,
 how the Internet is connected, etc
    - Graphs are a more general structure than trees we can think of a tree as a special kind of graph.
>>> Graph types:
    - A Undirected Graph
    - A Directed Graph
    - Directed Acyclic Graphs(DAG) - are directed graphs with no directed cycles.
    - Weighted DAG(directed networks)
    - Weighted DAG with negative edges
>>> Each of graph type has a different representation :
    >> Depth first search (DFS): is an algorithm for traversing or searching tree or graph data structures.
        > Time Complexity: O(E+V)
        > Graph type:
            - Undirected Graph
            - Directed Acyclic Graphs(DAG) without weigth
        > Example using:
            - Weighted Graph
            - Detecting a Cycle in a Graph:
            - Path Finding: go from here or there ?!!
            - Solving Puzzles with Only One Solution:
            - Searching Strongly Connected Components of a Graph
    >> Breadth First Search (BFS) : is an algorithm for traversing or searching tree or graph data structures.
        > Time Complexity: O(E+V)
        > Graph type:
            - Undirected Graph
            - Directed Acyclic Graphs(DAG) without weigth
        > Example using:
            - Shortest Path
            - Copying garbage collection
            - Serialization
    >> Dijkstra’s algorithm: for finding shortest Path between nodes in the Graphs
        > Time Complexity: O(E+V log V)
        > Graph type:
            - non-negative weighted DAG
    >> Bellman–Ford algorithm: computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.
        > Time Complexity: O(VE)
        > Graph type:
            - negative or positive weighted DAG

>>> we can also devide the graph algorithms into 2 categories:
    >> graph traversal/searching algoritms::
        - DFS
        - BFD
    >> find the Shortest Path algorithms :
        - dijakstra - non-negative weighted DAG
        - bellman-ford - negative or positive weighted DAG
        - BFS : it's  traverse a graph, but It can find the shortest path if the edge weights are unit length.

>>> time Complexty analysis:
    - BFS,DFS : we go through each vertex in vertlist or graph (V) and go through each vertex's adjecencies (E) >> the edges that connect from the node to each adjecency
>>>Graphs Termenologies :
    - A vertex :(also called a “node”) is a fundamental part of a graph.
    - payload : A vertex may also have additional information. We will call this additional information the “payload.”
    - Edge (link): An edge connects two vertices to show that there is a relationship between them.
      If the edges in a graph are all one-way, we say that the graph is a directed graph, or a digraph.
    - Weight : Edges may be weighted to show that there is a cost to go from one vertex to another.
    ** Example :
        V={V0,V1,V2,V3,V4,V5}    # the nodes

        #shows how each pair of nodes connectes together and it's cost
        E={(v0,v1,5),(v1,v2,4),       #
            (v2,v3,9),(v3,v4,7),
            (v4,v0,1),(v0,v5,2),
            (v5,v4,8),(v3,v5,3),
            (v5,v2,1)}

        - V (Capital) : Vertices (list of Nodes)   , v(Small): one Vertex
        - E (Capital) : Edges (List of eadges)  , e (small) : one edge
    - Path :The path from V3 to V1 is the sequence of vertices (V3,V4,V0,V1)
    - graph :
    - directed graph :
    - Undirected graph : the graph which each 2 nodes aims to each other or point to each other
    - A cycle in a directed graph : is a path that starts and ends at the same vertex. EX : (V5,V2,V3,V5) 
    - acyclic graph : A graph with no cycles
    - Directed Acyclic Graph (DAG): A directed graph with no cycles

>>> there are 2 impelementations of Graphs : (how to represent graphs)
    >> Adjecency Matrix : One of the easiest ways to implement a graph is to use a two-dimensional matrix. (Not Used)
        > Charactersirtics :
            - The advantage of the adjacency matrix is that it is simple, and for small graphs it is easy to see which nodes are connected to other nodes.
            - that most of the cells in the matrix are empty so it's called “sparse.”
            - A matrix is not a very efficient way to store sparse data.
            - The adjacency matrix is a good implementation for a graph when the number of edges (linkes) is large.
            - the number of edges required to fill the matrix is v^2
            -A matrix is full when every vertex is connected to every other vertex.
        **there is a few real problem in that approach so we are gonna focus on the Adjecency List because we are not gonna have any graphs that really have that many edges
    >> Adjecency List:A more space-efficient way to implement a sparsely connected graph
        > Charactersirtics :
            - In an adjacency list implementation we keep a master list of all the vertices in the Graph object and then
             each vertex object in the graph maintains a list of the other vertices that it is connected to.(adjacency table) or (route tble)
             EX:  {{id="v0", adj={v4:5,v5:2},{id="v1", adj={v1:5,v5:2},.... }
            - In our implementation of the Vertex class we will use a dictionary rather than a list where the dictionary keys are the vertices, and the values are the weights. 
            - The advantage of the adjacency list implementation is that it allows us to compactly represent a sparse graph.
            - The adjacency list also allows us to easily find all the links that are directly connected to a particular vertex. 


>>> when to use dijkstra algo or bellmanford algo:
    >> bellman-ford: used when there is a negative wieghts in the graphs
        - can accomodate the negative weights
        - but it takes a long time to run ,in terms of complexty it's not effecient the order is O(n^2)
    >> Dijkstra : used when there is not  a negative wieghts in the graphs
        - can't accomodate the negative weights
        - but faster than bellan-ford algo

>> the difference between Bellman–Ford algorithm and Dijkstra’s algorithm
    Bellman-Ford similar to Dijstra’s except that instead of utilizing a Priority Queue to visit nodes in order,
    Bellman-Ford looping iterates over every edge V times each, ensuring that all negative edge weights.

>>> why DFS Goes Deep and BFS Goes wide ?
    is it because of the nature of the queues and stacks and hows we insert and pops a nodes/vertises from a stacks or queues
>>>DFS : topological sort :



>>> **** there is a difference between DFS,BFS in Binary Tree and Using BFS,DFS in Graphs ****
  A Tree is typically traversed in two ways:
- Breadth First Traversal (Or Level Order Traversal)
- Depth First Traversals
    Inorder Traversal (Left-Root-Right)
    Preorder Traversal (Root-Left-Right)
    Postorder Traversal (Left-Right-Root)

'''