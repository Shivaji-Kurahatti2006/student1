# Import the function if it's in another file, or define it here
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

# Predefined student marks
student_marks = [85, 78, 92]

def test_student_grade():
    average_marks = sum(student_marks) / len(student_marks)
    grade = calculate_grade(average_marks)
    assert grade == "A"
