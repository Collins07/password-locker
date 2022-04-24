class User:
    """
    generate new instances of users
    """
    userslist=[]
    def __init__(self, firstname, lastname, username, password):
        """
        method to define properties for objects
        """
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
    def save_user(self):
        """
        method saves user into users list
        """  
        User.userslist.append(self)
    def delete_user(self):
        """
        removes user from list
        """
        User.userslist.remove(self)

    @classmethod
    def display_users(cls):
        """
        return info from users
        """
        return cls.userslist

    @classmethod
    def find_by_number(cls, number):
        """
        
        """    
