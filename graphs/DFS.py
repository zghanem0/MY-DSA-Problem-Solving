'''
 ***********************  very Important  **********************************8
>>> the whole idea is u have 2 list :
1- stack List: which u add the node's neihgbors in the , the first node that putted in the stack is the start node >> the node u want to start search from it
2-visted List: the nodes u visted , that is what returned at the end of the Function

>>> i've done 4 solutions : but the 2rd didn't work , the 3rd the working well and the blew is amazing

>>> DFS is better to done recursively : amazing Solution
def dfs(graph, start, visited=None): # the main use of graph is to get the adjecencies of each vertex
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt, visited)
    return visited

dfs(graph, 'A')
'''
# i didn't apply it on the real graph, but try to use key for the key and the value of is neighbors of that key
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(set(x.id for x in self.connectedTo))

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    # ********************** (Solution 1) very nice **********************
    def Deph_First_Search(self, visited):
        visited.append(self.id)
        for nbr in self.connectedTo:
            nbr.Deph_First_Search(visited)
        return visited



arr = []
v = Vertex('y')
print(Vertex.Deph_First_Search(v, arr))


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):  # f : from , t=to
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)  # in the first Node(vertex) "f"  then
        # add Neighbor using the "addNeighbor" method that inside the Vetrex Class

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# ********************** Solution 2 (Didn't work)  ***********************

'''
    def DFS(self, start):
        self.visited = set()
        self.stack = [start]
        while self.stack:
            self.vertex = self.stack.pop()
            if self.vertex not in self.visited:  # if the node not seen
                self.visited.add(self.vertex)  # now the node marked to be seen
                x = self.vertList[self.vertex]
                print(x , self.visited)
                self.stack.extend(self.vertList[set(self.vertex)] - self.visited) # here is the problem
        return self.visited
'''

g = Graph()
g.addEdge('a', 'b',
          5)  # link the first node "a" to "b" with weighted value is "5" , if both "a" and "b" not exist the both nodes will be created and connected
g.addEdge('a', 'd', 15)
g.addEdge('c', 'd', 3)
g.addEdge('b', 'c', 4)
g.addVertex("f")
x = Vertex('a')
#print(g.vertList['a'])
#print(g.DFS('a'))

# ********************** Solution 3 (is more simple and best **********************
'''
print(g.getVertices())
for vertex in g:
    print(vertex)'''
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited=set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


print(dfs(graph, 'A') )
