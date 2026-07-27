from dataclasses import dataclass, field
from typing import Optional

from validation import validate_age, validate_grade, validate_name


@dataclass
class Student:
    id: Optional[int] = field(default=None)
    name: str = field(default="")
    age: int = field(default=0)
    grade: str = field(default="")

    def __post_init__(self):
        self.name = validate_name(self.name)
        self.age = validate_age(self.age)
        self.grade = validate_grade(self.grade)

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "age": self.age, "grade": self.grade}

    @classmethod
    def from_row(cls, row: Optional[dict]) -> Optional["Student"]:
        if row is None:
            return None
        return cls(id=row["id"], name=row["name"], age=row["age"], grade=row["grade"])
