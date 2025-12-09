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
    print(test_graph.get_edges())

    v_g = test_graph.add_vertex("Georgiana")
    v_h = test_graph.add_vertex("Henrietta")
    v_i = test_graph.add_vertex("Indira")
    test_graph.add_edge("Diana", "Georgiana")
    test_graph.add_edge("Georgiana", "Henrietta")
    test_graph.add_edge("Georgiana", "Evita")
    test_graph.add_edge("Evita", "Indira")
    # test graph now looks like:
    #  F---D---G---H
    #       \ /
    #        E
    #        |
    #        I
    print(test_graph.bfs("Diana")) #D, then EFG in some order, then HI in some order, no duplicates
    print(test_graph.bfs("Henrietta")) #H, then G, then DE in some order, then FI in some order, no duplicates
    assert test_graph.bfs("Xochitl") == []

    print(test_graph.dfs("Fergie")) #FDEIGH or FDGHEI
    print(test_graph.dfs("Georgiana")) #starts with G, contains "D -> F" and "E -> I", no dupes
    assert test_graph.dfs("Xochitl") == []

    test_graph.remove_vertex("Diana")
    print(test_graph.get_vertices())
    print(test_graph.get_edges())
    print(test_graph.bfs("Georgiana"))
    print(test_graph.dfs("Fergie"))

    test_graph.clear()
    assert test_graph.is_empty()
    

    









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