# WEEK 2

# create a dictionary consisting of the fruit as a key and calories as value
fruitDict = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

# receive user input and lower for case insensitivity comparison
fruit = (input("Item: ")).lower()

# check if user input exists as a key in dictionary
if fruit in fruitDict:
    print ("Calories:", fruitDict[fruit]) # if exists, print value respective to key