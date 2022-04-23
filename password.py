class User:
    userInfo = list()
    def __init__(self, userName, userPassword):
        self.userName, self.userPassword = userName, userPassword
    def setUserName(self, userName):
        self.userName = userName
    def getUserName(self):
        return self.userName
    def setUserPassword(self, userPassword):
        self.userPassword = userPassword
    def getUserPaswword(self):
        return self.userPaswword
    def __str__(self):
        return ("%s %d"%())  