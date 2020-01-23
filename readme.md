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

---------------------
# Password Randomizer
---------------------
1. Ask if user would like a Randomly generated password
2. Create a string of randomly generated characters
3. Show string of randomly generated characters to user
4. Ask if user would like to save
- if user would not like to save kill program (for now)
5. Save to dictionary/list

------------------
# Account Recovery
------------------
1. Create a "Forgot Pass" function
2. Ask user for username
3. Return to user security question under the account
4. Ask for user to answer (expecting answer saved to the account)
5. If answer is correct, return user password.
6. (Optional) Ask if user wants to create/generate a new password
7. If answer is incorrect give user 4 more tries(5 tries total), kill function.

----------------------
# Beginning of Manager
----------------------
1. Ask if user would like to create a password or have one generated

-------------------
# Password Managing
-------------------
1. Ask user to create a password of at least 6 characters || Ask user to use atleast 1 special character and 1 number (optional)
2. Rate the password by the following:

the password is bad if:
- the same character, special character, or int is used more than half of the total number of characters created

the password is safe if:
- no characters, special characters, or ints are repeated

the password is okay if:
- It's passes the bad parameter but doesn't pass the safe parameter

3. Ask if user would like to save
- if user would not like to save ask if user wants to make a new one or exit function.

4. Saves password.
