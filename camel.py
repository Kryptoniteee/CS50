# WEEK 2

# receive user input
camelInput = input("camelCase: ")

# initialize underscore
underscore = "_"

# loop through user input string and find upper case
for i in camelInput:
    if i.isupper():
        # convert detected uppercase character to lower
        snakeCase = i.lower()
        # add the underscore behind the lower'ed character
        snakeCase = underscore + snakeCase
        # replace i in user input with the new underscore + lower'ed character
        camelInput = camelInput.replace(i, snakeCase)

# print outside for loop
print("snake_case: " + camelInput)