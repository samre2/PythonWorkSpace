#Student Report Card Generator

print("Welcome to the Studnet Report Card Genrrator")

#Step 1 : Read Student Details

name = input("Enter the Student's Name: ")
roll_number = int(input("Enter the Student's Roll Number: "))
subject1_marks = float(input("Enter the marks for Subject 1 : "))
subject2_marks = float(input("Enter the marks for Subject 2 : "))
subject3_marks = float(input("Enter the marks for Subject 3 : "))

#Step 2 : Store the details in a dictionary

student_details = {
    "name" : name,
    "roll_number" : roll_number,
    "marks" : [subject1_marks, subject2_marks, subject3_marks]
}

#Step 3 : Calculate the total and percentage using arithemetic operators

total_marks = sum(student_details["marks"])  # sum() function is used to calculate the total marks by summing up the marks in the list student_details["marks"]
percentage =  (total_marks / 300) * 100       # The percentage is calculated by dividing the total marks by the maximum possible marks (300 in this case, assuming each subject is out of 100) and then multiplying by 100 to convert it to a percentage.

#Step 4 : Decide pass/fail using logical operators - the students passes if every subject is at or above the passmark (40)

pass_mark = 40
is_pass = all (mark >= pass_mark for mark in student_details["marks"])  # The all() function is used to check if all the marks in the list student_details["marks"] are greater than or equal to the pass_mark (40). It returns True if all marks meet the condition, otherwise it returns False.  

#Step 5 : Assign a letter grade (A+, A, B, C, D, F) using an if / elif / else chain based on the percentage
if percentage >= 90:
    grade = "A+"

elif percentage >=80:
    grade = "A"
elif percentage >=70:
    grade = "B"
elif percentage >=60:
    grade = "C"
elif percentage >=50:
    grade = "D"
else:
    grade = "F"

#Step 6 : Award Distinction remarks using a nested if plus a set membership test (e.g. grade in {"A+", "A"}) to award a distinction remark.
distinction = "Distinction" if grade in {"A+", "A"} else ""  # This line uses a ternary expression to assign the value "Distinction" to the variable distinction if the grade is either "A+" or "A". If the grade is not in the set {"A+", "A"}, it assigns an empty string "" to distinction.      

#Step 7 : Set a final PASS/FAIL status using a ternary expression.
final_status = "PASS" if is_pass else "FAIL"  # This line uses a ternary expression to assign the value "PASS" to the variable final_status if is_pass is True, otherwise it assigns "FAIL". The variable is_pass was determined earlier based on whether all marks were above the pass mark.

#Step 8 : Print a neatly formatted report card using f-strings and separator lines.
print("\n" + "="*30)
print(f"Report Card for {student_details['name']} (Roll No: {student_details['roll_number']})")
print("="*30)   
print(f"Subject 1 Marks: {student_details['marks'][0]}")
print(f"Subject 2 Marks: {student_details['marks'][1]}")
print(f"Subject 3 Marks: {student_details['marks'][2]}")    
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")  # The :.2f format specifier is used to format the percentage value to 2 decimal places.
print(f"Grade: {grade}")

if distinction:
    print(f"Remark: {distinction}")
print(f"Final Status: {final_status}")
print("="*30)   

