# Password Creator/Manager

import random
import shane_char
import re
import json

class account:
    def __init__(self):
        self.acc_info = {}
        self.acc = {}

# Creates an account
def account_create():
    acc_data = account()

    print("-"*17, "\nAccount Creation!"), print("-"*17)

    while True:
        username = input("Enter a Username:\n")
        if len(username) < 5:
            print("Username has to be 5 characters or more.")
            continue

        acc_data.acc_info["Username"] = username
        break

    create_password(acc_data.acc_info)
    
    acc_data.acc[username] = acc_data.acc_info

    get_security_questions(acc_data.acc_info)

    account_save(acc_data.acc_info)

    return

# Creates password
def create_password(acc_info):

    if generate_random_password(acc_info) == 'no':
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
       
            acc_info["Password"] = password
            password_info = password
            password_rating(password)
            print("Would you like to save your password? (Type 'yes' or 'no'): ")
            save_query = input("")
            if save_query == 'yes':
                password_save(password_info)
                print("Password Saved.")
            elif 'no':
                continue
            
            break
        return

# Asks user to pick a question and saves the answer
def get_security_questions(acc_info):
    
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
            acc_info["Security Question"] = value
            acc_info["Security Answer"] = question_answer
            break

        else:
            print("Incorrect use.")
            print("*Choose a security question by typing in the number before the question* \n(ex: 1, 2, 3)")
            continue

    return

# Asks to generate a randomized password
def generate_random_password(acc_info):

    while True:
        rand_answer = input("Do you want a randomized password? ('yes' or 'no'):\n")
        if rand_answer == 'yes':
            gen_pass = random_pass()
            acc_info["Password"] = gen_pass
            password_info = acc_info["Password"]
            print("Your random pass is: " + gen_pass)
            password_save(password_info)

            break
        elif rand_answer == 'no':
            break
        else:
            print("Incorrect use.")

    return rand_answer

# Generates a randomized password using letters and digits
def random_pass():
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
def account_save(acc_data):
    
    json_file = open('account_file_test.json', 'w')
    json.dump(acc_data, json_file)

    return

# Recover exisiting account
def account_recovery():
    acc_data = open('account_file_test.json', 'r')
    file_data = json.load(acc_data)

    username = file_data["Username"]
    password = file_data["Password"]
    security_question = file_data["Security Question"]
    security_answer = file_data["Security Answer"]

    attempts = 4

    while True:
        print("-"*18, "\nPassword Recovery!"), print("-"*18)
        print("Enter a username: ")
        user_answer = input("")

        if user_answer == username in file_data["Username"]:
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

    return

# Login to existing account
def login():
    account_dict_file = open('account_file_test.json','r')
    file_data = json.load(account_dict_file)
        
    username = file_data['Username']
    password = file_data['Password']

    attempts = 4

    while True:
        print("Enter your username: ")
        user_input_username = input("")

        if user_input_username == username:
            while True:
                print("Enter your password: ")
                user_input_password = input("")
                if user_input_password == password:
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
    
# Manages and Rates your passwords.
# def password_manager():




# Saves and stores your passwords
def password_save(password_info):
    
    json_file = open('password_file_test.json', 'w')
    json.dump(password_info, json_file)

    return


# Gives the password a rating
def password_rating(string):
    import collections
    repeat_dict = collections.defaultdict(int)

    for characters in string:
        repeat_dict[characters] += 1

    for characters in sorted(repeat_dict, key=repeat_dict.get, reverse=True):
        if repeat_dict[characters] > len(string)//2:
            print("*WARNING* This password is Bad!")
            break
        elif repeat_dict[characters] == 1:
            print("This password is Safe!")
            break
        else:
            print("This password is Okay.")
            break

# Main Function
def main():

    print("-"*29, "\nWelcome to Password Manager!"), print("-"*29)
    print("Forgot your password? Type 'r' to get back your information!")
    answer = input("Do want to create an account? Type 'y', or type 'n' if you want to login: ")

    if answer == 'y':
        account_create()
    elif answer == 'n':
        login()
    elif answer == 'r':
        account_recovery()
    else:
        print("Incorrect use.")
        
main()
