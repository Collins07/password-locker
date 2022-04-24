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
    
