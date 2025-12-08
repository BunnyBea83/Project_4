# LEAH'S TEST CODE GOES ABOVE THE LINE

from graph_adt import Vertex
from graph_adt import UndirectedGraph

def test_vertex():
    v_a = Vertex("Anne")
    v_b = Vertex("Bea")
    v_c = Vertex("Caroline")
    v_a.add_neighbor(v_b)
    v_a.add_neighbor(v_c)
    assert v_a.get_id() == "Anne"
    print(v_a.get_connections())
    print(v_b.get_connections())

def test_undirected_graph():
    test_vertex()
    test_graph = UndirectedGraph()
    








# ------------------------------------ #

# BEA'S TEST CODE GOES BELOW THE LINE






# ------------------------------------ #

# RUNNING TEST CODE 

if __name__ == "__main__":

    #LEAH'S TEST METHOD CALLS GO HERE:
    test_vertex()

    #BEA'S TEST METHOD CALLS GO HERE:


    print("All tests passed!")