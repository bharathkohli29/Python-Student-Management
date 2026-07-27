import argparse

from database import add_student, delete_student, get_student, list_students
from student import Student


def build_parser():
    parser = argparse.ArgumentParser(description="Student management CLI")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add", help="Add a new student")
    add.add_argument("--name", required=True, help="Student full name")
    add.add_argument("--age", required=True, type=int, help="Student age")
    add.add_argument("--grade", required=True, help="Student letter grade")

    subparsers.add_parser("list", help="List all students")

    show = subparsers.add_parser("show", help="Show a student by ID")
    show.add_argument("--id", required=True, type=int, help="Student ID")

    delete = subparsers.add_parser("delete", help="Delete a student by ID")
    delete.add_argument("--id", required=True, type=int, help="Student ID")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        student = Student(name=args.name, age=args.age, grade=args.grade)
        student = add_student(student)
        print(f"Added student ID {student.id}: {student.name} (Age {student.age}, Grade {student.grade})")

    elif args.command == "list":
        students = list_students()
        if not students:
            print("No students found.")
            return
        for student in students:
            print(f"{student.id}: {student.name} | Age {student.age} | Grade {student.grade}")

    elif args.command == "show":
        student = get_student(args.id)
        if student is None:
            print(f"No student found with ID {args.id}")
            return
        print(f"{student.id}: {student.name} | Age {student.age} | Grade {student.grade}")

    elif args.command == "delete":
        deleted = delete_student(args.id)
        if deleted:
            print(f"Deleted student with ID {args.id}")
        else:
            print(f"No student found with ID {args.id}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
