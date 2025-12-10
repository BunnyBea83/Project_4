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
from profile_manager import ProfileManager
import unittest
from unittest.mock import patch
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

#unittest patch to excecute when asked for a reprompt due to invalid name
def test_profile_manager():
    print('\nTesting Profile Manager')
    manager = ProfileManager()
    manager.add_profile('Bea', 'Lynnwood', 'In a Relationship',26 ,'Pastry Chef', 'Libra', "Online")
    manager.add_profile('Cow', 'Farm', 'Single', 5, 'Companion', 'Tarus', 'Offline')
    manager.add_profile('John', "Seattle", 'Single', 89,"Programmer", "Pisces",'Offline')
    manager.add_profile('Kate', "Amsterdam", 'Married', 17,"Explorer", "Virgo",'Offline')
    print(manager.get_profile('Cow'))
    #unittest patch to excecute when asked for a reprompt due to invalid name
    with patch("builtins.input", side_effect = ["Bea"]):
        print(manager.get_profile('Leah'))
    manager.connect_profiles('Bea','Cow')
    manager.connect_profiles('Kate',"Bea")
    with patch("builtins.input", side_effect = ["BFS"]):
        print(manager.display_profiles())
    with patch("builtins.input", side_effect = ["DFS"]):
        print(manager.display_profiles())
    manager.display_profile_details('Kate')
    #display friends of friend
    with patch("builtins.input", side_effect = ["DFS"]):
        #should return only Bea
        print(manager.get_friends_of_friends("Kate"))
        #display friends of friend
    with patch("builtins.input", side_effect = ["BFS"]):
        #should return only Bea
        print(manager.get_friends_of_friends("Kate"))
    #test csv reader
    manager.read_profiles_from_csv("data\\test.csv")
    with patch("builtins.input", side_effect = ["DFS"]):
        #TODO: Currently doesnt display due to limitations on BFS and DFS
        print(manager.display_profiles())
    #remove a user from the profile manager
    manager.remove_profile("Bea")
    #Should display Kate, John, Cow (not in that order)
    with patch("builtins.input", side_effect = ["DFS"]):
        print(manager.display_profiles())


# ------------------------------------ #

# RUNNING TEST CODE 

if __name__ == "__main__":

    #LEAH'S TEST METHOD CALLS GO HERE:
    test_vertex()
    test_undirected_graph()

    #BEA'S TEST METHOD CALLS GO HERE:
    print( "\nBea's Test Code\n----------------------------\n")
    test_user_profile()
    test_profile_manager()

    print("All tests passed!")