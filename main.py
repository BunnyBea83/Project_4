#Written by Leah Gibbons, with contributions and testing from Bea Sauve

from profile_manager import ProfileManager
PROFILES_DATA_FILE_PATH = "data/profiles.csv" 

def main():
    """Displays welcome banner and login menu."""

    manager = ProfileManager() #ProfileManager and its data will persist across users
    close_program = False

    print("*-----*-----*-----*-----*-----*-----*-----*-----*")
    print("*  Welcome to the Glubs Social Media Network!   *")
    print("*-----*-----*-----*-----*-----*-----*-----*-----*")

    #Basic loop concept for this menu and other menus in this program:
    #The menu will display information.
    #Then the user will be prompted for input which will cause the program to take actions, display more information, and re-prompt for further input.
    #This process will loop forever until a special user input is received which causes the function to return.
    while True: 

        if close_program:
            print("Goodbye!")
            return
        current_user = None #user identity cleared between logins

        print("How would you like to login?")
        print("1. Login as user")
        print("2. Login as admin")
        print("99. Exit the program.")

        user_input = input(
            "Enter your selection: "
        ).strip().lower()
        if user_input == "1":
            current_user = login_user(manager)
            if current_user != "":
                close_program = display_user_menu(manager, current_user)
            else:
                print("Login failed. Please try again.")
        elif user_input == "2":
            current_user = login_user(manager)
            if current_user != "":
                is_admin = admin_verification() #verify every time someone tries to login as admin
                if is_admin:
                    close_program = display_admin_menu(manager, current_user)
                else:
                    print("Unable to verify admin credentials. Please login again.")
            else:
                print("Login failed. Please try again.")
            
        elif user_input == "99":
            close_program = True
        else:
            print("Sorry, I didn't recognize that input. Please try again: ")
    

def login_user(manager):
    """Prompts the user to enter their name. New users will be required to create a profile.
    
    :type ProfileManager: the session's ProfileManager
    :rtype string: the user's name"""
    username = input(
        "Please enter your name: "
    ).strip().title()
    if manager.contains_profile(username):
        print(f"Welcome back, {username}!")
        return username
    else:
        print(f"Welcome, {username}!")
        profile_created = create_profile(manager, username)
        if profile_created:
            return username
        else:
            return "" 


def admin_verification():
    """Password verification for admin logins.
    
    :rtype boolean: True if admin credentials were successfully verified, False otherwise.
    """
    while True:
        print("Administrators are required to enter a PASSWORD.")
        print("(The password is uncrackable)")
        user_input = input(
            "Enter the password, or enter 99 to return to the login menu: "
        ).strip().lower()
        if user_input == "uncrackable":
            return True
        elif user_input == "99":
            return False
        else:
            print("Incorrect password. Please try again: ")


def display_user_menu(manager, current_user):
    """Displays menu options for regular users.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :rtype boolean: True if the user chooses to quit the program, False to send them back to the login menu.
    """
    user_was_deleted = False
    while True: 

        #If the user deleted their profile, force logout.
        if user_was_deleted:
            print("Logging out...")
            return False
        
        print(f"User Menu: Logged in as {current_user}")
        print("1. Modify your profile")
        print("2. Add a friend")
        print("3. View your friend list")
        print("4. View a friend's friend list")
        print("5. Delete your profile.")
        print("6. Switch the current user.")
        print("7. Create graph of current user's network.")
        print("8. Logout (end program)")
        user_input = input(
            "Select your menu option: "
        ).strip().lower()

        if user_input == "1":
            # This option can change the current user's name, so we need to always check for that.
            current_user = modify_profile(manager, current_user)
        elif user_input == "2":
            add_friend(manager, current_user)
        elif user_input == "3":
            view_friends(manager, current_user)
        elif user_input == "4":
            view_friends_of_friends(manager, current_user)
        elif user_input == "5":
            user_was_deleted = delete_profile(manager, current_user)
        elif user_input == "6":
            print("Logging out as current user...")
            return False
        elif user_input == "7":
            create_user_network_graph(manager, current_user)
        elif user_input == "8":
            return True
        else:
            print("Sorry, I didn't recognize that input. Please try again: ")

def display_admin_menu(manager, current_user):
    """Displays menu options for users with admin persmissions.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :rtype boolean: True if the user chooses to quit the program, False to send them back to the login menu.
    """

    user_was_deleted = False

    while True: 

        #If the user deleted their profile, force logout.
        if user_was_deleted:
            print("Logging out...")
            return False
        
        print(f"Admin Menu: Logged in as {current_user}")
        print("1. Create a profile")
        print("2. Modify profile")
        print("3. View all profiles")
        print("4. Add a friend")
        print("5. View your friend list")
        print("6. View anyone's friend list")
        print("7. Delete a profile")
        print("8. Switch the current user")
        print("9. Read profiles from CSV")
        print("10. Create graph of current user's network")
        print("11. Logout (end program)")

        user_input = input("Select your menu option: ").strip().lower()

        if user_input == "1": 
            create_profile(manager, current_user, True)
        elif user_input == "2":
            #This option can change the current user's name, so we need to always check for that.
            current_user = modify_profile(manager, current_user, True)
        elif user_input == "3":
            view_all_profiles(manager)
        elif user_input == "4":
            add_friend(manager, current_user)
        elif user_input == "5":
            view_friends(manager, current_user)
        elif user_input == "6":
            view_friends_of_friends(manager, current_user, True)
        elif user_input == "7":
            delete_profile(manager, current_user, True)
        elif user_input == "8":
            print("Logging out as current user...")
            return False
        elif user_input == "9":
            read_profiles_from_csv(manager)
        elif user_input == "10":
            create_user_network_graph(manager, current_user)
        elif user_input == "11":
            return True
        else:
            print("Sorry, I didn't recognize that input. Please try again: ")

# ****************
# | MENU OPTIONS |
# ****************

def create_profile(manager, current_user, is_admin=False):
    """Creates a new user profile with several prompts for user input.

    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :type boolean: True if the user has admin permissions, False otherwise.
    :rtype boolean: True if a user successfully created their own profile, False otherwise.
    """

    #Regular users can only access this method when creating their own profile.
    if not is_admin and manager.contains_profile(current_user):
        print("A profile already exists under this name.")
        print("Returning to main menu...")
        return False
    
    #Admins can create profiles on behalf of others.
    elif manager.contains_profile(current_user):
        print("Admin: You are creating a new profile for someone else.")
        print("Let's get their information!")
        new_user = input(
            "What is their name? "
        ).strip().title()
        location = input(
            "What is their location? "
        ).strip().title()
        relationship_status = validate_relationship_input() 
        if relationship_status == "":
            print("Skipping adding relationship status.")
        age = validate_integer_input("What is their age? ")
        occupation = input(
            "What is their occupation? "
        ).strip().title()
        astrological_sign = input(
            "What is their astrological sign? "
        ).strip().title()
        status = input(
            "What are they up to right now? "
        ).strip()

        manager.add_profile(new_user, location, relationship_status, age, occupation, astrological_sign, status)

        print(f"Success! A new profile has been created under the name {new_user}")
        while True: 
            print("Would you like to add a profile picture?")
            user_input = input(
                "Enter 1 for yes or 2 for no: "
            )
            if user_input == "1":
                new_profile = manager.get_profile(current_user)
                photo = validate_jpg()
                if photo != "":
                    new_profile.add_photo(photo)
                    print("Success! Their profile picture has been added")
                return False
            elif user_input == "2":
                print("Skipping adding profile picture...")
                return False
            else:
                print("Sorry, I didn't understand that. Please try again.")

    
    #Initial profile creation for the current user.
    else:
        print("Wonderful! You would like to create a new profile.")
        print("Let's get some information about you!")
        location = input(
            "What is your location? "
        ).strip().title()
        relationship_status = validate_relationship_input() 
        if relationship_status == "":
            print("Skipping adding relationship status.")
        age = validate_integer_input("What is your age? ")
        occupation = input(
            "What is your occupation? "
        ).strip().title()
        astrological_sign = input(
            "What is your astrological sign? "
        ).strip().title()
        status = input(
            "What are you up to right now? "
        ).strip()

        manager.add_profile(current_user, location, relationship_status, age, occupation, astrological_sign, status)

        print(f"Success! Your profile has been created under the name {current_user}")
        while True: 
            print("Would you like to add a profile picture?")
            user_input = input(
                "Enter 1 for yes or 2 for no: "
            )
            if user_input == "1":
                new_profile = manager.get_profile(current_user)
                photo = validate_jpg()
                if photo != "":
                    new_profile.add_photo(photo)
                    print("Success! Your profile picture has been added")
                return True
            elif user_input == "2":
                print("Skipping adding profile picture...")
                return True
            else:
                print("Sorry, I didn't understand that. Please try again.")



def modify_profile(manager, current_user, is_admin=False):
    """Allows the user to modify their profile, or for administrators, to modify any profile.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :type boolean: True if the user has admin permissions, False otherwise.
    :rtype string: the current user's name
    """

    #Admins are asked whether they want to modify their own or someone else's profile.
    if is_admin:
        user_to_modify = admin_user_selection(manager, current_user, "Whose profile would you like to modify?")
        if user_to_modify == "":
            return current_user
    else:
        user_to_modify = current_user

    while True:
        print(f"You are modifying {user_to_modify}'s profile. What would you like to modify?")
        print("1. Name")
        print("2. Relationship status")
        print("3. Status")
        print("99. Return to main menu.")
        user_input = input(
            "Enter your choice: "
        ).strip().lower()
        if user_input == "99":
            return current_user
        elif user_input == "1":
            new_name = input(
                "Enter the new name: "
            ).strip().title()
            success = manager.change_name(user_to_modify, new_name)
            if not success:
                print("I'm sorry, we weren't able to make that name change.")
                print("This may be because the old name wasn't found in our network,")
                print("or because the new name already does exist in our network.")

            #If the user has changed their own name, update their name in this method and in the return.
            elif current_user == user_to_modify:
                    user_to_modify = new_name
                    current_user = new_name 
        elif user_input == "2":
            relationship_status = validate_relationship_input()
            if relationship_status != "":
                manager.get_profile(user_to_modify).set_relationship(relationship_status)
        elif user_input == "3":
            new_status = input(
                "Enter the new status: "
            ).strip().lower()
            manager.get_profile(user_to_modify).set_status(new_status)
        else:
            print("Sorry, I didn't understand that. Please try again.")

def view_all_profiles(manager):
    """Allows the user to view a list of all profiles using either a breadth-first or a depth-first search.
    
    :type ProfileManager: The session's ProfileManager
    """
    while True:
        print("What search method would you like to use to view all profiles in the network?")
        print("1. Breadth-first search")
        print("2. Depth-first search")
        print("99. Return to main menu.")
        user_input = input(
            "Enter your selection: "
        ).strip().lower()
        if user_input == "99":
            return
        elif user_input == "1":
            print(manager.display_profiles("bfs"))
        elif user_input == "2":
            print(manager.display_profiles("dfs"))
        else:
            print("I'm sorry, I didn't understand that. Please try again.")

def add_friend(manager, current_user):
    """Allows the user to add their friends.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    """
    while True:
        friend_to_add = input(
            "Enter the name of the friend you would like to add, or enter 99 to return to the main menu: "
        ).strip().title()

        #User may exit to main menu
        if friend_to_add == "99":
            return
        
        #Disallow adding self as friend
        elif friend_to_add == current_user:
            print("You cannot add yourself as a friend! Would you like to try again?")

        #Disallow adding friends not in the network
        elif not manager.contains_profile(friend_to_add):
            print("Sorry, this friend hasn't joined the Glubs Social Media Network yet!")
            print("Would you like to enter the name of a different friend?")

        #Disallow adding users who are already friends
        elif friend_to_add in manager.get_friends_of_friends(current_user, "bfs"):
            print("This user is already your friend! Would you like to add a different friend?")

        #Add friend
        else:
            successful = manager.connect_profiles(current_user, friend_to_add)
            if successful: 
                print(f"{friend_to_add} was successfully added as your friend!")
                print("Would you like to add another friend?")
            else:
                print("Sorry, something went wrong! Would you like to try again?")


def view_friends(manager, current_user):
    """Allows the user to view their own friends using either BFS or DFS.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    """
    while True:
        print(f"What search method would you like to use to view your friends?")
        print("1. Breadth-first search")
        print("2. Depth-first search")
        print("99. Return to main menu.")
        user_input = input(
            "Enter your selection: "
        ).strip().lower()
        if user_input == "99":
            return
        elif user_input == "1":
            print(manager.get_friends_of_friends(current_user, "bfs"))
        elif user_input == "2":
            print(manager.get_friends_of_friends(current_user, "dfs"))
        else:
            print("I'm sorry, I didn't understand that. Please try again.")

def view_friends_of_friends(manager, current_user, is_admin=False):
    """Allows the user to view a friend's friend list, or for admins, to view anyone's friend list.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :type boolean: True if the user has admin permissions, False otherwise.
    """
    #Admins may choose to view their own or anyone else's friends.
    if is_admin:
        user_to_get_friends = admin_user_selection(manager, current_user, "Whose friends would you like to view? ")
        if user_to_get_friends == "":
            return
        
    #Regular users may only view their friends' friend lists.
    else:
        user_to_get_friends = verify_user_is_friend(manager, current_user, "Whose friends would you like to view? ")
        if user_to_get_friends == "":
            return

    while True:
        print(f"What search method would you like to use to view the friends of {user_to_get_friends}?")
        print("1. Breadth-first search")
        print("2. Depth-first search")
        print("99. Return to main menu.")
        user_input = input(
            "Enter your selection: "
        ).strip()
        if user_input == "99":
            return
        elif user_input == "1":
            print(manager.get_friends_of_friends(user_to_get_friends, "bfs"))
        elif user_input == "2":
            print(manager.get_friends_of_friends(user_to_get_friends, "dfs"))
        else:
            print("I'm sorry, I didn't understand that. Please try again.")


def delete_profile(manager, current_user, is_admin=False):
    """Allows the user to delete their profile, or for administrators, to delete any profile.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :rtype boolean: True if the user successfully deletes their own profile, False otherwise.
    """
    
    #Admins may choose to delete their own or someone else's profile.
    user_to_delete = current_user
    if is_admin:
        user_to_delete = admin_user_selection(manager, current_user, "Whose account would you like to delete?")

    while True:
        #Give user a chance to change their mind before deleting the profile.
        print(f"Really delete {user_to_delete}'s profile?")
        print("1. Yes")
        print("2. No (return to main menu)")
        user_input = input(
            "Enter your choice: "
        ).strip().lower()

        #The user will be returned to the main menu after the profile is deleted or the deletion failed. 
        #If they deleted their own profile, they will be logged out as well.
        if user_input == "1":
            success = manager.remove_profile(user_to_delete)
            if success: 
                print(f"{user_to_delete}'s profile has been deleted.")
                return user_to_delete == current_user 
            else:
                print("Sorry, something went wrong and the deletion was unsuccessful. Returning to main menu.")
                return False
        elif user_input == "2":
            return False
        else: 
            print("Sorry, I didn't understand that. Please try again.")

def read_profiles_from_csv(manager):
    """Builds the social network from the provided csv file.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    """
    print("Building profiles from data file...")
    try:
        manager.read_profiles_from_csv(PROFILES_DATA_FILE_PATH)
        print("Profiles successfully loaded from data file!")
        print("Returning to main menu...")
        return 
    except FileNotFoundError:
        print("Error: The file was not found. Unable to build profiles from csv.")
        print("Returning to main menu...")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Unable to build profiles from csv.")
        print("Returning to main menu...")
        return
    

def create_user_network_graph(manager, current_user):
    """Creates a graph of the current user's network.

    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    """
    manager.create_user_graph(current_user,1)


            






# **********************
# * INPUT VALIDATION   *
# **********************


def validate_relationship_input():
        """Validates relationship status input.
        
        :rtype string: The valid, recognized relationship status, or an empty string if the user exits without entering a valid input.
        """
        
        #Permitted inputs and their mappings
        relationship_dictionary = {
            "1": "Single",
            "single": "Single",
            "2": "In a Relationship",
            "in a relationship": "In a Relationship",
            "3": "Married",
            "married": "Married",
        }

        while True: 
            print("Current relationship status?")
            print("1. Single")
            print("2. In a relationship")
            print("3. Married")
            print("99. Return to previous menu without entering relationship status.")
            user_input = input(
                "Enter your selection: "
            ).strip().lower()
            if user_input == "99":
                return ""
            elif user_input not in relationship_dictionary:
                print("Sorry, I didn't understand that. Please try again.")
            else: 
                return relationship_dictionary[user_input]

def validate_jpg():
    """Validates that a string is a jpg file name.
    
    :rtype string: the valid jpg file name, or an empty string if the user exits without entering a valid input.
    """
    while True:
        user_input = input(
            "Please enter the name of your jpg file, or enter 99 to return to the main menu. "
        ).strip()
        if user_input.lower().endswith(".jpg"):
            return user_input
        elif user_input == "99":
            return ""
        else: 
            print("Photo must be a jpg file. Please try again.")

def validate_existing_username(manager):
    """Prompts the user for a valid username that exists in the current network.

    :type ProfileManager: manager, the session's ProfileManager.
    :rtype string: a valid username connected to an existing profile, or an empty string if the user exits.
    """
    while True:
        user_input = input(
            "Please enter the username: "
        ).strip().title()
        if user_input == "99":
            return ""
        elif manager.contains_profile(user_input):
            return user_input
        else: print("Sorry, that username does not exist on our network. Please try again, or enter 99 to return.")

def validate_integer_input(prompt):
    """Prompts the user for a valid integer input.
    
    :type string: prompt, the specific prompt to be used
    :rtype int: A valid integer
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid integer.")


def admin_user_selection(manager, current_user, prompt):
    """Allows an admin to choose whether they wish to perform an operation on themselves or on a different user in the network.
    
    :type ProfileManager: the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :type string: prompt, the specific prompt to be used
    :rtype string: A valid username of someone on the network
    """
    while True:
            print(prompt)
            print("1. Yours")
            print("2. Someone else's")
            print("99. Return to main menu.")
            user_input = input("Enter your selection: ")
            if user_input == "1":
                return current_user
            elif user_input == "2":
                return(validate_existing_username(manager))
            elif user_input == "99":
                return ""
            else:
                print("Sorry, I didn't understand that. Please try again.")

def verify_user_is_friend(manager, current_user, prompt):
    """Prompts a user to choose a valid friend from their friends list.
    
    :type ProfileManager: manager, the session's ProfileManager
    :type string: current_user, the user who is logged in.
    :type string: prompt, the specific prompt to be used.
    :rtype string: A valid friend of the user, or an empty string if the user exits the menu.
    """

    #Get the user's friend list
    friend_list = manager.get_friends_of_friends(current_user, "bfs")

    while True:
        print(prompt)
        friend_name = input("Enter your friend's name: ").strip().title()
        if friend_name == "99":
            return ""
        elif friend_name in friend_list:
            return friend_name
        else:
            print("Sorry, we couldn't find that person in your friends list.")
            print("Please try again, or enter 99 to return.")





# Execute
if __name__ == "__main__":
    main()


        
        



