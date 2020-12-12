# importing os for clearing the console screen
import os


# creating the pswd class
class pswd():
    # defining the constructor for initialising the class for retriving the prevoiusly
    # stored passwords and user names
    def __init__(self):
        self.user_name = self.get_user()
        self.user_pwd = self.get_pwd()

    # it creates a text file and stores the user password in it FILENAME: pwd.txt
    # the files is handled by using with statement so no need to close the files
    def save_pwd(self):
        with open("pwd.txt", 'w') as pwdfile:
            pwdfile.write(self.user_pwd)

    # it creates a text file and stores the username in this file FILENAME: user.txt
    def save_user(self):
        with open("user.txt", 'w') as userfile:
            userfile.write(self.user_name)
        # it reads the currently existing files and returns the username

    def get_user(self):
        with open('user.txt', 'r') as userfile:
            return userfile.read()

    # it reads the currently exiting password file and returns the password
    def get_pwd(self):
        with open('pwd.txt', 'r') as pwdfile:
            return pwdfile.read()

    # this method prompts to input the previous password and if the password matches
    # with the old password then it asks to enter new password twice and updates
    # value inside the pew.txt file
    def change_pwd(self):
        # finite loop executes until the password is updated successfully
        # or it prompts for reentering the passsword if the entered password does not \
        # with the old password
        while True:
            tmp_userpwd = input('Enter current password:')
            self.user_pwd = self.get_pwd()
            if tmp_userpwd == self.user_pwd:
                new_pass = input("Enter new password: ")
                new_pass2 = input('Confirm password: ')
                if new_pass == new_pass2:
                    self.user_pwd = new_pass
                    self.save_pwd()
                    print("Password Changed Successfully\n")
                    break
                else:
                    print("New password does not match.\n")
                    print("Re-Enter the new password Again...\n")
            else:
                print("Wrong password, Enter Again...\n")

    # this method modifies the username and save the changes into the user.txt file
    def change_user(self):
        while True:
            tmp_username = input('Enter the current username: ')
            self.user_name = self.get_user()
            if tmp_username == self.user_name:
                tmp_username1 = input('Enter the new user name: ')
                if tmp_username1 == self.user_name:
                    print('The user already exists\n')
                else:
                    self.user_name = tmp_username1
                    self.save_user()
                    print("Username changed successfully.\n")
                    break
            else:
                print('Username doesnt exists \n')

    # this method checks if the eneterred password is correct or not
    # if not then it returns a false value else if it matches it returnns true value
    # if the password is correct call the main method of any program that you want to
    # run if  the user inputs a correct password
    def checkpass(self):
        if self.user_name == self.input_user:
            self.usr_flag = True
        else:
            self.usr_flag = False
            print("invalid Username..!\n")
        if self.user_pwd == self.input_pwd:
            self.pwd_flag = True
        else:
            self.pwd_flag = False
            print('Wrong Password...!\n')
        if self.usr_flag and self.pwd_flag:
            print('Login Successfull')
            return True
        else:
            return False

    # this method takes the password and username form the user and stores them into
    # class variables
    def input_credentials(self):
        self.input_user = input('Enter the username: ')
        self.input_pwd = input('Enter the password: ')


# this is the main driver program tha creates the objects of the class
# and perform all the actions
def main():
    obj = pswd()
    while True:
        os.system('cls')
        print("\n\t1.Login\n\t2.Change Credentials\n\t3.Exit\n")
        choice = int(input('Enter your choice: '))
        if choice == 1:
            obj.input_credentials()
            obj.checkpass()
        elif choice == 2:
            ch = int(
                input('\nChoose of option to change:\n\t1. Change Username\n\t2. Change Password\nEnter Your choice: '))
            if ch == 1:
                obj.change_user()
            elif ch == 2:
                obj.change_pwd()
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
