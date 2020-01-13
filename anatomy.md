---------------------------
# Account Creation Skeleton
---------------------------

<strike>Create an account, Store it</strike>
<strike>Make a password, Store it to the account</strike>
<strike>Create a list of general questions</strike>
<strike>Save question and answer<strike>
<strike>Save Account.<strike>

------------------
# Account Recovery
------------------
Create a "Forgot Pass" function:

<strike>Ask user for username<strike>

Return to user security question under the account

Ask for user to answer (expecting answer saved to the account)

If answer is correct, return user password.

(Optional) Ask if user wants to create/generate a new password

If answer is incorrect give user 4 more tries(5 tries total), kill function.

---------------------------
# Password Managing Skeleton
---------------------------
<strike>1. Ask if user would like to create a password or have one generated</strike>

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