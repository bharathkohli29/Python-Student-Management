import os
import sys
import importlib.util

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

STUDENT_PATH = os.path.join(ROOT_DIR, "student.py")
VALIDATION_PATH = os.path.join(ROOT_DIR, "validation.py")

spec_student = importlib.util.spec_from_file_location("student", STUDENT_PATH)
student_module = importlib.util.module_from_spec(spec_student)
sys.modules["student"] = student_module
spec_student.loader.exec_module(student_module)

spec_validation = importlib.util.spec_from_file_location("validation", VALIDATION_PATH)
validation_module = importlib.util.module_from_spec(spec_validation)
sys.modules["validation"] = validation_module
spec_validation.loader.exec_module(validation_module)

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
