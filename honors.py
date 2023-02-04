# Mo2-Lab
# Paul R. Thompson
# File name: honors.py  
# Program Description:  

goodToGo = True
zstop = "ZZZ"

print("This program will test if a student\'s GPA qualifies that student for ")
print(" either the Dean\'s List or the Honor Roll.")
print("To end the program type ZZZ when asked for the student\'s last name.")

while goodToGo:
    lastName = str(input("Enter the last name. "))
    if lastName == zstop:
        print("Thank you for using this program. ")
        break
    firstName = str(input("Enter the first name. "))
