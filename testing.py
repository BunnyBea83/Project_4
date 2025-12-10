# LEAH'S TEST CODE GOES ABOVE THE LINE

#TODO: UNCOMMENT ALL TEST METHODS BEFORE PUSHING

from graph_adt import Vertex
from graph_adt import UndirectedGraph




def test_vertex():
    v_a = Vertex("Anne")
    v_b = Vertex("Bea")
    v_c = Vertex("Caroline")
    v_a.add_neighbor("Bea")
    v_a.add_neighbor("Caroline")
    assert v_a.get_id() == "Anne"
    print(v_a.get_connections())
    print(v_b.get_connections())
    v_a.remove_neighbor("Xochitl") #should do nothing
    v_a.remove_neighbor("Caroline")
    print(v_a.get_connections())

def test_undirected_graph():
    test_graph = UndirectedGraph()
    assert test_graph.is_empty()
    assert test_graph.size() == 0
    v_d = test_graph.add_vertex("Diana")
    v_e = test_graph.add_vertex("Evita")
    v_f = test_graph.add_vertex("Fergie")
    assert not test_graph.is_empty()
    assert test_graph.size() == 3
    assert test_graph.contains("Diana")
    assert v_e == test_graph.get_vertex("Evita")
    test_graph.add_edge("Diana", "Fergie")
    test_graph.add_edge("Diana", "Fergie") #duplicate should add nothing
    test_graph.add_edge("Fergie", "Fergie") #self-loop should add nothing
    test_graph.add_edge("Diana", "Evita")
    print(f"List of edges: {test_graph.get_edges()}")

    v_g = test_graph.add_vertex("Georgiana")
    v_h = test_graph.add_vertex("Henrietta")
    v_i = test_graph.add_vertex("Indira")
    test_graph.add_edge("Diana", "Georgiana")
    test_graph.add_edge("Georgiana", "Henrietta")
    test_graph.add_edge("Georgiana", "Evita")
    test_graph.add_edge("Evita", "Indira")
    test_graph.add_vertex("Xochitl") #unconnected vertex
    # test graph now looks like:
    #  F---D---G---H
    #       \ /
    #        E   
    #        |   X
    #        I
    print(f"BFS with Diana:  {test_graph.bfs("Diana")}") 
    print(f"BFS with Henrietta:  {test_graph.bfs("Henrietta")}")
    print(f"BFS with disconnected node Xochitl:  {test_graph.bfs("Xochitl")}")
    print(f"BFS with no specified start node:  {test_graph.bfs()}")
    assert test_graph.bfs("Steve") == [] #start node not in graph

    print(f"Fergie's friends: {test_graph.limited_bfs("Fergie", 1)}")
    print(f"Georgiana's six degrees of separation including herself: {test_graph.limited_bfs("Georgiana", 6, True)}")
    assert test_graph.limited_bfs("Xochitl", 2) == []
    assert test_graph.limited_bfs("Steve", 3) == [] #start node not in graph

    print(f"DFS with Fergie: {test_graph.dfs("Fergie")}") 
    print(f"DFS with Georgiana: {test_graph.dfs("Georgiana")}") 
    print(f"DFS with disconnected node Xochitl: {test_graph.dfs("Xochitl")}") 
    print(f"DFS with no specified start node: {test_graph.dfs()}") 
    assert test_graph.dfs("Steve") == [] #start node not in graph 

    test_graph.remove_vertex("Diana")
    # test graph now looks like:
    #  F       G---H
    #         /
    #        E   
    #        |   X
    #        I
    print(f"List of vertices after Diana removed: {test_graph.get_vertices()}")
    print(f"List of edges after Diana removed: {test_graph.get_edges()}")
    print(f"BFS with Georgiana after Diana removed: {test_graph.bfs("Georgiana")}")

    test_graph.clear()
    assert test_graph.is_empty()
    assert test_graph.dfs() == []
    assert test_graph.bfs("Bob") == []

    

    









# ------------------------------------ #

# BEA'S TEST CODE GOES BELOW THE LINE
#Author: Bea Sauve   Date 12/08/2025   Class: AD325
from user_profile import UserProfile
def test_user_profile():
    user = UserProfile('Bea', 'Lynnwood', 'In a Relationship',26 ,'Pastry Chef', 'Libra', "Online")
    user.print_details()
    user.add_photo('Bea.jpg')
    user.add_friend("Leah")
    user.add_friend('John')
    print(user.get_friends())
    user.remove_friend('John')
    user.set_name('Bean')
    user.set_status(False)
    user.set_relationship('Married')
    user.print_details()



# ------------------------------------ #

# RUNNING TEST CODE 

if __name__ == "__main__":

    #LEAH'S TEST METHOD CALLS GO HERE:
    test_vertex()
    test_undirected_graph()

    #BEA'S TEST METHOD CALLS GO HERE:
    test_user_profile()

    print("All tests passed!")