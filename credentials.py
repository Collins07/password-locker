class Credentials:
    accounts=[]

    def __init__(self, accountusername, accountname, accountpassword):
        """
        defines properties for objects
        """
        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword

    def save_account(self):
        Credentials.accounts.append(self)

    def delete_account(self):
        Credentials.accounts.remove(self)

    @classmethod
    def display_accounts(cls):
        """
        list of accounts
        """
        for account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_number(cls,number):
        for account in cls.accounts:    
              if account.accountsusername == number:
                  return account