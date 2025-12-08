''' Author: Bea Sauve   Date: 12/06/2025  Class: A325
Building class to construct User Profiles
'''

class UserProfile:
    ALLOWED_RELATIONS = {"single", "in a relationship", "married"}
    def __init__(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        self.name = name
        self.location = location
        self.relationship_status = relationship_status
        self.age = age
        self.occupation = occupation
        self.astrological_sign = astrological_sign
        self.status = status
        self.friends = []
        self.photo = "Photo not avalible"


    def get_name(self):
        ''' Obtiain Users name
        @return name(string): Users name'''
        return self.name
    
    def set_name(self, name):
        ''' Modify name of users profile'''
        self.name = name


    def get_location(self):
        ''' Obtain Users location
        @return location(string): Users location'''
        return self.location


    def get_relationship_status(self):
        ''' Obtain Users relationship status
        @return relationship_status(string): Users relationship status'''
        return self.relationship_status


    def get_age(self):
        '''Obtain users age
        @return age(int): Users age'''
        return self.age


    def get_occupation(self):
        '''Obtain users occupation
        @return occupation(string): Users occupation'''
        return self.occupation


    def get_astrological_sign(self):
        '''Obtain Users astrological sign
        @return: astrological_sign(string): Users astro sign'''
        return self.astrological_sign


    def get_status(self):
        '''Obtain Users relationship status
        @return status(string): Users relationship status'''
        return self.status


    def set_status(self, status):
        '''Set users relationship status, within allowed relationship statuses'''
        if status and status.lower() in self.ALLOWED_RELATIONS:
            self.status = status
        print("Invalid Status. Please enter: Single, In a Relationship, or Married")


    def get_friends(self):
        '''Obtain all friends in friends list
        @return friends(list): list of users friends'''
        return self.friends


    def add_friend(self, friend_profile):
        '''Add a friend to friends list'''
        self.friends.append(friend_profile)


    def remove_friend(self, friend_profile):
        '''Remove a friend from friends list'''
        self.friends.remove(friend_profile)


    def print_details(self):
        '''Display all details of user'''
        print(f'Image: {self.photo}/nStatus: {self.status}/nName: {self.name}/n'
              f'Age: {self.age:>5} Occupation: {self.occupation:>22} Location: {self.location}/n'
              f'Relationship Status: {self.relationship_status:>18} Astrological Sign: {self.astrological_sign} /n'
              f'Friends List: {self.friends}')


    def add_photo(self, photo):
        '''Add a photo to profile'''
        '''User may add a profile photo if they choose'''
        substring = ".jpg"
        if substring in photo:
            self.photo = photo
        else:
            print(f'{photo} does not contain "{substring}')
