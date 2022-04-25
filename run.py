import string
from random import *
from user import User
from credentials import Credentials

def create_user(firstname, lastname, username, password):
    newUser = User(firstname, lastname, username, password)
    return newUser

def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
    return User.display_users()



def create_account(accountusername, accountname, accountpassword):
    newaccount = Credentials(accountusername, accountname, accountpassword)
    return newaccount

def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account() 
def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.display_accounts()


    
def main():
    while True:
        print("Welcome to password locker, write signin or login to start")
        print("signin or login")
        option = input()
        option = option.lower()
        if option == "signin":
            print("Create Account")
            print("-"*20)
            print("Enter your Firstname: ")
            firstname = input()
            print("Enter your Lastname: ")
            lastname = input()
            print("Set your username: ")
            username = input()
            print("Set your password: ")
            password = input()
            save_user(create_user(firstname,lastname, username, password))
            print("Your account was created successfully. These are your account details:")
            print("-"*30)
            print(f"Name: {firstname} {lastname}\nUsername: {username}\nPassword: {password}")
            print("\nGo to Login to access your account")
            print("\n\n")

        elif option == "login":
            print("Your username: ")
            loginUsername = input()
            print("Your Password: ")
            loginPassword = input()
            if find_user(loginPassword):
                print("\n")
                print("To create multiple accounts type 'account' to view them type 'view")
                print("-"*60)
                print("account or view?")
                choose = input()
                print("\n")
                if choose == "account":
                    print("Add your credentials Account")
                    print("-"*30)
                    accountusername = loginUsername
                    print("Account Name")
                    accountname = input()
                    print("\n")
                    print("To generate automatic password type 'generate' and to create new password type 'new'")
                    decision = input()
                    if decision == "generate":
                        characters = string.ascii_letters + string.digits
                        accountpassword = "".join(choice(characters) for x in range (randint(6,16)))
                        print(f"Password: {accountpassword}")
                    elif decision == "new":
                        print("Enter your password")
                        accountpassword = input()
                    else:
                        print("Please Enter a valid choice")
                        save_account(create_account(accountusername,accountname,accountpassword))
                        print("\n") 
                        print(f"Username: {accountusername}\n Account Name: {accountname}\nPassword: {accountpassword}")

                elif choose == "view":
                    if find_account(accountusername):
                        print("Here are your accounts")
                        print("-"*30)
                        for user in display_accounts():
                            print(f"Account: {user.accountname}\n Password: {user.accountpassword}\n\n")
                    else:
                        print("Invalid credentials!!")

                else:
                    print("PLEASE TRY AGAIN!!")
                    print("\n")
            else:
                print("Incorrect INFO please try again!!")

        else:
            print("Kindly choose a valid option")
            print("\n")

if __name__ == "__main__":
    main()