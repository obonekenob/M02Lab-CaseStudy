# Mo2-Lab
# Paul R. Thompson
# File name: honors.py  
# Program Description:  

goodToGo = True
myNo = False
zStop = "ZZZ"
dList = 3.5
hList = 3.25

print("This program will test if a student\'s GPA qualifies that student for ")
print(" either the Dean\'s List or the Honor Roll.")
print("To end the program type ZZZ when asked for the student\'s last name.")

while goodToGo:
    lastName = str(input("Enter the last name. "))
    if lastName.upper() == zStop:
        print("Thank you for using this program. ")
        goodToGo = myNo 
    else:
        firstName = str(input("Enter the student\'s first name. "))
        GPA = float(input("Enter the student\'s GPA: "))
        if GPA >= dList:
            print("The student has made the Dean\'s List. ")
        elif GPA >= hList:
            print("This student has made the Honor Roll.")
        else:
            print("This student does not qualify for either list.")
