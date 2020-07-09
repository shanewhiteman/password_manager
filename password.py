# Password Creator/Manager

import json
import os
import random
import re
import sys
from collections import Counter

import get_char

WEB_ACCOUNTS_KEY = "Web Accounts"


class account:
    user_acc = {}
    filename = ""

    def __init__(self, filename):
        self.filename = filename

    # Creates an account
    def create(self):
        print("-"*17, "\nAccount Creation!"), print("-"*17)

        user_info = {}
        while True:
            username = input("Enter a Username:\n")
            if len(username) < 5:
                print("Username has to be 5 characters or more.")
                continue

            user_info["Username"] = username
            break

        user_info["Password"] = self.create_pass()
        user_info = self.get_sec_questions(user_info)
        self.user_acc[username] = user_info
        self.save()

        return

    # Creates password
    def create_pass(self):
        if self.ask_random_pass() == False:
            while True:
                password = input("Enter a Password:\n")

                if not validate_pass(password):
                    continue

                self.pass_rating(password)
                print("Are you sure you want \"" + password +
                      "\" as your password? (Type 'y' or 'n'): ")
                save_answer = input("")
                if save_answer == 'y':
                    print("Password Saved.")
                    return password
                elif 'n':
                    continue
                break

        else:
            password = self.generate_pass()

            return password

    # Asks user to pick a question and saves the answer
    def get_sec_questions(self, user_info):
        sec_questions_dict = {
            "1": "What's your pet's name",
            "2": "What's your mother's middle name",
            "3": "What's your best friend's nickname",
            "4": "Which hospital were you born in"
        }

        print("-"*26)
        for key, val in sec_questions_dict.items():
            print(key, ":", val)
        print("-"*26)

        while True:

            security_choice = input(
                "Please choose a security question (Type in corresponding number):\n")

            if security_choice in sec_questions_dict:
                value = sec_questions_dict[security_choice]
                print(value)
                question_answer = input("")
                user_info["Security Question"] = value
                user_info["Security Answer"] = question_answer
                break

            else:
                print("Incorrect use.")
                print(
                    "*Choose a security question by typing in the number before the question* \n(ex: 1, 2, 3)")
                continue

        return user_info

    # Asks to generate a randomized password
    def ask_random_pass(self):

        while True:
            rand_answer = input(
                "Would you like a randomized password? ('y' or 'n'):\n")
            if rand_answer == 'y':
                return True
            elif rand_answer == 'n':
                return False
            else:
                print("Incorrect use.")

        return False

    # Generates a randomized password
    def generate_pass(self):
        char_source = get_char.ascii_characters_and_num()
        characters_list = char_source.letters + \
            char_source.digits + char_source.special_characters

        # first we guarantee one of each character type
        rand_password = random.choice(char_source.lowercase)
        rand_password += random.choice(char_source.uppercase)
        rand_password += random.choice(char_source.digits)
        rand_password += random.choice(char_source.special_characters)

        # then we fill the rest of the password length with random characters
        # from source
        for _ in range(6):
            rand_password += random.choice(characters_list)

        print("Your random pass is: " + rand_password)
        return rand_password

    # Saves and stores account
    def save(self):
        acc_data = json.dumps(self.user_acc)
        acc_file = open(self.filename, 'w')
        acc_file.write(acc_data)
        acc_file.close()
        return

    # Loads account information
    def load(self):
        acc_file = open(self.filename, 'r')
        acc_data = acc_file.read()
        if len(acc_data) == 0:
            return
        self.user_acc = json.loads(acc_data)
        acc_file.close()
        return

    # Checks if an account exists
    def check(self, user):
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
            elif self.check(user_answer) == False:
                continue
            else:
                self.delete(user_answer)
                break

        return

    # Deletes accounts
    def delete(self, user):
        del self.user_acc[user]
        self.save()
        print("removed account: \"" + user + "\"")

    # Recover exisiting account
    def recover(self):
        attempts = 4
        print("-"*18, "\nPassword Recovery!"), print("-"*18)
        while True:
            user_answer = input("Enter a username: ")

            if self.check(user_answer) == False:
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
                        print("You have " + str(attempts) + " attempt(s) left.")
                        continue
        return

    # Gives the password a rating
    def pass_rating(self, password):
        char_set = Counter()

        for character in password:
            char_set[character] += 1

        for character in sorted(char_set, key=char_set.get, reverse=True):
            if char_set[character] > len(password)//2:
                print("*WARNING* This password is Bad!")
                break
            elif char_set[character] == 1:
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
            if self.check(user_answer) == False:
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
                        print(password)
                        print("Password not found!")
                        print("You have " + str(attempts) + " attempt(s) left.")
                        continue

                return username

    # Checks if entry exists
    def entry_check(self, user, webacc):
        while True:
            try:
                self.user_acc[user][WEB_ACCOUNTS_KEY][webacc]
            except KeyError:
                print("That account doesnt exist!")
                return False
            else:
                return True

    # Deletes entries
    def entry_del(self, user, webacc):
        del self.user_acc[user][WEB_ACCOUNTS_KEY][webacc]
        self.save()
        print("removed entry: \"" + webacc + "\"")

    # Password Manager
    def pass_manager(self):
        user = self.login()

        print("-"*65, "\nUsage: Enter a website then enter a password for the site.")
        print("Type 's' to see your passwords, type 'd' to delete an existing entry"), print(
            "-"*65)

        site = input("Enter your website: ")

        if site == 'd':
            try:
                print(self.user_acc[user][WEB_ACCOUNTS_KEY])
            except KeyError:
                print("No entries created yet!")
                sys.exit(1)
            else:
                while True:
                    print("Type 'e' to exit")
                    get_pass = input(
                        "Enter an entry you would like to delete (type in website name): ")

                    if get_pass == 'e':
                        sys.exit(0)

                    elif self.entry_check(user, get_pass) == False:
                        continue

                    else:
                        self.entry_del(user, get_pass)
                        break

        elif site == 's':
            try:
                print(self.user_acc[user][WEB_ACCOUNTS_KEY])
            except KeyError:
                print("No entries created yet!")
                sys.exit(1)

        else:
            site_pass = self.create_pass()
            try:
                self.user_acc[user][WEB_ACCOUNTS_KEY][site] = site_pass
            except KeyError:
                user_pass = {
                    site: site_pass
                }
                self.user_acc[user][WEB_ACCOUNTS_KEY] = user_pass
                self.save()
            else:
                self.save()


def validate_pass(password):
    # Fail Case 1
    if len(password) < 6:
        print("Password has to be 6 characters or more.")
        return False
    # Fail Case 2
    elif any(character.isdigit() for character in password) == False:
        print("Password has to include at least one digit/number.")
        return False
    # Fail Case 3
    elif bool(re.match("^[a-zA-Z0-9_]*$", password)) == True:
        print("Password has to include at least one special character")
        return False

    return True

# Main Function


def main():
    if not os.path.exists('/tmp/account_file.json'):
        make_file = open('/tmp/account_file.json', 'w')
        make_file.close()

    acc = account('/tmp/account_file.json')
    acc.load()

    print("-"*29, "\nWelcome to Password Manager!"), print("-"*29)
    print("Forgot your password? Type 'r' to get back your information!")
    print("Type 'd' to delete an account")
    answer = input(
        "Do want to create an account? Type 'y', or type 'n' if you want to login: ")

    if answer == 'y':
        acc.create()
    elif answer == 'n':
        acc.pass_manager()
    elif answer == 'r':
        acc.recover()
    elif answer == 'd':
        acc.get_user_acc()
    else:
        print("Incorrect use.")


main()
