'''

>> searching types :
    - linear search
    - binary search
    - Depth First Search (DFS)
    - Breadth First Search (BFS)

>>> there are 2 ways of traversing :
	- using graph traversal : DFS and BFS
	- using tree traversal : preorder,inorder,postorder

>>> when use DFS and BFS:
That heavily depends on the structure of the search tree and the number and location of solutions (aka searched-for items).

If you know a solution is not far from the root of the tree, a breadth first search (BFS) might be better.
If the tree is very deep and solutions are rare, depth first search (DFS) might take an extremely long time, but BFS could be faster.

If the tree is very wide, a BFS might need too much memory, so it might be completely impractical.

If solutions are frequent but located deep in the tree, BFS could be impractical.

If the search tree is very deep you will need to restrict the search depth for depth first search (DFS), anyway (for example with iterative deepening).

use BFS - when you want to find the shortest path from a certain source node to a certain destination. (Or more generally, the smallest number of steps to reach the end state from a given initial state.)

use DFS - when you want to exhaust all possibilities, and check which one is the best or count the number of all possible ways.

use DFS : For maze Solving priblems
-----------------------------------------------------------------------------------------------
Here we will see what are the different applications of DFS and BFS algorithms of a graph?

The DFS or Depth First Search is used in different places. Some common uses are −

If we perform DFS on unweighted graph, then it will create minimum spanning tree for all pair shortest path tree
We can detect cycles in a graph using DFS. If we get one back-edge during BFS, then there must be one cycle.
Using DFS we can find path between two given vertices u and v.
We can perform topological sorting is used to scheduling jobs from given dependencies among jobs. Topological sorting can be done using DFS algorithm.
Using DFS, we can find strongly connected components of a graph. If there is a path from each vertex to every other vertex, that is strongly connected.
Like DFS, the BFS (Breadth First Search) is also used in different situations. These are like below −

In peer-to-peer network like bit-torrent, BFS is used to find all neighbor nodes
Search engine crawlers are used BFS to build index. Starting from source page, it finds all links in it to get new pages
Using GPS navigation system BFS is used to find neighboring places.
In networking, when we want to broadcast some packets, we use the BFS algorithm.
Path finding algorithm is based on BFS or DFS.
BFS is used in Ford-Fulkerson algorithm to find maximum flow in a network.

**** DFS : For maze ,Finding connected components. such as chess, spanning tree protocol
*** BFS : to get the shortest path , dijekstra algorithm,torrent,GPS



'''