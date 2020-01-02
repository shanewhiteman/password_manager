#import

#dictionaries for storing accounts and passwords
account_dict = {}
special_characters = ['!','@','#','$','%','&','*']
i = 0

#Creates account, Password, and Security Question and stores them.
def account_create():
    sec_questions_dict = {
        "1":"What's your dog's name",
        "2":"What's your cat's name",
        "3":"What's your best friend's middle name",
        "4":"some fourth option"
     }

    print("-"*18, "\nAccount Creation!"), print("-"*18)
    username = input("Enter a Username:\n")  
    password = ''

    while True:
        if len(password) < 6:
            print("Password has to be 6 characters or more.")
            password = input("Enter a Password:\n")
        else:
            break
        
    for key,val in sec_questions_dict.items():
        print(key,":",val)

    #take in a key -> print out the value -> ask for input
    security_choice = input("Please choose a security question (Type in corresponding number):\n")
    
    for security_choice in sec_questions_dict:
        value = sec_questions_dict[security_choice]
        print(value)
        break
    save_answer = input("")
    return

def password_manager():
    print("some third thing")


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