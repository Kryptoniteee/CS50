# receive user input
greeting = input("Greeting: ")

# space and case insensitivity
greeting = greeting.replace(" ", "")
greeting = greeting.lower()

# comparison made with startswith() function
# https://pytutorial.com/check-if-not-startswith-python
if greeting.startswith("hello") is True:
    print ("$0")
elif (greeting.startswith("h") is True) and (greeting.startswith("hello") is False):
    print ("$20")
else:
    print ("$100")