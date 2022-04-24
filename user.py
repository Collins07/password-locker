class User:
    """
     new instances of users
    """
    userslist=[]
    def __init__(self, firstname, lastname, username, password):
        """
         to define properties for objects
        """
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
    def save_user(self):
        """
         saves user into users list
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
        takes username and returns if it matches the number
        """
        for user in cls.userslist:
            if user.password == number:
                return user

    @classmethod
    def user_exists(cls, number):
        for user in cls.userslist:
            if user.username == number:
                return True
                return False




