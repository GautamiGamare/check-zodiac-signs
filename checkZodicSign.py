import datetime

print("Welcome to zodic sign checker")
yr= int(input("Enter your Birth year ex[2000]"))
mh = int(input("Enter Birth Month ex[05]"))
dt = int(input("Enter date ex[01]"))
print("Your Birth Date is : ",dt,"/",mh,"/",yr)

current_date = datetime.datetime.now()
year = current_date.year
print("Your Age is",year-yr)
while True:
    if ((mh == 3 and dt >= 21) or (mh == 4 and dt <= 19)):
        print("Your Zodic sign is 'Aries' and Symbol is 'The Ram'")
        break
    elif ((mh == 4 and dt >= 20) or (mh == 5 and dt <= 20)):
        print("Your Zodic sign is 'Taurus' and Symbol is 'The Bull'")
        break
    elif ((mh == 5 and dt >= 21) or (mh == 6 and dt <= 20)):
        print("Your Zodic sign is 'Gemini' and Symbol is 'The Twins'")
        break
    elif ((mh == 6 and dt >= 21) or (mh == 7 and dt <= 22)):
        print("Your Zodic sign is 'Cancer' and Symbol is 'The Crab'")
        break
    elif ((mh == 7 and dt >= 23) or (mh == 8 and dt <= 22)):
        print("Your Zodic sign is 'Leo' and Symbol is 'The Lion'")
        break
    elif ((mh == 8 and dt >= 23) or (mh == 9 and dt <= 22)):
        print("Your Zodic sign is 'Virgo' and Symbol is 'The Virgin'")
        break
    elif ((mh == 9 and dt >= 23) or (mh == 10 and dt <= 22)):
        print("Your Zodic sign is 'Libra' and Symbol is 'The Scales'")
        break
    elif ((mh == 10 and dt >= 23) or (mh == 11 and dt <= 21)):
        print("Your Zodic sign is 'Scorpio' and Symbol is 'The Scorpion'")
        break
    elif ((mh == 11 and dt >= 22) or (mh == 12 and dt <= 21)):
        print("Your Zodic sign is 'Sagittarius' and Symbol is 'The Archer'")
        break
    elif ((mh == 12 and dt >= 22) or (mh == 1 and dt <= 19)):
        print("Your Zodic sign is 'Capricorn' and Symbol is 'The Goat'")
        break
    elif ((mh == 1 and dt >= 20 ) or (mh == 2 and dt <= 18)):
        print("Your Zodic sign is 'Aquarius' and Symbol is 'The Water Bearer'")
        break
    elif ((mh == 2 and dt >= 19 ) or (mh == 3 and dt <= 20)):
        print("Your Zodic sign is 'Pisces' and Symbol is 'The Fishes'")
        break
    else:
        print("Please Enter valid date")
        break
