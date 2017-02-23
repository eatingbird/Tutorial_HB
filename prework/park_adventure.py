# Assignment2 for Hackbright March 2017 course
# code by Soo Park, consulthere@gmail.com

# Code specification
# have your user make at least two decisions (use at least two if/elif/else)

# What to build
# Get user name
# Ask what is the preferred area to visit
# Ask what city within the user want to visit
# Give the user link to the citi information

# Greeting
userName = raw_input("What is your user name? ")
print (" Hello %s, I heard you are planning a trip." %(userName))

# First choice
print("I can give you a one line advice on the city you may visit.")
print("Choose an activity you like. ")
firstAnswer = int(raw_input("1)Walking, 2) Driving? Enter the number: "))

# Second choice
if firstAnswer ==1: # Likes walking
    print("New York and San Francisco are great cities to drive around.")
    walkCity = int(raw_input("Which one? 1) New York, 2) San Francisco? Enter the number: "))
    if walkCity == 1:
        print("You should go to some good restaurants too!")
    elif walkCity ==2:
        print("Call me!")
    else:
        print("Wrong choice")
elif firstAnswer ==2: # Likes driving
    print("Los Angeles and Portland are great cities to drive around.")
    walkCity = int(raw_input("Which one? 1) LA, 2) Portland? Enter the number: "))
    if walkCity == 1:
        print("Expect traffic.")
    elif walkCity == 2:
        print("Don't forget to visit the bookstore!")
    else:
        print("Wrong choice")
else: # No data for the activity
    print("Wrong choice")

print("[THE END]")