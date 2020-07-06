# Password Creator/Manager

import random
import re
import json
import sys
import os
import get_char

class account:
    user_acc = {}
    user_info = {}
    user_pass = {}
    filename = ""

    def __init__(self, filename):
        self.filename = filename

    # Creates an account
    def acc_create(self):
        print("-"*17, "\nAccount Creation!"), print("-"*17)

        while True:
            username = input("Enter a Username:\n")
            if len(username) < 5:
                print("Username has to be 5 characters or more.")
                continue

            self.user_info["Username"] = username
            break

        self.user_acc[username] = self.user_info
        self.user_info["Password"] = self.create_pass()
        self.get_sec_questions()
        self.acc_save()

        return

    # Creates password
    def create_pass(self):
        if self.ask_random_pass() == 'n':
            while True:
                password = input("Enter a Password:\n")
                # Fail Case 1
                if len(password) < 6:
                    print("Password has to be 6 characters or more.")
                    continue
                # Fail Case 2
                elif any(character.isdigit() for character in password) == False:
                    print("Password has to include at least one digit/number.")
                    continue
                # Fail Case 3
                elif bool(re.match("^[a-zA-Z0-9_]*$", password)) == True:
                    print("Password has to include at least one special character")
                    continue

                self.pass_rating(password)
                print("Are you sure you want \"" + password + "\" as your password? (Type 'y' or 'n'): ")
                save_answer = input("")
                if save_answer == 'y':
                    print("Password Saved.")
                    return password
                elif 'n':
                    continue
                break

        else:
            password = self.get_random_pass()

            return password

    # Asks user to pick a question and saves the answer
    def get_sec_questions(self):
        sec_questions_dict = {
        "1":"What's your pet's name",
        "2":"What's your mother's middle name",
        "3":"What's your best friend's nickname",
        "4":"Which hospital were you born in"
        }

        print("-"*26)
        for key,val in sec_questions_dict.items():
            print(key,":",val)
        print("-"*26)
        
        while True:

            security_choice = input("Please choose a security question (Type in corresponding number):\n")

            if security_choice in sec_questions_dict:
                value = sec_questions_dict[security_choice]
                print(value)
                question_answer = input("")
                self.user_info["Security Question"] = value
                self.user_info["Security Answer"] = question_answer
                break

            else:
                print("Incorrect use.")
                print("*Choose a security question by typing in the number before the question* \n(ex: 1, 2, 3)")
                continue

        return

    # Asks to generate a randomized password
    def ask_random_pass(self):

        while True:
            rand_answer = input("Would you like a randomized password? ('y' or 'n'):\n")
            if rand_answer == 'y':
                break
            elif rand_answer == 'n':
                break
            else:
                print("Incorrect use.")

        return rand_answer

    # Gets a generated password
    def get_random_pass(self):
        gen_pass = self.rand_pass()
        print("Your random pass is: " + gen_pass)

        return gen_pass

    # Generates a randomized password
    def rand_pass(self):
        string = get_char.ascii_characters_and_num()
        characters_list = string.letters + string.digits + string.special_characters
        rand_password = random.choice(string.lowercase)
        rand_password += random.choice(string.uppercase)
        rand_password += random.choice(string.digits)
        rand_password += random.choice(string.special_characters)

        for characters in range(6):
            rand_password += random.choice(characters_list)

        return rand_password

    # Saves and stores account
    def acc_save(self):
        acc_data = json.dumps(self.user_acc)
        acc_file = open(self.filename, 'w')
        acc_file.write(acc_data)
        acc_file.close()
        return

    # Loads account information
    def acc_load(self):
        acc_file = open(self.filename, 'r')
        acc_data = acc_file.read()
        if len(acc_data) == 0:
            return
        self.user_acc = json.loads(acc_data)
        acc_file.close()
        return

    # Checks if an account exists
    def acc_check(self, user):
        while True:
            try:
                self.user_acc[user]
            except KeyError:
                print("That account doesnt exist!")
                return False
            else:
                return True

    # Gets the account from the user for deletion
    def get_user_acc(self):

        while True:
            print("Name the account you would like to delete (Type 'e' to exit): ")
            user_answer = input("")
            if user_answer == 'e':
                sys.exit(1)
            elif self.acc_check(user_answer) == False:
                continue
            else:
                self.acc_del(user_answer)
                break

        return

    # Deletes accounts
    def acc_del(self, user):
        del self.user_acc[user]
        self.acc_save()
        print("removed account: \"" + user + "\"")

    # Recover exisiting account
    def acc_recovery(self):
        #acc_data = open(self.filename, 'r')
        #file_data = json.load(acc_data)
        attempts = 4
        print("-"*18, "\nPassword Recovery!"), print("-"*18)
        while True:
            user_answer = input("Enter a username: ")

            if self.acc_check(user_answer) == False:
                continue

            else:
                password = self.user_acc[user_answer]["Password"]
                security_question = self.user_acc[user_answer]["Security Question"]
                security_answer = self.user_acc[user_answer]["Security Answer"]

                print(security_question)
                while True:
                    question_answer = input("")
                    if question_answer == security_answer:
                        print("Your password is: "+password)
                        break
                    elif attempts == 0:
                        print("You have exceeded max attempts.")
                        sys.exit(1)
                    else:
                        attempts -= 1
                        print("You have "+ str(attempts) +" attempt(s) left.")
                        continue
        return

    # Gives the password a rating
    def pass_rating(self, string):
        import collections
        repeat = collections.defaultdict(int)

        for characters in string:
            repeat[characters] += 1

        for characters in sorted(repeat, key=repeat.get, reverse=True):
            if repeat[characters] > len(string)//2:
                print("*WARNING* This password is Bad!")
                break
            elif repeat[characters] == 1:
                print("This password is Safe!")
                break
            else:
                print("This password is Okay.")
                break

    # Login to existing account
    def login(self):

        attempts = 4

        while True:
            print("Enter a username: ")
            user_answer = input("")
            if self.acc_check(user_answer) == False:
                continue
            
            else:
                username = self.user_acc[user_answer]["Username"]
                password = self.user_acc[user_answer]["Password"]
                while True:
                    print("Enter your password: ")
                    get_password = input("")
                    if get_password == password:
                        break
                    elif attempts == 0:
                        print("You have exceeded max password attempts!")
                        sys.exit(1)
                    else:
                        attempts -= 1
                        print("Password not found!")
                        print("You have "+ str(attempts) +" attempt(s) left.")
                        continue

                return username
    
    # Checks if entry exists
    def entry_check(self, user, webinfo, webacc):
        while True:
            try:
                self.user_acc[user][webinfo][webacc]
            except KeyError:
                print("That account doesnt exist!")
                return False
            else:
                return True

    # Deletes entries
    def entry_del(self, user, webinfo, webacc):
        del self.user_acc[user][webinfo][webacc]
        self.acc_save()
        print("removed entry: \"" + webacc + "\"")

    # Password Manager
    def pass_manager(self):
        user = self.login()

        print("-"*65, "\nUsage: Enter a website then enter a password for the site.")
        print("Type 's' to see your passwords, type 'd' to delete an existing entry"), print("-"*65)

        site = input("Enter your website: ")

        if site == 'd':
            try:
                print(self.user_acc[user]["Web Accounts"])
            except KeyError:
                print("No entries created yet!")
                sys.exit(1)
            else:
                while True:
                    print("Type 'e' to exit")
                    get_pass = input("Enter an entry you would like to delete (type in website name): ")

                    if get_pass == 'e':
                        sys.exit(1)

                    elif self.entry_check(user, "Web Accounts", get_pass) == False:
                        continue

                    else:
                        self.entry_del(user, "Web Accounts", get_pass)
                        break

        elif site == 's':
            try:
                print(self.user_acc[user]["Web Accounts"])
            except KeyError:
                print("No entries created yet!")
                sys.exit(1)

        else:
            site_pass = self.create_pass()
            try:
                self.user_acc[user]["Web Accounts"][site] = site_pass
            except KeyError:
                self.user_pass[site] = site_pass
                self.user_acc[user]["Web Accounts"] = self.user_pass
                self.acc_save()
            else:
                self.acc_save()

# Main Function
def main():
    if not os.path.exists('account_file.json'):
        make_file = open('account_file.json', 'w')
        make_file.close()

    acc = account('account_file.json')
    acc.acc_load()

    print("-"*29, "\nWelcome to Password Manager!"), print("-"*29)
    print("Forgot your password? Type 'r' to get back your information!")
    print("Type 'd' to delete an account")
    answer = input("Do want to create an account? Type 'y', or type 'n' if you want to login: ")

    if answer == 'y':
        acc.acc_create()
    elif answer == 'n':
        acc.pass_manager()
    elif answer == 'r':
        acc.acc_recovery()
    elif answer == 'd':
        acc.get_user_acc()
    else:
        print("Incorrect use.")
        
main()
