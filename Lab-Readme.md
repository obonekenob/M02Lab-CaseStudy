# M02 Lab - Case Study if...else and while
Paul R. Thompson  
File name: honors.py  
Program Description:  

 This program is used to determine if a student is qualified  
     for either the Dean's List or the Honor Roll. A message  
     is also displayed if the student is not qualified for  
     either honor.  
   
 The program accepts the first name, last name and the GPA  
     of a student. The name fields are text strings and the  
     GPA is entered as a floating point number.  
  
 The program is controlled by a while-loop boolean set to True  
     and is ended when the operator enters the literal 'ZZZ' in  
     the last name field and the while-loop boolean is set to  
     False.  
  
 The program uses cascading if/else logic to determine eligibilty,  
     checking the GPA value entered beginning with the highest  
     GPA needed and then downward GPA values from then on.  
  
 If the GPA entered is 3.5 or greater a message is displayed  
     informing the operator the student is qualified for the  
     Dean's List.  
 If the GPA entered is 3.25 or greater a message is displayed  
     informing the operator the student is qualified for the  
     Honor Roll.  
 If the GPA entered is below 3.25 a message is displayed  
     informing the operator the student is not qualified for  
     either list.  
