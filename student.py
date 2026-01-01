# Function to calculate grade based on average marks
def calculate_grade(average):
    if 90 <= average <= 100:
        return "S"
    elif 80 <= average <= 89:
        return "A"
    elif 65 <= average <= 79:
        return "B"
    elif 50 <= average <= 64:
        return "C"
    elif 40 <= average <= 49:
        return "D"
    else:
        return "F"

# Predefined student details
student = {
    "name": "Shivaji Kurahatti",
    "department": "Computer Science",
    "semester": "5th",
    "marks": [85, 78, 92]  # marks in three subjects
}

# Calculate average
average_marks = sum(student["marks"]) / len(student["marks"])

# Get grade
grade = calculate_grade(average_marks)

# Display student details and grade
print("--- Student Report ---")
print(f"Name       : {student['name']}")
print(f"Department : {student['department']}")
print(f"Semester   : {student['semester']}")
print(f"Marks      : {student['marks']}")
print(f"Average    : {average_marks:.2f}")
print(f"Grade      : {grade}")
