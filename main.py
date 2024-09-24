# a function to calculate the final score and grades using the scores
def calc_grade(scores):
     sum_score = sum([int(score) for score in scores])
     avg_score = sum_score/len(scores)

     # condition to specify the grades

     if (avg_score >=60 and avg_score < 70):
          grade = "D"
     elif (avg_score >=70 and avg_score < 80):
          grade = "c"
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
          print(f"Total Score: {student["sum_scores"]}")
          print(f"Final Grade: {student['grade']}")
             
          
# this says to start from the main function 
if ( __name__ == "__main__"):



    student_list = []
    num_subjects = 3 # 3 subjects are taken 



# making a loop to store the information of the students

while(True):
     student_name = input("enter your name please! ")
     student_id = input("enter your ID number: ")
     scores = []

     for i in range(num_subjects):
           
          
            subject = {0:"physics" , 1: "chemistry" , 2:"maths"}

            score = (input(f"enter your score in {subject[i]}: "))  # type casting string score to int
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



     
          
     



