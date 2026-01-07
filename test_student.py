import student_grade

def test_grade_S():
    assert student_grade.calculate_grade(95) == "S"

def test_grade_A():
    assert student_grade.calculate_grade(85) == "A"

def test_grade_B():
    assert student_grade.calculate_grade(70) == "B"

def test_grade_C():
    assert student_grade.calculate_grade(55) == "C"

def test_grade_D():
    assert student_grade.calculate_grade(45) == "D"

def test_grade_F():
    assert student_grade.calculate_grade(30) == "F"
