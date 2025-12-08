from graph_adts import UndirectedGraph
from linked_adts import LinkedDictionary
from user_profile import UserProfile
import csv

class ProfileManager:
    def __init__(self):
        '''Create the profile manager'''
        self.dict_manager = LinkedDictionary()
        self.graph_manager = UndirectedGraph()

    def add_profile(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        ''' Add a user profile to the profile manager'''
        user = UserProfile(name, location, relationship_status,age, occupation, astrological_sign, status)
        self.dict_manager.add(name, user)

    def get_profile(self, name):
        '''Obtain user profile from the profile manager
        @return profile(vertex): Users profile stored in the undirected graph manager'''
        return self.dict_manager.get_value(name)
    
    def remove_profile(self, name):
        '''TODO: Figure this out'''
        ''' Remove a users profile from the undirected graph (and other locations)'''
        self.dict_manager.remove(name)
        
    def connect_profiles(self, name1, name2, weight=0):
        self.manager.add_edge(name1, name2, weight = 0)

    def display_profiles(self):
        '''TODO: figure out where to start display from and if search methods return a list'''
        choice = self.search_prompt()
        if choice == 'bfs' or choice == 'breadth-first-search':
            # Display all the profiles in bfs order
            return self.manager.bfs()
        else:
            # Display all profiles in dfs order
            return self.manager.dfs()
        

    def display_profile_details(self, name):
        ''' If user exists in directory, display their profile details
        @return (str): String of users information'''
        # Ensure the name is of a valid user
        if self.verify_user(name):
            #Store user information
            user = self.manager.get_vertex(name)
            return user.print_details()
        # Error raised if user doesn't exist. Return None
        else:
            return None
            
    def get_friends_of_friends(self, name):
        ''' Obtain a list of friends of a users friends
        @return'''
        # Ensure the user exists
        if self.verify_user(name):
            #prompt user for search type
            choice = self.search_prompt()
            #access user profile
            user = self.manager.get_vertex(name)
            #get users friends
            friends = user.get_friends()
            #loop get friends of friend, use search based on users request
            for friend in friends:
                if choice == 'bfs' or choice == 'breadth-first-search':
                    self.manager.bfs(friend)
                else:
                    self.manager.dfs(friend)
        # Error raised if user not valid, return none
        else:
            return None

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
        return
    
    def search_prompt(self):
        valid_choice = {'bfs', 'breadth-first-search', 'dfs', 'depth-first-search'}
        # keep looping till a valid input is made
        while True:
            choice = input("Choose display order: 'Breadth-First-Search' or 'Depth-First-Search'? ('BFS' and 'DFS' also accepted)").strip().lower()
            if choice in valid_choice:
                return choice
            print("Invalid Input: Please enter 'BFS', 'DFS', 'Breadth-First-Search' or 'Depth-First-Search'")
    
    def verify_user(self, name):
        ''' verify the user exists within the directory
        @return (boolean): True if user found, False otherwise'''
        if self.manager.contains(name):
            return True
        print(f'User: {name} does not exist within directory. Please enter a valid name.')
        return False
        
            
