# a function to calculate the final score and grades using the scores


def calc_grade(scores):
     sum_score = sum([int(score) for score in scores])
     avg_score = sum_score/len(scores)

     # condition to specify the grades

     if (avg_score >=60 and avg_score < 70):
          grade = "D"
     elif (avg_score >=70 and avg_score < 80):
          grade = "C"
     elif (avg_score >=80 and avg_score < 90):
          grade = "B"
     elif (avg_score >=90 and avg_score < 100):
          grade = "A"
     else :
          grade = "F"
         

     return sum_score,grade
     

# making a function to display the info of students

def display_info(student_list):
     
     print("\n STUDENT DETAILS:\n")
     for student in student_list:
          print(f"Name: {student['name']}")
          print(f"Student ID: {student['Id']}")
          print(f"Total Marks: {student['sum_scores']}")

          
          print(f"Final Grade: {student['grade']}")
          
          # to give remarks 
          if(student["grade"]=="A" ):
               print("Remarks: Excellent academics keep it up!")
          elif(student["grade"] == "B" ):
               print("Remarks: You seem hardworking keep going!")
          elif(student["grade"] == "C" ):
               print("Remarks: You are studying well , keep going!")
          elif(student["grade"] == "D" ):
               print("Remarks: You need to study well and you can do much more!")
               
          else:
               print("Remarks: You need to study hard, don't loose hope!")


          print("\n") # to print the space after detail of one student
             

     
 
def mainFunction():

       
     student_list = [] # a list to store my dictionaries 
     num_subjects = 3 # 3 subjects are taken 



# making a loop to store the information of the students

     while(True):
             
     
     
             student_name = input("Enter Student's name: ")
             while student_name.replace(" ", "").isalpha() == False : # here we make string spaceless and check if its character
               student_name = input("Enter valid name: ") 
      
      
     
          
     
             student_id = input("enter the ID number: ")
             while student_id.isalpha() == True :
              
              student_id = input("enter the valid Student Id(In Number): ") 
      
      
             scores = []

             for i in range(num_subjects):
                  
           
          
                  subject = {0:"physics" , 1: "chemistry" , 2:"maths"}

                  score = (input(f"enter marks in {subject[i]}: "))  # type casting string score to int
            
            # check if the marks is greater than 100 or less than or equal to 0
                  while(int(score) > 100 or int(score) <= 0):
                      print("you entered invalid marks \n")
                      score = (input(f"enter the marks in {subject[i]} again: ")) 

                  scores.append(score) # adding our individual score value to the list scores

           

     # storing student information in a dictionary
             final_score , total_grade = calc_grade(scores) # returns two values to variables respectively

             info_students ={"name": student_name , "Id": student_id, "scores" : score , "sum_scores": final_score , "grade": total_grade }
             student_list.append(info_students) # a list of dictionaries is created in student_list

     # if more student info to be added 
             other_student = input("Would you like to add info of any other student ( yes / no ): ")

# if the other student is not added then exit 
             if (other_student !="yes"):
                
                break


# now  displaying the info of all students that entered the marks from our list student_list here
     display_info(student_list)


if __name__ == "__main__": # to make my script safe to run in here
     mainFunction()




 




     
          
     



