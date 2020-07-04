# Password Creator/Manager
# Notes: Three Dictionaries!
# (acc1 : {accinfo {site : pass}},
#  acc2 : {accinfo {site : pass}})

import random
import re
import json
import sys
import shane_char

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
        self.create_pass()
        self.get_sec_questions()
        self.acc_save()

        return
    # Creates password
    def create_pass(self):
        if self.gen_random_pass() == 'n':
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

                self.user_info["Password"] = password
                self.pass_rating(password)
                print("Are you sure you want \"" + password + "\" as your password? (Type 'y' or 'n'): ")
                save_answer = input("")
                if save_answer == 'y':
                    print("Password Saved.")
                elif 'n':
                    continue

                break

        return
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
    def gen_random_pass(self):

        while True:
            rand_answer = input("Would you like a randomized password? ('y' or 'n'):\n")
            if rand_answer == 'y':
                gen_pass = self.rand_pass()
                self.user_info["Password"] = gen_pass
                password_info = self.user_info["Password"]
                print("Your random pass is: " + gen_pass)
                break
            elif rand_answer == 'n':
                break
            else:
                print("Incorrect use.")

        return rand_answer
    # Generates a randomized password
    def rand_pass(self):
        string = shane_char.ascii_characters_and_num()
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
    # Gets the account from the user for deletion
    # def get_user_acc(self):
    #     acc_data = open(self.filename, 'r')
    #     file_data = json.load(acc_data)
        
    #     while True:
    #         print("Name the account you would like to delete (Type 'e' to exit): ")
    #         user_answer = input("")
    #         if user_answer == 'e':
    #             sys.exit(1)
    #         try:
    #             file_data[user_answer]["Username"]
    #         except KeyError:
    #             print("That account doesnt exist!")
    #             continue
    #         else:
    #             break

    #         username = file_data[user_answer]["Username"]
    #         if user_answer == username in file_data[user_answer]["Username"]:
    #             self.acc_del(username)

    #     acc_data.close()
    #     return
    # Deletes accounts
    # def acc_del(self, user):
    #     del self.user_acc[user]
    #     self.acc_save()
    #     print("removed account \"" + user + "\"")

    # Recover exisiting account
    def acc_recovery(self):
        acc_data = open(self.filename, 'r')
        file_data = json.load(acc_data)

        attempts = 4

        while True:
            print("-"*18, "\nPassword Recovery!"), print("-"*18)

            while True:
                print("Enter a username: ")
                user_answer = input("")
                try:
                    file_data[user_answer]["Username"]
                except KeyError:
                    print("That account doesnt exist!")
                    continue
                else:
                    break
        
            username = file_data[user_answer]["Username"]
            password = file_data[user_answer]["Password"]
            security_question = file_data[user_answer]["Security Question"]
            security_answer = file_data[user_answer]["Security Answer"]


            if user_answer == username in file_data[user_answer]["Username"]:

                while True:
                    print(security_question)
                    question_answer = input("")
                    if question_answer == security_answer:
                        print("Your password is: "+password)
                        break
                    elif attempts == 0:
                        print("You have exceeded max attempts.")
                        break
                    else:
                        attempts -= 1
                        print("You have "+ str(attempts) +" attempt(s) left.")        
                break

            else:
                print("Username not found!")
                continue

            acc_data.close()

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
        acc_data = open('account_file.json','r')
        file_data = json.load(acc_data)

        attempts = 4

        while True:
            print("Enter your username: ")
            get_username = input("")

            try:
                file_data[get_username] = input("")
            except KeyError:
                print("That account doesnt exist!")
                continue
            else:
                break

            if get_username == username:
                username = file_data[get_username]['Username']
                password = file_data[get_username]['Password']

                while True:
                    print("Enter your password: ")
                    password = input("")
                    if password == password:
                        #password_manager()
                        print("We made it!")
                        break
                    elif attempts == 0:
                        print("You have exceeded max password attempts!")
                        break
                    else:
                        attempts -= 1
                        print("Password not found!")
                        print("You have "+ str(attempts) +" attempt(s) left.")
                        break

            else:
                print("Username not found!")
                continue
    
        return

# Main Function
def main():
    acc = account('account_file.json')
    acc.acc_load()

    print("-"*29, "\nWelcome to Password Manager!"), print("-"*29)
    print("Type 'd' to delete an account")
    print("Forgot your password? Type 'r' to get back your information!")
    answer = input("Do want to create an account? Type 'y', or type 'n' if you want to login: ")

    if answer == 'y':
        acc.acc_create()
    elif answer == 'n':
        acc.login()
    elif answer == 'r':
        acc.acc_recovery()
    #elif answer == 'd':
       #acc.get_user_acc()
    else:
        print("Incorrect use.")
        
main()
