'''Authors: Bea Sauve (psudocode) and Leah Gibbons(code implementation)  Date:12/08/25  Class: Ad325'''
'''Example psudocode for main'''

class Main:
    def __init__():
        #create the initial profile manager
        self.manage_profiles = ProfileManager()


    def login():
        input("Enter 1, 2, or 3: 1)Log in as Manager   2)Log in as User 3)Create a profile")
        if input == 1:
            manager_menu()
        if input == 2:
            name = input("Enter User Name: ")
            #validate the profile then move to the menu with the profile
            profile = self.manage_profiles.get_profile(name)
            user_menu(profile)
        if input == 3:
            create_profile()
        else:
            #error retry input

    def manager_menu():
        input(#display menu provided in assignment)
        ''' 
        if 1: 
            create_user()
            manager_menu()
        if 2:
            name = input(which profile would you like to modify? #display all avalible profiles)
            #validate the name then pass the profile over for modification
            to_modify = self.profile_manager.get_profile(name)
            modify_profile(to_modify, 'manager'):

        '''
    def user_menu(user_profile):
    '''
        current_user = self.profile_manager.get_profile(name):
        input(#display user menu
            1) Modify profile, 2)view all profiles, 3)add a friend, 4)remove a friend  5)view friends list  6)view friends of friends 7)delete profile 8)create graph 9)logout )
            if 1:
                  modify_profile(user_profile, 'user')

            '''

|========Helper Methods======================================|

    def create_profile():
    '''
        create_user()
        input("would you like to 1)log in as user 2)return to menu? Enter 1 or 2")
        if 1: user_menu()
        if 2: login()
        else invalid input
        '''
    
    def create_user():
    '''
        name = input(name)
        location = input(location),...(same thing for these variables) relationship_status, age, occupation, astrological_sign,
        status = "Offline"
        user = (enter all variable that were just requested)
        input('would you like to add a photo? Enter yes or no")
        if yes:
            photo = input(list photo name):
        user.add_photo()
        if no:
            return None

        manager.add_user_profile(user)
        print(profile made)
    '''
    def modify_profile(user_profile, user_type):
        '''Modify the given users profile then return back to the menu of authorizer.
        
        :type any: user_profile, profile object of the user.
        :type string: user_type, the account type that is doing the modifying. Indicates which menu to return to.
        '''
        '''
        input(what would you like to modify?
                1) Name
                2) Location
                #include relationship_status, age, occupation, astrological_sign, add photo
        if 1: user_profile.set_name(input("Enter your new name"))
        if 2: user_profile.set_location(input("Enter your new location"))
        if 3: ...
        else: #invalid input
        input(  1)Continue to modify  2)return to menu)
        if 1) reloop
        if 2: 
            if user_type == 'user':
               user_menu(user_profile.get_name())
            if user_type == 'manager':
                manager_menu()


        '''