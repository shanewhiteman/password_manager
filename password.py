import random
import shane_char

#dictionaries for storing accounts and passwords
# Creates account, Password, and Security Question and stores them.
def account_create():
    #Have a username and password -> security answer
    #account_dict = {}

    print("-"*18, "\nAccount Creation!"), print("-"*18)

    while True:
        username = input("Enter a Username:\n")
        if len(username) < 5:
            print("Username has to be 5 characters or more.")
            continue
        else:
            break
    
    while password_randomizer_query() == 'no':
        password = input("Enter a Password:\n")
        if len(password) < 6:
            print("Password has to be 6 characters or more.")
            continue
        else:
            break

    security_questions()

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
            print("Your random pass is: " + random_pass())
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
    password = random.choice(string.lowercase)
    password += random.choice(string.uppercase)
    password += random.choice(string.digits)

    for characters in range(6):
        password += random.choice(letters_and_num)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password


# Manages and Rates your passwords.
def password_manager():
    print("I don't do anything yet!")


def main():
    print("Hey welcome to Password Manager!")
    answer = input("Do want to create an account? Type 'yes' or 'no': ")
    accepted_answers = ['yes','no']

    if answer == 'yes':
        account_create()
    elif answer == 'no':
        password_manager()
    else:
        print("Incorrect use.")
        
main()