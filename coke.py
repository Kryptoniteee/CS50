# WEEK 2

# initialize amount due = 50
initialAmountDue = 50

# keep in loop if Amount Due has not been depleted to 0
while initialAmountDue > 0:

    # print Amount Due and ask for coin insert if amount due is not 0
    print("Amount Due: ", initialAmountDue)
    coinInsert = int(input ("Incert Coin: "))

    # if condition to accept only these coins
    if coinInsert == 25 or coinInsert == 10 or coinInsert == 5:
        initialAmountDue = initialAmountDue - coinInsert # subtract coin insert from amount due

# once amount due = 0, the loop will break and come here. Amount due can be any value except for > 0
# if amount due is negative, abs will convert it to positive number
# if amount due is 0, abs will have no effect
changeOwed = abs(initialAmountDue)
print("Change Owed: ", changeOwed)