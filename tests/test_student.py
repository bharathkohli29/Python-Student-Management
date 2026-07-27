import pytest

from student import Student
from validation import validate_age, validate_grade, validate_name


def test_student_validation():
    student = Student(name="Alice Smith", age=20, grade="A")
    assert student.name == "Alice Smith"
    assert student.age == 20
    assert student.grade == "A"


def test_validate_name_rejects_empty():
    with pytest.raises(ValueError):
        validate_name("")


def test_validate_age_rejects_negative():
    with pytest.raises(ValueError):
        validate_age(-1)


def test_validate_grade_normalizes():
    assert validate_grade("b+") == "B+"
