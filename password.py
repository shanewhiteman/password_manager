# Password Creator/Manager

import random
import shane_char 
import re
import json

class dictionary_class:
    def __init__(self):
        self.account_dict = {}
        self.account_info_dict = {}


# Creates an account
def account_create():
    dict_data = dictionary_class()

    print("-"*18, "\nAccount Creation!"), print("-"*18)

    while True:
        username = input("Enter a Username:\n")
        if len(username) < 5:
            print("Username has to be 5 characters or more.")
            continue
        else:
            dict_data.account_info_dict["Username"] = username
            break

    create_password()
    
    dict_data.account_dict[username] = dict_data.account_info_dict

    get_security_questions()

    account_save()

    return

# Creates password
def create_password():
    dict_data = dictionary_class()

    if generate_random_password() == 'no':
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
            else:
                dict_data.account_info_dict["Password"] = password
                password_rating(password)
                print("Would you like to save your password? (Type 'yes' or 'no'): ")
                save_query = input("")
                if save_query == 'yes':
                    password_save()
                    print("Password Saved.")
                    break
                elif 'no':
                    continue
                else:
                    break
    else:
        while True:
            print("Would you like to save your password?(Type 'yes' or 'no'): ")
            save_query = input("")
            if save_query == 'yes':
                password_save()
                print("Password Saved.")
                break
            elif 'no':
                create_password()
                continue
            else:
                break
   
    return


# Asks user to pick a question and saves the answer
def get_security_questions():
    dict_data = dictionary_class()
    
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
        dict_data = dictionary_class()
        security_choice = input("Please choose a security question (Type in corresponding number):\n")

        if security_choice in sec_questions_dict:
            value = sec_questions_dict[security_choice]
            print(value)
            question_answer = input("")
            dict_data.account_info_dict["Security Question"] = value
            dict_data.account_info_dict["Security Answer"] = question_answer
            break

        else:
            print("Incorrect use.")
            print("*Choose a security question by typing in the number before the question* \n(ex: 1, 2, 3)")
            continue

    return value, question_answer

# Asks to generate a randomized password
def generate_random_password():
    dict_data = dictionary_class()

    while True:
        rand_answer = input("Do you want a randomized password? ('yes' or 'no'):\n")
        if rand_answer == 'yes':
            gen_pass = random_pass()
            dict_data.account_info_dict["Password"] = gen_pass
            print("Your random pass is: " + gen_pass)
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
def account_save():
    dict_data = dictionary_class()

    # account_file = open('account.txt','a')
    # account_file.write(dict_data.account_dict)
    # account_file.write("\n")
    # account_file.close()
    json_file = open('account_file.json', 'a')
    json.dump(dict_data.account_dict, json_file)

    return

# Recover exisiting account
def account_recovery():
    account_dict_file = open('account_file.json')
    file_data = json.load(account_dict_file)

    #for acc in file_data:
        # name =
        # password =
        # security_question =
        # secuirty_answer = 


    # for line in account_dict_file:
        
    #     word = re.split('\{|: |, |\}', line)
    #     name = word[1]
    #     username = name.replace("'","")
    #     pass_w = word[6]
    #     password = pass_w.replace("'","")
    #     sec_ques = word[8]
    #     security_question = sec_ques.replace('"',"")
    #     sec_answ = word[10]
    #     security_answer = sec_answ.replace("'","")
    
    attempts = 4

    while True:
        print("Enter a username: ")
        user_answer = input("")

        if user_answer == username:
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

    account_dict_file.close()

    return

# Login to existing account
def login():
    account_dict_file = open('account.txt','r')

    attempts = 4
    for line in account_dict_file:
        word = re.split('\{|: |, |\}', line)
        name = word[1]
        username = name.replace("'","")
        pass_w = word[6]
        password = pass_w.replace("'","")

    while True:
        print("Enter your username: ")
        user_input_username = input("")

        if user_input_username == username:
            while True:
                print("Enter your password: ")
                user_input_password = input("")
                if user_input_password == password:
                    #password_manager()
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

    account_dict_file.close()
    
    return
    
# Manages and Rates your passwords.
# def password_manager():




# Saves and stores your passwords
def password_save():
    dict_data = dictionary_class()

    # account_file = open('password.txt','a')
    # account_file.write(dict_data.account_info_dict)
    # account_file.write("\n")
    # account_file.close()
    json_file = open('password_file.json', 'a')
    json.dump(dict_data.account_dict, json_file)


    return dict_data.account_info_dict

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

# Lists the password
def list_password():
    account_file = open('password.txt','r')
    print(str(account_file.read()))
    account_file.close()

# Main Function
def main():

    print("-"*29, "\nWelcome to Password Manager!"), print("-"*29)
    print('*IMPORTANT* Type "recovery" to recover your account password if forgotten!')
    answer = input("Do want to create an account? Type 'yes' or 'no': ")

    if answer == 'yes':
        account_create()
    elif answer == 'no':
        login()
    elif answer == 'recovery':
        account_recovery()
    else:
        print("Incorrect use.")
        
main()


#process to save data
#dictionary{"firstname": "clint", "lastname": "edwards"}(binary/object) -> function -> (string) {"firstname" = "clint", "lastname": = "edwards"} -> file -> {"firstname" = "clint", "lastname": = "edwards"}

#process to load data
#file -> {"firstname" = "clint", "lastname": = "edwards"} -> readfile -> function(decode) -> dictionary{"firstname": "clint", "lastname": "edwards"}(binary/object)

#each function for each check
