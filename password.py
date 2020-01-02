#import

#dictionaries for storing accounts and passwords
account_dict = {}
special_characters = ['!','@','#','$','%','&','*']
i = 0

def account_create():
    print("-"*18, "\nAccount Creation!"), print("-"*18)
    username = input("Enter a Username:\n")  
    password = ''

    while True:
        if len(password) < 6:
            print("Password has to be 6 characters or more.")
            password = input("Enter a Password:\n")
        else:
            break
        
    print(security_questions())
    security = input("Please choose a security question (Type in corresponding number):\n")



def security_questions():
    sec_questions_dict = {
        "1":"What's your dog's name",
        "2":"What's your cat's name",
        "3":"What's your best friend's middle name",
        "4":"some fourth option"
     }

    for key,val in sec_questions_dict.items():
        print(key,":",val)


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