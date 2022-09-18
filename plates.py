# WEEK 2

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # condition 1: max 6 char, min 2 char
    # checking for more than 6 char, less than 2 char
    if len(s) > 6 or len(s) < 2:
        return False

    # condition 2: start with at least 2 letters
    # checking for non alphabets for first 2 letters
    if s[0:2].isalpha() == False:
        return False

    # condition 3: no periods, spaces or punctuation marks
    # checking for periods, spaces, punctuation marks
    for i in s:
        if i in ['.', ' ', ',']:
            return False

    # condition 4: numbers cannot be used in the middle of the plate, must be the end
    # looping and identifying one number and making sure the next element is also a number

    # looping through s with x as element
    # initializing z as a counter
    z = 0
    for x in s:
        if x.isnumeric() == True: # checking if x is a number
            z += 1 # if x is a number, increase counter z and continue next loop
            continue

        # if z is not equals to 0, it means that there is already a previous numeric element
        # if current element is not a number and previous element is a number -> xxx5x
        # this would mean that the numbers are in the middle of the plate
        if z != 0 and x.isnumeric() == False:
            return False


    # condition 5: first number cannot be 0
    # checking if first numeric element identified in loop is 0

    # looping s with element y
    for y in s:
        if y.isnumeric() == True: # checking first instance of numeric element identified
            if y == "0": # if first numeric element is 0, return false
                return False
            # if first numeric element is not 0, it breaks out of loop as it fulfills condition
            # of first number not being 0
            else:
                break

    return True

main()