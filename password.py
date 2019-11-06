#import

account_dict = {}
sec_questions_dict = {}

def account_create():
    print("account created")


def security_questions():
    print("security questioned")


def main():
    print("Hey welcome to password manager!")
    answer = input("Do you have an account? Type 'yes' or 'no': ")
    accepted_answers = ['yes','no']

    if answer == accepted_answers[0]:
        print("goodjob: yes")
    elif answer == accepted_answers[1]:
        print("goodjob: no")
    else:
        print("Incorrect use.")
main()