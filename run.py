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
        if option == "signin":
            print("Create Account")
            print("-"*10)
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
            print("-"*10)
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