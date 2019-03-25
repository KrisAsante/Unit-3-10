# Created by: Chris Asante
# Created on: 19-March-2019
# Created for: ICS3U
# Daily Assignment – Unit 3-10  n n
# This program is an application that displays the running average
 
number_times_inputed = 0.0
running_average = 0.0
sum_of_marks = 0.0
user_input = 0.0

print(input("Enter any number from 0-100."))
print(input("Type '-1' to get your final average"))

while user_input != -1.0:  
     if user_input < -1.0 or user_input > 100: 
        print ("Please enter a positive number between 0-100")    
        number_times_inputed = number_times_inputed -1.0  
        sum_of_marks = sum_of_marks - user_input
        user_input = input("Mark entered: ")
        user_input = float(user_input)
        number_times_inputed = number_times_inputed + 1.0                    
        sum_of_marks = sum_of_marks + user_input 
        running_average = sum_of_marks/number_times_inputed
     else:
        user_input = input("Mark entered: ")
        user_input = float(user_input)
        number_times_inputed = number_times_inputed + 1.0                    
        sum_of_marks = sum_of_marks + user_input 
        running_average = sum_of_marks/number_times_inputed
          
if user_input == -1.0:
   number_times_inputed = number_times_inputed - 1.0
   sum_of_marks = sum_of_marks - user_input
   running_average = sum_of_marks/number_times_inputed                  
   print ("Average is: " + str(running_average))     