#Written by Leah Gibbons, with contributions and testing from Bea Sauve

from profile_manager import ProfileManager

def main():
    manager = ProfileManager() #ProfileManager and its data will persist across users
    current_user = None #user identity cleared between logins
    print("*-----*-----*-----*-----*-----*-----*-----*-----*")
    print("*  Welcome to the Glubs Social Media Network!   *")
    print("*-----*-----*-----*-----*-----*-----*-----*-----*")
    while True: #Infinite loop until user enters exit code
        print("How would you like to login?")
        print("1. Login as user")
        print("2. Login as admin")
        print("99. Exit the program.")
        user_input = input(
            "Enter your selection: "
        ).strip().lower()
        if user_input == "1":
            current_user = login_user(manager)
            display_user_menu(manager, current_user)
        elif user_input == "2":
            current_user = login_user(manager)
            is_admin = admin_verification() #verify every time someone tries to login as admin
            if is_admin:
                display_admin_menu(manager, current_user)
            else:
                print("Unable to login as admin. Please try again.")
        elif user_input == "99":
            print("Thank you, come again!")
            return
        else:
            print("Sorry, I didn't recognize that input. Please try again: ")
    
def get_username():
    username = input(
        "Please enter your name: "
    ).strip().title()
    return username

def login_user(manager):
    username = input(
        "Please enter your name: "
    ).strip().title()
    if manager.


def admin_verification():
    while True:
        print("Administrators are required to enter a PASSWORD.")
        print("\(The password is \"uncrackable\"\)")
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
    print("User Menu:")
    print("1. Create a profile")
    print("2. Modify your profile")
    print("3. Add a friend")
    print("4. View your friend list")
    print("5. View your friend's friend list")
    print("6. Delete your profile.")
    print("7. Create graph of current user's network")
    print("11. Logout (end program)")
    user_input = input("Select your menu option: ").strip().lower()
    if user_input == "1": 
        create_profile(manager, current_user)
    elif user_input == "2":
        # This option can change the current user's name, so we need to always check for that.
        current_user = modify_profile(manager, current_user)
    elif user_input == "3":
        add_friend()
    elif user_input == "4":
        view_friend_list()
    elif user_input == "5":
        view_friends_of_friend()
    elif user_input == "6":
        create_user_network_graph()
    elif user_input == "11":
        return
    else:
        print("Sorry, I didn't recognize that input. Please try again: ")

def display_admin_menu(manager, current_user):
    print("Admin Menu:")
    print("1. Create a profile")
    print("2. Modify profile")
    print("3. View all profiles")
    print("4. Add a friend")
    print("5. View your friend list")
    print("6. View your friend's friend list")
    print("7. Delete a profile")
    print("8. Switch the current user")
    print("9. Read profiles from CSV")
    print("10. Create graph of current user's network")
    print("11. Logout (end program)")

    user_input = input("Select your menu option: ").strip().lower()

    if user_input == "1": 
        create_profile(manager, current_user)

    elif user_input == "2":
        #This option can change the current user's name, so we need to always check for that.
        current_user = modify_profile(manager, current_user, True)
    elif user_input == "3":
        view_all_profiles()
    elif user_input == "4":
        add_friend()
    elif user_input == "5":
        view_friend_list()
    elif user_input == "6":
        view_friends_of_friend()
    elif user_input == "7":
        delete_profile()
    elif user_input == "8":
        return
    elif user_input == "9":
        read_profiles_from_csv()
    elif user_input == "10":
        create_user_network_graph()
    elif user_input == "11":
        return
    else:
        print("Sorry, I didn't recognize that input. Please try again: ")

def search_prompt(self):
    '''Helper method: Verify users search choice.
    
    :rtype string: choice, users validated search type choice.
    '''
    #Predetermined choice types
    valid_choice = {'bfs', 'breadth-first-search', 'dfs', 'depth-first-search'}
    #Keep looping till a valid input is made
    while True:
        choice = input("Choose display order: 'Breadth-First-Search' or 'Depth-First-Search'? ('BFS' and 'DFS' also accepted): ").strip().lower()
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

# ****************
# | MENU OPTIONS |
# ****************

def create_profile(manager, current_user):
    if manager.contains_profile(current_user):
        print("A profile already exists under your current name.")
        while True:
            print("Options: ")
            print("1. Modify your existing profile.")
            print("2. Return to main menu.")
            user_input = input("Enter your selection: ")
            if user_input == "1":
                modify_profile(manager, current_user)
                return
            elif user_input == "2":
                return
            else:
                print("Sorry, I didn't understand that. Please try again.")
    else:
        print("Wonderful! You would like to create your profile.")
        print("Let's get some information about you!")
        location = input(
            "What is your location?"
        ).strip().title()
        relationship_status = validate_relationship_input() 
        if relationship_status == "":
            print("Skipping adding relationship status.")
        age = input(
            "What is your age?"
        ).strip()
        occupation = input(
            "What is your occupation?"
        ).strip().title()
        astrological_sign = input(
            "What is your astrological sign?"
        ).strip().title()
        status = input(
            "What are you up to right now?"
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
                    print("Success! Your profile picture has been added. You will be returned to the main menu.")
                return
            elif user_input == "2":
                print("Skipping adding profile picture...")
                print("Returning to main menu...")
                return
            else:
                print("Sorry, I didn't understand that. Please try again.")



def modify_profile(manager, current_user, is_admin=False):
    if is_admin:
        user_to_modify = admin_user_selection(manager, current_user, "Whose profile would you like to modify?")
        if user_to_modify == "":
            return current_user
    else:
        user_to_modify = current_user

    while True:
        print("What would you like to modify?")
        print("1. Name")
        print("2. Relationship status")
        print("3. Status")
        print("99. Return to main menu.")
        user_input = input(
            "Enter your choice: "
        ).strip()
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
            elif current_user == user_to_modify:
                    user_to_modify = new_name
                    current_user = new_name 
        elif user_input == "2":
            relationship_status = validate_relationship_input()
            if relationship_status != "":
                manager.get_value(user_to_modify).set_relationship(relationship_status)
        elif user_input == "3":
            new_status = input(
                "Enter the new status: "
            ).strip()
            manager.get_value(user_to_modify).set_status(new_status)
        else:
            print("Sorry, I didn't understand that. Please try again.")




    

            
        
            






# **********************
# * INPUT VALIDATION   *
# **********************


def validate_relationship_input():
        
        relationship_dictionary = {
            "1": "Single",
            "single": "Single",
            "2": "In a Relationship",
            "in a relationship": "In a Relationship",
            "3": "Married",
            "married": "Married",
        }

        while True: 
            print("What is your relationship status?:")
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
    while True:
        user_input = input(
            "Please enter the name of your jpg file, or enter 99 to return to the main menu."
        ).strip()
        if user_input.lower().endswith(".jpg"):
            return user_input
        elif user_input == "99":
            return ""
        else: 
            print("Photo must be a jpg file. Please try again.")

def validate_existing_username(manager):
    while True:
        user_input = input(
            "Please enter the username: "
        ).strip().title()
        if user_input == "99":
            return ""
        elif manager.contains_profile(user_input):
            return user_input
        else: print("Sorry, that username does not exist on our network. Please try again, or enter 99 to return.")

def admin_user_selection(manager, current_user, prompt):
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









        
        



