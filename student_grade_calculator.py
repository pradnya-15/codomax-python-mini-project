
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

subjects = ["Python", "Mathematics", "English", "Computer Science", "Data Science"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject} (out of 100): "))
    marks.append(mark)

total = sum(marks)
average = total / len(subjects)
grade = calculate_grade(average)

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2))
print("Grade:", grade)

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
