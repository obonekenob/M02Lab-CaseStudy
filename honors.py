# Mo2-Lab
# Paul R. Thompson
# File name: honors.py  
# Program Description:  

goodToGo = True
Bzstop = "ZZZ"
Lzstop = "zzz"
Dlist = 3.5
Hlist = 3.25

print("This program will test if a student\'s GPA qualifies that student for ")
print(" either the Dean\'s List or the Honor Roll.")
print("To end the program type ZZZ when asked for the student\'s last name.")

while goodToGo:
    lastName = str(input("Enter the last name. "))
    if lastName == Bzstop or lastName == Lzstop:
        print("Thank you for using this program. ")
        break
    else:
        firstName = str(input("Enter the first name. "))
        GPA = float(input("Enter the GPA: "))
#        if GPA >= 3.5:
        if GPA >= Dlist:
            print("Congratulations. You are on the Dean\'s List. ")
#        elif GPA >= 3.25:
        elif GPA >= Hlist:
            print("Congratulations. You made the Honor Roll.")
        else:
            print("I am sorry. You do not qualify for either list.")
