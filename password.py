#import

#dictionaries for storing accounts and passwords
#special_characters = ['!','@','#','$','%','&','*']
#i = 0

#Creates account, Password, and Security Question and stores them.
def account_create():
    #Have a username and password -> security queston and answer
    #account_dict = {}

    print("-"*18, "\nAccount Creation!"), print("-"*18)

    while True:
        username = input("Enter a Username:\n")
        if len(username) < 5:
            print("Username has to be 5 characters or more.")
            continue
        else:
            break

    while True:
        password = input("Enter a Password:\n")
        if len(password) < 6:
            print("Password has to be 6 characters or more.")
        else:
            break

    security_questions()
    
    password_randomizer()
    
    return

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


def password_randomizer():
    rand_answer = input("Do you want a randomized password? ('yes' or 'no'):\n")
    accepted_answers = ['yes','no']

    print("I work cause I want to!")

def password_manager():
    print("Ask if user would like to create a password or have one generated")


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