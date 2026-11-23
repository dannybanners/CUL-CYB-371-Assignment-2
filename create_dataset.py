import csv

# Create a fictional student dataset and save it as a CSV file.
students = [
    ["STU001", "Computer Science", 200, 92, 78],
    ["STU002", "Cybersecurity", 200, 85, 84],
    ["STU003", "Information Technology", 300, 88, 73],
    ["STU004", "Computer Science", 100, 76, 69],
    ["STU005", "Data Science", 300, 95, 91],
    ["STU006", "Cybersecurity", 100, 81, 76],
    ["STU007", "Information Technology", 200, 70, 65],
    ["STU008", "Data Science", 400, 90, 87],
    ["STU009", "Computer Science", 300, 84, 80],
    ["STU010", "Cybersecurity", 400, 78, 72],
    ["STU011", "Information Technology", 100, 93, 88],
    ["STU012", "Data Science", 200, 67, 61],
    ["STU013", "Computer Science", 400, 89, 85],
    ["STU014", "Cybersecurity", 300, 91, 90],
    ["STU015", "Information Technology", 400, 82, 77],
]

columns = [
    "Student_ID",
    "Department",
    "Level",
    "Attendance_Percentage",
    "Average_Examination_Score"
]

with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(students)

print("Student dataset created successfully: student_dataset.csv")
