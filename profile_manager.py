''' Author: Bea Sauve    Date:  12/08/2025   Class: AD325'''
from graph_adt import UndirectedGraph
from linked_adts import LinkedDictionary
from user_profile import UserProfile
import csv
import graphviz

class ProfileManager:
    def __init__(self):
        '''The constructor for the class
        
        Initialises a linked dictionary to manage and an Undirected Graph
        '''
        self.dict_manager = LinkedDictionary()
        self.graph_manager = UndirectedGraph()

    def add_profile(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        ''' Add a user profile to the linked dictionary and graph manager.
        
        :type string: name, location, relationship_status, occupation, atrological_sign, status, Information about the user.
        :type int: age, The users' age
        '''
        user = UserProfile(name, location, relationship_status,age, occupation, astrological_sign, status)
        # Add the profile to dictionary manager
        self.dict_manager.add(name, user)
        # Add the profile to graph manager
        self.graph_manager.add_vertex(name)

    def get_profile(self, name):
        '''Obtain user profile from the profile manager

        :type string: name, Users' name to obtain data from.
        :rtype any: profile(vertex), Users profile stored in the undirected graph manager.
        '''
        return self.dict_manager.get_value(name)
       
    
    def remove_profile(self, name):
        ''' Remove a users profile from all manager locations and friends they are attached to.

        :type string: name, Users' name which will be removed from all structures.
        '''
        #Remove user as a friend from their friends' lists
        friends = self.dict_manager.get_value(name).get_friends()
        for friend in friends:
            self.dict_manager.get_value(friend).remove_friend(name)
        #Remove the user from the Profile Manager
        self.dict_manager.remove(name)
        self.graph_manager.remove_vertex(name)
        #insert command for removing vertices and disconnecting edges
        print(f'User: {name} has been deleted.')
        
    def connect_profiles(self, name1, name2):
        '''Connect profile of one user to another via vertices and edges.
        
        :type string: name1, name2, Names of both users to connect.
        '''
        #Initialize profiles to add eachother as friends
        user1 = self.dict_manager.get_value(name1)
        user2 = self.dict_manager.get_value(name2)
        #Add each user as friends of eachother
        user1.add_friend(name2)
        user2.add_friend(name1)
        #Indicate friendship by adding edges to their vertices
        self.graph_manager.add_edge(name1, name2)

    def display_profiles(self, search_type = bool):
        '''Display all Profiles present in manager.
        
        :rtype list: List of all user profiles displayed in chosen search order.
        '''
        if search_type == True:
            # Display all the profiles in bfs order, starting at first key in dictionary
            return self.graph_manager.bfs(list(self.dict_manager.get_keys())[0])
        elif search_type == False:
            # Display all profiles in dfs order, starting at first key in dictionary
            return self.graph_manager.dfs(list(self.dict_manager.get_keys())[0])
        

    def display_profile_details(self, name):
        ''' Display users profile details.

        :type string: name, Name of user to display information of.
        :rtype string: String of users information
        '''
        #Store user information
        user = self.dict_manager.get_value(name)
        #Print user information
        return user.print_details()
            
    def get_friends_of_friends(self, name, search_type=bool):
        ''' Obtain a list of friends of a users friend

        :type string: name, Name of user to obtain friends of.
        :rtype list: List of friends of users friends'''
        #Traverse based on choice given
        if search_type == True:
            return self.graph_manager.limited_bfs(name, 1)
        elif search_type == False:
            return self.graph_manager.limited_dfs(name, 1)

    

    def read_profiles_from_csv(self, file_path):
        '''Given a file path, read the file, create user profiles, and add them to the profile manager
        
        :type file: file_path, file location to read user data from'''
      
        try:
            with open(file_path, mode = 'r', newline = '') as file:
                csvfile = csv.DictReader(file, delimiter=',')
                #keep track of any errors that may arise
                failed_rows = []
                # Iterate through csv, parsing information, starting with the second line to skip headers
                for index, row in enumerate(csvfile, start = 2):
                    # Based on index incrementation, assign rows to variables
                    try:
                        name = row["name"]
                        status = row['status']
                        #assign as none if no image is present
                        picture = row['picture'] or None
                        location = row["location"]
                        relationship = row['relationship_status']
                        age = int(row['age'])
                        occupation = row['occupation']
                        sign = row['astrological_sign']
                        #create a list of friends, separated by the delimeter
                        friend_cell = row.get("friends", "") or ""
                        friends = [f.strip() for f in friend_cell.split('|') if f.strip()]
                        #Add user to Profile Manager
                        self.add_profile(name,location,relationship,age,occupation, sign, status)
                        # Add a photo to profile if one was present in csv
                        if picture is not None:
                            self.dict_manager.get_value(name).add_photo(picture)
                        #add friend to users friend list and connect their vertices in graph
                        for friend in friends:
                            if self.graph_manager.contains(friend):
                                self.connect_profiles(name, friend)
                    #If there's a failed conversion or the column name isnt present, not the error
                    except(ValueError,KeyError) as e:
                        failed_rows.append((index, row, str(e)))
        # Raise error if file doesn't work
        except FileNotFoundError:
            raise FileNotFoundError(f'File not found: {file_path}')
        # Raise error if problems arise durin build
        except Exception as e:
            raise RuntimeError(f'Failed to build from CSV: {e}')
        if failed_rows:
            print(failed_rows)                              

    def create_user_graph(self, current_user, depth=1):
        '''Display graph of user and their friend connections.
        
        :type vertex: Vertex on graph indicated by current user.
        :rtype graphviz: Visualization of user and who their connected to.
        '''
        dot = graphviz.Graph()
        visited = set()
        start = self.graph_manager.get_vertex(current_user)
        self.__add_nodes(dot, start, visited)
        dot.render(f"{current_user}_graph", format="png", view=True)
        return dot

    def __add_nodes(self, dot, node, visited):
        ''' Helper method to recursively add nodes and edges to Graphviz object
        
        :type dot: dot object Diagraph for graphviz
        :type node:'''
        #keep track of vertices, and loop till all have been visited
        if node is None or node.key in visited:
            return
        visited.add(node.key)
        #obtain a list of all connected keys
        friends_list = node.get_connections()
        #create the vertex into a node
        dot.node(node.key, node.key)
        for friend in friends_list:
            dot.edge(node.key, friend)
            friend_vertex = self.graph_manager.get_vertex(friend)
            self.__add_nodes(dot, friend_vertex, visited)
    
    def contains_profile(self, profile):
        '''Method that returns whether a profile exists within the manager
        
        :type any: profile, a users profile
        :rtype boolean: True if the profile exists, False otherwise'''
        if profile in self.dict_manager.get_keys():
            return True
        else:
            return False
        
            
