def main():
    mealTime = input("What time is it? ")
    convertedTime = convert(mealTime)

    # simple range check using if statement, sometimes i think too much :')
    if convertedTime >= 7 and convertedTime <=8:
        print("breakfast time")
    elif convertedTime >= 12 and convertedTime <=13:
        print("lunch time")
    elif convertedTime >= 18 and convertedTime <=19:
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":") # 7:30 > 7, 30 respectively
    minutes = float(minutes) / 60 # convert to float and divide by 60 mins
    hour = float(hour) # convert to float
    newTime = hour+minutes # add together
    return newTime

if __name__ == "__main__":
    main()