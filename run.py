#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

def create_user(first_name, last_name, created_user_name, created_user_password, confirm_password):
    """
    Function to create a new user
    """
    new_user = User(first_name,last_name,created_user_name,created_user_password,confirm_password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def create_credential(account,userName,password):
    """
    Function to create new user credentials
    """
    new_credential = Credential(account,userName,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()

def display_credentials():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def find_credentials(account):
    '''
    Function that finds credentials by account name
    '''

    return Credentials.find_by_name(account)

def existing_credentials(account):
    '''
    Functiion that checks if an account really exists
    '''
    return Credentials.credentials_exists(account)

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def main():

   while True: 
        print("Welcome to Password Locker!!!")
        print('\n')
        print("Do you have an account with Password Locker? y/n")
        print("Use a short code: ex - to logout")
        option = input().lower()

        if option == "n":
            print("Signup to account")
            print('Enter first name')
            first_name = input()
            print('Enter last name')
            last_name = input()
            print('Create username')
            created_user_name = input()
            print('Create password')
            created_user_password = input()
            print('Confirm password')
            confirm_password = input()
            
            save_user( first_name,last_name,created_user_name,created_user_password,confirm_password)
            print('-' * 10)
            
            print(f"Congratulations, {last_name} your have successfully created an account \n Your Username is: {created_user_name} \n Your Password is: {confirm_password}")

            while True:
                    print("Select a short code to navigate through:1 - login to an account :2 - logout an account")
                    short_code = input().lower()
                    print('\n')
                    
                    if short_code == '2':
                        print(" Your have succefully logout from your account") 
                        break
                
                    elif short_code == '2':
                        print("*** Login ***")
                        print('\n')
                        print("Enter account name")
                        account = input()
                        print("Enter username")
                        user_name = input()

                        while True:
                            print("Select a short code to navigate through: 1 - to input your password :2 - to generate your password")
                            short_code = input().lower()
                            print('\n')

                            if short_code == '1':
                                print("Enter password")
                                password = input()
                                break
            
                            
                            elif short_code == '2':
                                print(password)
                                break

                    while True:
                        print("Use these short codes : 1 - create new credentials, 2 - display credentials, 3 - delete credentials, 4-find credentials, 5 - logout the account") 
                        short_code = input().lower()
                    
                        if short_code == '1':
                                print("Enter account name")
                                account = input()
                                print("Enter username")
                                user_name = input()
                              
                                while True:
                                    print("Select short code: 1 - to input your password :2 - generate password")
                                    short_code = input().lower()
                                    print('\n')
                                    
                                    if short_code == '1':
                                        print("Enter password")
                                        password = input()
                                        break
                                    
                                    elif short_code == '2':
                                        password = random_password(8)
                                        print(password)
                                        break
                                    
                                save_credential(add_credentials(account, user_name,password))
                                print('-' * 10)
                                print(f"Your new credentials: \n Username: {user_name}  \n Account Name: {account}")
                                print('\n')
                        
                        elif short_code == '2':
                                if display_credentials():
                                    print("Your credentials")
                                    print('\n')
                                    
                                    print('-' * 10)
                                    for credential in display_credentials():
                                         print(f" Account Name: {credential.account}  \n Username: {credential.user_name} \n Password: {credential.password}")
                                 
                                    print('\n')
                                else:
                                    print('\n')
                                    print(f"No credentials")
                                    print('\n')
                                    
                        elif short_code == '3':
                                print("Enter name of the account you want to delete its credentials")

                                default_accname = input()
                                if existing_credentials(account):
                                    print('\n')
                                    search_account = find_credentials(account)
                                    delete_credentials(search_account)
                                    
                                    print('-' * 10)
                                    print(f" {account} has been deleted")
                                    print('\n')
                                else:
                                    print("The {account} account doesn't exist")   
                                    print('\n')
                        elif short_code == '4':
                                print("Enter the account name you want to search for")
                                
                                    
                                print('-' * 10)
                                account = input()
                                if existing_credentials(account):
                                    print('\n')
                                    search_account = find_credentials(account)
                                    print(f"{user_name} your account credentials is as follows:")
                                    
                                    print(f"Account Name: {account}")
                                    print(f"Your Password: {password}")
                                    
                                else:
                                    print("Account doesn't exist")
                                    print('\n')
                                    
                        elif  short_code == '5':            
                                    print(" loged out") 
                                    break  
                        else:
                            print("invalid code.")
                                                     
        elif option == "y":    
               print("Login account")
               print("Select short code :1 - login to an account :2 - logout an account")
               short_code = input().lower()
               
               if short_code == '2':
                    print("loged out") 
                    break
               
               elif short_code == '1':
                    print("Login ")
                    print("Enter account name")
                    account = input()
                    print("Enter username")
                    user_name = input()
                  
                    while True:
                            print("Select short code : 1- to input your password :2 -  generate password")
                            short_code = input().lower()
                            print('\n')
                            
                            if short_code == '1':
                                print("Enter password")
                                password = input()
                                break
                            
                            elif short_code == '2':
                                password = random_password(8)
                                print(password)
                                break
                            
                    save_credential(add_credentials(account, user_name, password))
                    print('-' * 10)
                    
                    print(f"Welcome {user_name} to your account \n Account Name: {account}")
                    print('\n')    
                        
                    while True:
                        print("Use short codes : 1 - create new credentials, 2 - display credentials, 3 - delete credentials, 4 -find credentials,5 - logout the account") 
                        short_code = input().lower()
                    
                        if short_code == '1':
                                print("Enter account name")
                                account = input()
                                print("Enter username")
                                user_name = input()
                                
                                while True:
                                    print("Select short code: 1 - to input your password :2 -generate password")
                                    short_code = input().lower()
                                    print('\n')
                                    
                                    if short_code == '1':
                                        print("Enter password")
                                        password = input()
                                        break
                                    
                                    elif short_code == '2':
                                        password = random_password(8)
                                        print(password)
                                        break
                                    
                                save_credential(add_credentials(account, user_name,password))
                                print('-' * 10)
                                print(f"Your new credentials: \n Username: {user_name}  \n Account Name: {account} \n Password: {password}")
                                print('\n')
                        
                        elif short_code == '2':
                                if display_credentials():
                                    print("Your credentials")
                                    print('\n')
                                    
                                    print('-' * 10)
                                    for credential in display_credentials():
                                         print(f" Account Name: {credential.account}  \n Username: {credential.user_name} \n Password: {credential.password}")
                                 
                                    print('\n')
                                else:
                                    print('\n')
                                    print(f"No credentials saved yet")
                                    print('\n')
                                    
                        elif short_code == '3':
                                print("Enter name of the account you want to delete its credentials")

                                default_accname = input()
                                if existing_credentials(account):
                                    print('\n')
                                    search_account = find_credentials(account)
                                    delete_credentials(search_account)
                                    print('-' * 10)
                                    print(f"Your Password Locker has deleted {account}")
                                    print('\n')
                                else:
                                    print("{account} account credentials doesn't exist")   
                                    print('\n')
                        elif short_code == '4':
                                print("Enter the account name you want to search for")
                                
                                account = input()
                                if existing_credentials(account):
                                    print('\n')
                                    print('-' * 10)
                                    search_account = find_credentials(account)
                                    print(f"Hello, {user_name} your account credentials is as follows:")
                                    
                                    print(f"Account Name: {account}")
                                    print(f"Your Password: {password}")
                                    
                                else:
                                    print("account credentials doesn't exist")
                                    print('\n')
                                    
                        elif  short_code == '5':            
                                    print("Your have succefully logout your account") 
                                    break  
                        else:
                            print("Sorry, invalid code.")
        
        elif option == 'ex':
            print("karibu")
            break
        else:
            print("Please try again with valid option")  

if __name__ == '__main__':
    main()        