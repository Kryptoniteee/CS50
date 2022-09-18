# WEEK 2

origTxt = input ("Input: ")

# for every character (i) in origTxt
for i in origTxt:

    # check to see if i matches with any char in the list
    if i in ['a', 'e', 'i', 'o', 'u']:

        # if matches, replace the character in origTxt with nothing
        origTxt = origTxt.replace(i, "")
print("Output:", origTxt)
