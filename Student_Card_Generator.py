# {Assignment name: Day 2 – Mini Project: Student Report Card Generator

# Description: Build a program that reads a student's marks and produces a formatted report card, applying arithmetic, logical, and conditional logic.

# Activity instructions: Write a Python program  that generates a student report card. It must:

#Read the student's name, roll number, and marks in three subjects using input(), casting the marks with float().
#Store the student's details in a dictionary.
#Calculate the total and percentage using arithmetic operators.
#Decide pass/fail using logical operators — the student passes only if every subject is at or above the pass mark (40).
#Assign a letter grade (A+, A, B, C, D, F) using an if / elif / else chain based on the percentage.
#Use a nested if plus a set membership test (e.g. grade in {"A+", "A"}) to award a distinction remark.
#Set a final PASS/FAIL status using a ternary expression.
#Print a neatly formatted report card using f-strings and separator lines. 

# Student Report Card Generator
print("Welcome to the Student Report Card Generator")
# Step 1: Read student details
name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")
subject1_marks = float(input("Enter the marks for subject 1: "))
subject2_marks = float(input("Enter the marks for subject 2: "))
subject3_marks = float(input("Enter the marks for subject 3: "))
# Step 2: Store details in a dictionary
student_details = {
    "name": name,
    "roll_number": roll_number,
    "marks": [subject1_marks, subject2_marks, subject3_marks]
}
# Step 3: Calculate total and percentage
total_marks = sum(student_details["marks"])
percentage = (total_marks / 300) * 100
# Step 4: Determine pass/fail status
pass_mark = 40
is_pass = all(mark >= pass_mark for mark in student_details["marks"])
# Step 5: Assign letter grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
# Step 6: Award distinction remark
distinction = "Distinction" if grade in {"A+", "A"} else ""
# Step 7: Set final PASS/FAIL status
final_status = "PASS" if is_pass else "FAIL"
# Step 8: Print formatted report card
print("\n" + "="*30)
print(f"Report Card for {student_details['name']} (Roll No: {student_details['roll_number']})")
print("="*30)
print(f"Subject 1 Marks: {student_details['marks'][0]}")
print(f"Subject 2 Marks: {student_details['marks'][1]}")
print(f"Subject 3 Marks: {student_details['marks'][2]}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
if distinction:
    print(f"Remark: {distinction}")
print(f"Final Status: {final_status}")
print("="*30)
