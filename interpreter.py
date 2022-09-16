# receive user input and split by whitespace into x, y, z respectively
x, y, z = input("Expression: ").split(" ")

# convert x and z to integer
x = int(x)
z = int(z)

# use cases
match y:
    case "+":
        print("{:.1f}".format(x+z))
    case "-":
        print("{:.1f}".format(x-z))
    case "*":
        print("{:.1f}".format(x*z))
    case "/":
        print("{:.1f}".format(x/z))