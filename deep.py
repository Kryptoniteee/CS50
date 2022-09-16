#receive user input with long question
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#transform input to lower case for easier case insensitivity
x = x.lower()

#remove all whitespace in input for easier space insensitivity
x = x.replace(" ","")

#checking if user input has 42 or fortytwo(case and space insensitive) or forty-two
if (x == "42" or x == "fortytwo" or x == "forty-two"):
    print("Yes")
else:
    print("No")