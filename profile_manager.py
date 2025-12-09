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
        :rtype any: profile(vertex), Users profile stored in the undirected graph manager, None if not valid name.
        '''
        #Verify user name, return their data if found.
        val_user = self.verify_user(name)
        return self.dict_manager.get_value(val_user)
       
    
    def remove_profile(self, name):
        '''TODO: Figure this out'''
        ''' Remove a users profile from all manager locations.

        :type string: name, Users' name which will be removed from all structures.
        '''
        #Verify Users' name, then remove data from all structures
        val_user = self.verify_user(name)
        self.dict_manager.remove(val_user)
        #insert command for removing vertices and disconnecting edges
        print(f'User: {name} has been deleted.')
        
    def connect_profiles(self, name1, name2, weight=0):
        '''Connect profile of one user to another via vertices and edges.
        
        :type string: name1, name2, Names of both users to connect.
        '''
        self.graph_manager.add_edge(name1, name2, weight = 0)

    def display_profiles(self):
        '''TODO: figure out where to start display from and if search methods return a list.'''
        '''Display all Profiles present in manager.
        
        :rtype list: List of all user profiles displayed in chosen search order.
        '''
        #Prompt and validate user input
        choice = self.search_prompt()
        if choice == 'bfs' or choice == 'breadth-first-search':
            # Display all the profiles in bfs order
            return self.graph_manager.bfs()
        else:
            # Display all profiles in dfs order
            return self.graph_manager.dfs()
        

    def display_profile_details(self, name):
        ''' If user exists in directory, display their profile details.

        :type string: name, Name of user to display information of.
        :rtype string: String of users information
        '''
        #Ensure the name is of a valid user
        val_user = self.verify_user(name)
        #Store user information
        user = self.dict_manager.get_value(val_user)
        #Print user information
        return user.print_details()
            
    def get_friends_of_friends(self, name):
        ''' Obtain a list of friends of a users friends

        :type string: name, Name of user to obtain friends of.
        :rtype list: List of friends of users friends'''
        #Validate name given
        val_name = self.verify_user(name)
        #Prompt user for search type
        choice = self.search_prompt()
        #Access user profile
        user = self.manager.get_vertex(val_name)
        #get users friends
        friends = user.get_friends()
        #loop get friends of friend, use search based on users request
        for friend in friends:
            if choice == 'bfs' or choice == 'breadth-first-search':
                return self.manager.bfs(friend)
            else:
                return self.manager.dfs(friend)

    

    def read_profiles_from_csv(self, file_path):
        #TODO: figure out adding user and friends
        try:
            with open(file_path, mode = 'r', newline = '') as file:
                csvfile = csv.DictReader(file, delimiter='|')
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
                        friends = row['friends'].split('|') 

                        new_user = UserProfile(name,location,relationship,age,occupation, sign, status)
                        # Add a photo to profile if one was present in csv
                        if picture is not None:
                            new_user.add_photo(picture)
                        #add friend to users friend list and connect their vertices in graph
                        for friend in friends:
                            new_user.add_friend(friend)
                            self.manager.add_edge(new_user.get_name,friend)
                        #add user to graph
                        self.manager.add_vertex(new_user)
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
        dot = graphviz.graph()
        self.__add_nodes(dot,self.graph_manager.get_vertex(current_user))
        return dot

    def __add_nodes(self, dot, node):
        ''' Helper method to recursively add nodes and edges to Graphviz object
        
        :type dot: dot object Diagraph for graphviz
        :type node:'''
        if node:
            dot.node(str(node), f"{node}")
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)
    
    def search_prompt(self):
        '''Helper method: Verify users search choice.
        
        :rtype string: choice, users validated search type choice.
        '''
        #Predetermined choice types
        valid_choice = {'bfs', 'breadth-first-search', 'dfs', 'depth-first-search'}
        #Keep looping till a valid input is made
        while True:
            choice = input("Choose display order: 'Breadth-First-Search' or 'Depth-First-Search'? ('BFS' and 'DFS' also accepted)").strip().lower()
            #Verify their choice resides within predetermined choice types.
            if choice in valid_choice:
                return choice
            #Prompt user if invalid input given.
            print("Invalid Input: Please enter 'BFS', 'DFS', 'Breadth-First-Search' or 'Depth-First-Search'")
    
    def verify_user(self, name):
        '''Helper Method: Verify the user exists within the directory. Prompt if user isn't in directory

        :type string: name, Name of user to varify.
        :rtype boolean: True if user found, False otherwise.
        '''
        while True:
            user = (name or input("enter a User's name: ")).strip()
            if user in self.dict_manager.get_keys():
                return user
            print(f'User: {user} does not exist within directory. Please enter a valid name.')
            #Force Reprompt
            name = None
        
            
