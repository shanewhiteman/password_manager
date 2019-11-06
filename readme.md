
Create a password manager that manages your passwords
and gives you feedback on the password you just gave.

------------------
# Account Creation
------------------
1. Ask if user has an "account"
2. Ask user for Username
3. Ask user for Password of atleast 6 characters || Ask user to use atleast 1 special character and 1 number (optional)
4. Ask user to choose from a list of pre-created general "Security Questions" || Ask user to answer
5. Save user's inputs in a list/dictionary

----------------------
# Beginning of Manager
----------------------
1. Ask if user would like to create a password or have one generated

---------------------------
# Password Managing Attempt
---------------------------
1. Ask user to create a password of at least 6 characters || Ask user to use atleast 1 special character and 1 number (optional)
2. Rate the password by the following:

the password is bad if:
- the same character, special character, or int is used more than half of the total number of characters created

the password is okay if:
- the same character, special character, or int is used less than or equal to half of the total number of characters created

the password is safe if:
- no characters, special characters, or ints are repeated

3. Ask if user would like to save if "Okay" rating given
- if user would not like to save kill program (for now)
4. Save to dictionary/list
-----------------------------
# Password Randomizer Attempt
-----------------------------
1. Ask if user would like a Randomly generated password
2. Create a string of randomly generated characters
3. Show string of randomly generated characters to user
4. Ask if user would like to save
- if user would not like to save kill program (for now)
5. Save to dictionary/list
