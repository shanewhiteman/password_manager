import random
import shane_char

#Have a (username : password)
account_dict = {}
#Have a (username : security question answer)
forget_pass_dict = {}

# Creates account, Password, and Security Question and stores them.
def account_create():

    print("-"*18, "\nAccount Creation!"), print("-"*18)

    while True:
        username = input("Enter a Username:\n")
        if len(username) < 5:
            print("Username has to be 5 characters or more.")
            continue
        else:
            break


    if password_randomizer_query() == 'no':
        while True:
            password = input("Enter a Password:\n")
            if len(password) < 6:
                print("Password has to be 6 characters or more.")
                continue
            else:
                break
    
    account_dict[username] = password

    security_questions()

    #account_save()

    #forget_pass_save()


    account_save()

    return 

# Asks user to pick a question and saves the answer
def security_questions():
     sec_questions_dict = {
         "1":"What's your dog's name",
         "2":"What's your cat's name",
         "3":"What's your best friend's middle name",
         "4":"some fourth option"
      }

     print("-"*26)
     for key,val in sec_questions_dict.items():
         print(key,":",val)
     print("-"*26)
     #take in a key -> print out the value -> ask for input
     security_choice = input("Please choose a security question (Type in corresponding number):\n")

     value = sec_questions_dict[security_choice]
     print(value)
     question_answer = input("")

     return question_answer

# Asks to generate a randomized password
def password_randomizer_query():
    accepted_answers = 'yes','no'

    while True:
        rand_answer = input("Do you want a randomized password? ('yes' or 'no'):\n")
        if rand_answer == 'yes':
            gen_pass = random_pass()
            print("Your random pass is: " + gen_pass)
            break
        elif rand_answer == 'no':
            break
        elif rand_answer != accepted_answers:
            print("Incorrect use.")



    return rand_answer

# Generates a randomized password using letters and digits
def random_pass():
    string = shane_char.ascii_characters_and_num()
    letters_and_num = string.letters + string.digits
    rand_password = random.choice(string.lowercase)
    rand_password += random.choice(string.uppercase)
    rand_password += random.choice(string.digits)

    for characters in range(6):
        rand_password += random.choice(letters_and_num)

    password_list = list(rand_password)
    random.SystemRandom().shuffle(password_list)
    rand_password = ''.join(password_list)

    return rand_password

# Saves and stores account
def account_save():


    # account_file = open('account.txt','w')
    # account_file.write(str(account_dict))
    # account_file.close()

    return account_dict

def forget_pass_save():

    # forg_pass_user = account_create()
    # forg_pass_answer = security_questions()

    # forget_pass_file = open('forgottenpass.txt','w')
    # forget_pass_file.write(str(forget_pass_dict))
    # forget_pass_file.close()

    return forget_pass_dict

#def forgot_pass():


# Manages and Rates your passwords.
def password_manager():
    print("I don't do anything yet!")


def main():
    print("Hey welcome to Password Manager!")
    answer = input("Do want to create an account? Type 'yes' or 'no': ")
    accepted_answers = 'yes','no'

    if answer == 'yes':
        account_create()
    elif answer == 'no':
        password_manager()
    else:
        print("Incorrect use.")
        
main()