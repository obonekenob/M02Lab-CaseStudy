# Mo2-Lab
# Paul R. Thompson
# File name: honors.py  
# Program Description:  
#
# This program is used to determine if a student is qualified
#     for either the Dean's List or the Honor Roll. A message
#     is also displayed if the student is not qualified for
#     either honor.
# 
# The program accepts the first name, last name and the GPA
#     of a student. The name fields are text strings and the
#     GPA is entered as a floating point number.
#
# The program is controlled by a while-loop boolean set to True
#     and is ended when the operator enters the literal 'ZZZ' in
#     the last name field and the while-loop boolean is set to
#     False.
#
# The program uses cascading if/else logic to determine eligibilty,
#     checking the GPA value entered beginning with the highest
#     GPA needed and then downward GPA values from then on.
#
# If the GPA entered is 3.5 or greater a message is displayed
#     informing the operator the student is qualified for the
#     Dean's List.
# If the GPA entered is 3.25 or greater a message is displayed
#     informing the operator the student is qualified for the
#     Honor Roll.
# If the GPA entered is below 3.25 a message is displayed
#     informing the operator the student is not qualified for
#     either list.
#
#    Initial variable definitions and assigned values
#
goodToGo = True       #  While loop control - pgm runs when True
zStop = "ZZZ"         #  User entry to teminate program
dList = 3.5           #  minimum value for Deans list
hList = 3.25          #  minimum value for Honor Roll
#
#  Introductory comments and instructions
#
print("This program will test if a student\'s GPA qualifies that student for ")
print(" either the Dean\'s List or the Honor Roll.")
print("To end the program type ZZZ when asked for the student\'s last name.")

while goodToGo:        # Begin while loop

    lastName = str(input("Enter the last name. "))   # Get last name or ZZZ to stop loop

    if lastName.upper() == zStop:                    # Check for ZZZ
        print("Thank you for using this program. ")  # ZZZ found. Display exit message
        goodToGo = False                             # Set loop vaiable to False and end program
    
    else:
        firstName = str(input("Enter the student\'s first name. ")) # Get first name
        GPA = float(input("Enter the student\'s GPA: "))            # Get GPA

        if GPA >= dList:                                            # If GPA equal or greater 3.5
            print("This student has made the Dean\'s List. ")       # Print deans list message and get next student

        elif GPA >= hList:                                          # if GPA equal or greater 3.25
            print("This student has made the Honor Roll.")          # Print honor roll message and get next student

        else:                                                       # GPA less than 3.25
            print("This student does not qualify for either list.") # print not qualified message and get next student
