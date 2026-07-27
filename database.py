import sqlite3
from pathlib import Path
from typing import List, Optional

from student import Student

_DB_PATH = Path(__file__).with_name("students.db")


def _get_connection():
    conn = sqlite3.connect(_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _initialize_db():
    with _get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
            """
        )
        conn.commit()


def add_student(student: Student) -> Student:
    _initialize_db()
    with _get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (student.name, student.age, student.grade),
        )
        student.id = cursor.lastrowid
    return student


def get_student(student_id: int) -> Optional[Student]:
    _initialize_db()
    with _get_connection() as conn:
        row = conn.execute("SELECT id, name, age, grade FROM students WHERE id = ?", (student_id,)).fetchone()
    return Student.from_row(row)


def list_students() -> List[Student]:
    _initialize_db()
    with _get_connection() as conn:
        rows = conn.execute("SELECT id, name, age, grade FROM students ORDER BY id").fetchall()
    return [Student.from_row(row) for row in rows]


def delete_student(student_id: int) -> bool:
    _initialize_db()
    with _get_connection() as conn:
        cursor = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    return cursor.rowcount > 0
