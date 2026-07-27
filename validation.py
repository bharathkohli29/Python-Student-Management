import re
from typing import Any


def validate_name(name: str) -> str:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    name = name.strip()
    if len(name) > 100:
        raise ValueError("Name must be at most 100 characters.")
    return name


def validate_age(age: Any) -> int:
    if isinstance(age, str):
        if age.isdigit():
            age = int(age)
        else:
            raise ValueError("Age must be an integer.")
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150.")
    return age


def validate_grade(grade: str) -> str:
    if not isinstance(grade, str) or not grade.strip():
        raise ValueError("Grade must be a non-empty string.")
    normalized = grade.strip().upper()
    if not re.fullmatch(r"[A-F][+-]?", normalized):
        raise ValueError("Grade must be a letter grade from A to F, optionally with + or -.")
    return normalized
