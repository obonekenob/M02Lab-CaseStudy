# Mo2-Lab
# Paul R. Thompson
# File name: honors.py  
# Program Description:  

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
