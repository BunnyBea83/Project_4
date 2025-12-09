'''Authors: Bea Sauve (psudocode) and Leah Gibbons(code implementation)  Date:12/08/25  Class: Ad325'''
'''Example psudocode for main'''

class Main:
    def __init__():
        #create the initial profile manager
        self.manage_profiles = ProfileManager()

    def main():
        '''Run the whole program'''
        login()


    def login():
        ''' Initial menu allowing the user to choose how to navigate through the program
        
        User may log in as a manager, log in as a user, create a profile, or exit
        '''
        input("Enter 1, 2, or 3: 1)Log in as Manager   2)Log in as User 3)Create a profile 4)Exit")
        if input == 1:
            manager_menu()
        if input == 2:
            name = input("Enter User Name: ")
            #validate the profile then move to the menu with the profile
            profile = self.manage_profiles.get_profile(name)
            user_menu(profile)
        if input == 3:
            create_profile('user')
        if input == 4:
            #exit the program
        else:
            #error retry input

    def manager_menu():
        '''Manager menu display operations the manager may preform while accessing their profile
        
        Operation include: they may modify profiles, read csv files to manager, switch between profiles, and display relationships of profiles
        
        '''
        input(#display menu provided in assignment)
        ''' 
        if 1: 
            create_user('manager')
            manager_menu()
        if 2:
            name = input(which profile would you like to modify? #display all avalible profiles)
            #validate the name then pass the profile over for modification
            to_modify = self.profile_manager.get_profile(name)
            modify_profile(to_modify, 'manager'):


        To be continued...

        '''
    def user_menu(user_profile):
    '''User menu display operations the user may preform while accessing their profile
    
    Operations include: modifying their own profile, adding and removing friends, and displaying relationships between friends
    '''
    '''
        #set users status to online
        user_profile.set_status(True)
        #prompt the user for what they would like to do
        input(#display user menu
            1) Modify profile, 2)view all profiles, 3)add a friend, 4)remove a friend  5)view friends list  6)view friends of friends 7)delete profile 8)create graph 9)logout )
        #1) modify your profile, passing in current profile, and status of 'user'
        if 1:
                modify_profile(user_profile, 'user')

        To be continued...

        #9) log out of the program
        input == 9:
            #set status to offline
            profile.set_status(False)
            #exit the program

            '''

|========Helper Methods======================================|

    def create_profile(user_type):
    '''Helper method of create user
    
    Calls the create user profile method, then asks the user if they would like to navigate to said profile or return to log in menu
    '''
    '''
        create_user()
        if user_type == 'manager':
            manager_menu()
        if user_type == 'user':
            input("would you like to 1)log in as user 2)return to menu? Enter 1 or 2")
            if 1: 
                user_menu()
            if 2: 
                login()
        else invalid input
        '''
    
    def create_user():
    '''Create a profile and add it to the Profile Manager
    
    '''
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
        #Return to either the user menu or manager menu depending ot the user_type that was passed
        if 2: 
            if user_type == 'user':
               user_menu(user_profile.get_name())
            if user_type == 'manager':
                manager_menu()


        '''