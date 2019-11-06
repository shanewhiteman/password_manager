#import

#dictionaries for storing accounts,and passwords
account_dict = {}
special_characters = ['!','@','#','$','%','&','*']
i = 0

def account_create():
    print("-"*18, "\nAccount Creation!"), print("-"*18)
    username = input("Enter a Username:\n")
    password = input("Enter a Password:\n")
    if len(password) < 6:
        print("Password has to be 6 characters or more.")
    print(security_questions())
    security = input("Please choose a security question (Type in corresponding number):\n")
    


    #fail parameters
    if len(password) < 6:
        print("Password has to be 6 characters or more.")
    
    #elif password != i:
        #while True:
            #i+1
            #if password == special_characters[i]:
                #break
            #elif password != special_characters[i]:
                #print("Password has to have atleast 1 special character")
                #break
    #elif password < numbers in range(11):
        #print("password has to have a number")
    

def security_questions():
    sec_questions_dict = {
        "1":"What's your dog's name",
        "2":"What's your cat's name",
        "3":"What's your best friend's middle name",
        "4":"some fourth option"
     }
    return

def password_manager():
    print("some third thing")


def main():
    print("Hey welcome to Password Manager!")
    answer = input("Do want to create an account? Type 'yes' or 'no': ")
    accepted_answers = ['yes','no']

    if answer == accepted_answers[0]:
        account_create()
    elif answer == accepted_answers[1]:
        password_manager()
    else:
        print("Incorrect use.")
        
main()