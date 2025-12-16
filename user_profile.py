''' Author: Bea Sauve   Date: 12/06/2025  Class: A325
Building class to construct User Profiles
'''

class UserProfile:
    
    def __init__(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        '''The constructor for the class'''
        self.name = name
        self.location = location
        self.relationship_status = relationship_status
        self.age = age
        self.occupation = occupation
        self.astrological_sign = astrological_sign
        self.status = status
        self.friends = []
        self.photo = "Photo not avalible"
        self.activity = "Offline"

    def get_name(self):
        ''' Obtiain Users name.

        :rtype string: name, Users name.
        '''
        return self.name
    
    def set_name(self, name):
        ''' Modify name of users profile.
        
        :type string: name, Name to add to profile.
        '''
        self.name = name

    def get_location(self):
        ''' Obtain Users location.

        :rtype string: location, Users location.
        '''
        return self.location

    def get_relationship_status(self):
        ''' Obtain Users relationship status

        :rtype string: relationship_status, Users relationship status.
        '''
        return self.relationship_status

    def get_age(self):
        '''Obtain users age.

        :rtype int: age, Users age.
        '''
        return self.age

    def get_occupation(self):
        '''Obtain users occupation.

        :rtype string: occupation, Users occupation.
        '''
        return self.occupation

    def get_astrological_sign(self):
        '''Obtain Users astrological sign

        :rtype string: astrological_sign, Users astro sign.
        '''
        return self.astrological_sign

    def get_status(self):
        '''Obtain Users relationship status

        :rtype string: status, Users relationship status.
        '''
        return self.status

    def set_relationship(self, status):
        '''Set users relationship status, within allowed relationship statuses
        
        :type string: status, relationship the user is in'''
        #Validate status given
        if not status:
            print("Invalid Status. Please choose: 1) Single, 2) In a Relationship, 3) Married")
            return
        choice = status.strip().lower()
        # Accept both numeric shortcuts and textual labels
        mapping = {
            "1": "Single",
            "single": "Single",
            "2": "In a Relationship",
            "in a relationship": "In a Relationship",
            "3": "Married",
            "married": "Married",
        }
        #Update relationship status if it resides within mapping
        if choice in mapping:
            self.relationship_status = mapping[choice]
            return
        print("Invalid Status. Please choose: 1) Single, 2) In a Relationship, 3) Married")

    def set_status(self, status):
        '''Set users activity status
        
        :type boolean: True if user is online, False if offline
        '''
        self.status = status
    
    def set_activity(self, activity = bool):
        '''Set the user activity to 'Online' or 'Offline
        
        :type boolean: activity, indicates whether the user is actively online or not
        '''
        if activity == True:
            self.activity = 'Online'
        else:
            self.activity = 'Offline'

    def get_friends(self):
        '''Obtain all friends in friends list

        :rtype list: friends, list of users friends.'''
        return self.friends

    def add_friend(self, friend_profile):
        '''Add a friend to friends list.
        
        :type string: friend_profile, Name of friend to add.
        '''
        if friend_profile not in self.get_friends():
            self.friends.append(friend_profile)

    def remove_friend(self, friend_profile):
        '''Remove a friend from friends list
        
        :type any: friend_profile, profile to remove from list
        '''
        if friend_profile in self.get_friends():
            self.friends.remove(friend_profile)

    def print_details(self):
        '''Display all details of user.
        
        :rtype string: Details of users profile.
        '''
        print(
            f"|===================={self.name}'s Profile====================|\n"
            f"Image: {self.photo}\n"
            f"Status: {self.status:<18} Currently: {self.activity}\n"
            f"Name: {self.name:<20} Relationship Status: {self.relationship_status} \n"
            f"Age: {self.age:<21} Astrological Sign: {self.astrological_sign}\n"
            f"Occupation: {self.occupation:<14} Location: {self.location}\n"
            f"Friends List: {self.friends}\n"
            f"|=============================================================|"
        )


    def add_photo(self, photo):
        '''Add a photo to profile.
        
        :type string: photo, String reference to photo.
        '''
        '''User may add a profile photo if they choose'''
        substring = ".jpg"
        if substring in photo:
            self.photo = photo
        else:
            print(f'{photo} does not contain "{substring}')