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

    #BEA'S TEST METHOD CALLS GO HERE:
    test_user_profile()

    print("All tests passed!")