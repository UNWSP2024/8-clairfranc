# Claire Francis, March 20th, 2025, Week8_program3.py

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).



import random
def state_quiz():

    answers_right = 0
    answers_wrong = 0
    USstates = {"Alabama" : "Montgomery", "Alaska" : "Juneau", "Arizona" : "Phoenix",
                "Arkansas" : "Little Rock", "California" : "Sacramento", "Colorado" : "Denver",
                "Connecticut" : "Hartford", "Delaware" : "Dover", "Florida" : "Tallahassee",
                "Georgia" : "Atlanta", "Hawaii" : "Honolulu", "Idaho" : "Boise",
                "Illinois" : "Springfield", "Indiana" : "Indianapolis", "Iowa" : "Des Moines",
                "Kansas" : "Topeka", "Kentucky" : "Frankfort", "Louisiana" : "Baton Rouge",
                "Maine" : "Augusta", "Maryland" : "Annapolis", "Massachusetts" : "Boston",
                "Michigan" : "Lansing", "Minnesota" : "Saint Paul", "Mississippi" : "Jackson",
                "Missouri" : "Jefferson City", "Montana" : "Helena", "Nebraska" : "Lincoln",
                "Nevada" : "Carson City", "New Hampshire" : "Concord", "New Jersey" : "Trenton",
                "New Mexico" : "Santa Fe", "New York" : "Albany", "North Carolina" : "Raleigh",
                "North Dakota" : "Bismarck", "Ohio" : "Columbus", "Oklahoma" : "Oklahoma City",
                "Oregon" : "Salem", "Pennsylvania" : "Harrisburg", "Rhode Island" : "Providence",
                "South Carolina" : "Columbia", "South Dakota" : "Pierre", "Tennessee" : "Nashville",
                "Texas" : "Austin", "Utah" : "Salt Lake City", "Vermont" : "Montpelier",
                "Virginia" : "Richmond", "Washington" : "Olympia", "West Virginia" : "Charleston",
                "Wisconsin" : "Madison", "Wyoming" : "Cheyenne"}

    key_list = list(USstates.keys())
    num = random.randint(0, 49)
    state = key_list[num]
    guess = input("Enter the capital of " + str(state) + ": ")
    answer = USstates.get(state)
    print(answer)


    if guess == answer:
        answers_right += 1
        print("That is correct!")
    else:
        answers_wrong += 1
        print("womp, womp.")


while(1):
    state_quiz()
