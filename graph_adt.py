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
        """Retrieves the set of all vertices (referenced by key) connected to the current vertex.
        
        :rtype set, a set of keys.
        """
        return self.neighbors 
    
    def get_id(self): #confused about this one, since if v is a Vertex then v.key already returns the key
        #should key be made a private field? Or should get_id return something else...?
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
        """The constructor for the class.
        
        Initializes an empty dictionary of vertices.
        """
        self.clear()

    def add_vertex(self, key):
        """Adds a vertex to the graph. If the given key already exists in the graph, does nothing.
        
        :type any: the key name for the vertex to be added.
        :rtype Vertex: returns the Vertex object which has been added.
        
        """
        if key not in self.vertices:
            self.vertices.add(key, Vertex(key))
            #adds key-value pair to our dictionary of vertices: 
            #key is the key name of the Vertex, value is the Vertex object.
        return self.vertices.get_value(key)
        
    def get_vertex(self, key):
        """Retrieves the Vertex object associated with the given key.
        
        :type any: the key sought
        :rtype Vertex: the Vertex paired with the key.
        """
        return self.vertices.get_value(key)
          
    def add_edge(self, from_key, to_key):
        """Adds an edge to the graph by adding two vertices as neighbors of each other.
        Does nothing if either vertex does not exist in the graph.

        Since the graph is undirected, if A is a neighbor of B, then B is a neighbor of A.
        
        :type any: from_key, one of the endpoints of the edge.
        :type any: to_key, the other endpoint of the edge.
        """
        if to_key in self.vertices and from_key in self.vertices: 
            self.vertices.get_value(from_key).add_neighbor(to_key)
            self.vertices.get_value(to_key).add_neighbor(from_key)

    def get_vertices(self):
        """Retrieves a list of all vertices in the graph.
        
        :rtype list: a list of all the graph's vertices."""
        list_vertices = []
        for key in self.vertices.get_keys():
            list_vertices.append(self.vertices.get_value(key))

        return list_vertices

    def contains(self, key):
        """Checks if the given key is in the graph.
        
        :type any: key, the key to be searched for.
        :rtype boolean: True if the key is in the graph, False otherwise.
        """
        return key in self.vertices.get_keys()

    def clear(self):
        """Clears the graph of all vertices and makes it empty."""
        self.vertices = LinkedDictionary()

    def is_empty(self):
        """Checks if the graph is empty.
        
        :rtype boolean: True if the graph is empty, False otherwise."""
        return len(self.vertices) == 0

    def size(self):
        """Returns the number of vertices in the graph.
        
        :rtype int: the size of the graph.
        """
        return len(self.vertices)

    def get_edges(self):
        """Returns a list of edges in the graph while avoiding duplicates.

        :rtype list: a list of tuples. Each tuple is a pair of vertices; the edge is implicit between them.
        """
        edges = []
        for k in self.vertices.get_keys():
            v = self.vertices.get_value(k)
            for nbr in v.get_connections():
                if (nbr, k) not in edges:
                    edges.append(k, nbr)
        # for v in self.vertices.values(): #for each Vertex object
        #     for nbr in v.get_connections(): #for each of its neighbors
        #         if (nbr, v.key) not in edges:  #prevents duplicates
        #             edges.append((v.key, nbr)) 
        return edges



#      bfs(self, start)
# #    #     This implementation should use a queue.
#      dfs(self, start)

    

