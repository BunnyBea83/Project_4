# graph_adt was written by Leah

from linked_adts import LinkedQueue
from linked_adts import LinkedDictionary

class Vertex:
    """Represents one vertex in an undirected graph."""
    
    def __init__(self, key):
        """The constructor for the class. 
        
        Initializes a set for tracking the vertex's neighbors (by key).

        :type any: key, the key name for the vertex.
        """
        self.key = key
        self.neighbors = set() 

    def add_neighbor(self, nbr):
        """Adds a neighbor to the vertex's set of neighbors. 
        
        Implicitly, if two vertices are neighbors, there is an edge between them.
        
        :type any: nbr, a key referencing the neighbor vertex.
        """
        self.neighbors.add(nbr) 

    def get_connections(self):
        """Returns a list of all vertices (referenced by key) connected to the current vertex.
        
        :rtype list, a list of keys.
        """
        return list(self.neighbors)
    
    def get_id(self): 
        """Retrieves the vertex's key.
        
        :rtype any: the vertex's key.
        """
        return self.key
    
    # weights not implemented currently
    def get_weight(self, nbr):
        return 0
    

    
class UndirectedGraph:
    """Represents one undirected graph, composed of vertices and undirected edges."""
    
    def __init__(self):
        """The constructor for the class. Initializes an empty dictionary of vertices."""
        self.clear()

    def add_vertex(self, key):
        """Adds a vertex to the graph. If the given key already exists in the graph, does nothing.
        
        :type any: the key name for the vertex to be added.
        :rtype Vertex: returns the Vertex object which has been added.
        
        """
        if self.vertices.get_value(key) is None:
            self.vertices.add(key, Vertex(key))
            #adds key-value pair to our dictionary of vertices: 
            #key is the key name of the Vertex, value is the Vertex object.
        return self.vertices.get_value(key) #might decide to return keys instead?
    


        
    def get_vertex(self, key):
        """Retrieves the Vertex object associated with the given key.
        
        :type any: the key sought
        :rtype Vertex: the Vertex paired with the key.
        """
        return self.vertices.get_value(key)
          
    def add_edge(self, from_key, to_key):
        """Adds an edge to the graph by adding two different vertices as neighbors of each other.
        Does nothing if either vertex does not exist in the graph or if the edge would be a self-loop.

        Since the graph is undirected, if A is a neighbor of B, then B is a neighbor of A.
        
        :type any: from_key, one of the endpoints of the edge.
        :type any: to_key, the other endpoint of the edge.
        """
        if self.contains(from_key) and self.contains(to_key) and to_key != from_key:
            self.vertices.get_value(from_key).add_neighbor(to_key)
            self.vertices.get_value(to_key).add_neighbor(from_key)


    def get_vertices(self):
        """Retrieves a list of all vertices in the graph.
        
        :rtype list: a list of all the graph's vertices.
        """
        list_vertices = []
        for key in self.vertices.get_keys():
            list_vertices.append(self.vertices.get_value(key))

        return list_vertices

    def contains(self, key):
        """Checks if the given key is in the graph.
        
        :type any: key, the key to be searched for.
        :rtype boolean: True if the key is in the graph, False otherwise.
        """
        return self.vertices.get_value(key) is not None 

    def clear(self):
        """Clears the graph of all vertices and makes it empty."""
        self.vertices = LinkedDictionary()

    def is_empty(self):
        """Checks if the graph is empty.
        
        :rtype boolean: True if the graph is empty, False otherwise."""
        return self.vertices.get_size() == 0

    def size(self):
        """Returns the number of vertices in the graph.
        
        :rtype int: the size of the graph.
        """
        return self.vertices.get_size()

    def get_edges(self):
        """Returns a list of edges in the graph while avoiding duplicates.

        :rtype list: a list of tuples. Each tuple is a pair of vertices; the edge is implicit between them.
        """
        edges = []

        for k in self.vertices.get_keys():
            v = self.vertices.get_value(k)
            for nbr in v.get_connections():
                if (nbr, k) not in edges:
                    edges.append((k, nbr))
        return edges



    def bfs(self, start): 
        """Traverses the graph in a breadth-first search.

        Runs in linear time (O(n + m) for n vertices and m edges.)
        
        :type any: start, the key for the starting vertex.
        :rtype list: A list of keys in the breadth-first order visited.
        """
        if not self.contains(start): #key not in graph
            return []
        
        discovered_set = set() 
        vertex_queue = LinkedQueue()
        traversal_order = []

        vertex_queue.enqueue(start) #queue of keys

        while not vertex_queue.is_empty():
            current = vertex_queue.dequeue() 
            discovered_set.add(current)
            traversal_order.append(current)
            for nbr in self.get_vertex(current).get_connections(): #nbrs are keys
                if nbr not in discovered_set: #discover and enqueue any undiscovered neighbors
                    discovered_set.add(nbr)
                    vertex_queue.enqueue(nbr) 

        return traversal_order


    def dfs(self, start):
        """Traverses the graph in a depth-first search.
        
        Runs in linear time (O(n + m) for n vertices and m edges.)
        
        :type any: start, the key for the starting vertex.
        :rtype list: A list of keys in the depth-first order visited.
        """
        if not self.contains(start): #key not in graph
            return []
        
        vertex_stack = [start] #stack of keys
        visited_set = set()
        traversal_order = []

        while len(vertex_stack) != 0:
            current = vertex_stack.pop()
            visited_set.add(current)
            traversal_order.append(current)
            for nbr in self.get_vertex(current).get_connections(): #nbrs are keys
                if nbr not in visited_set:
                    visited_set.add(nbr)
                    vertex_stack.append(nbr) #push to the top of the stack

        return traversal_order

    

