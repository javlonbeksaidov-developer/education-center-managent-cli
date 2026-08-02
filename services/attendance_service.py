from database.json_service import load, save
from models.attendance import Attendance
from models.group import Group
from models.student import Student
from utils.validator import search_input

DATA_ATTENDANCES = "data/attendances.json"
DATA_GROUPS = "data/groups.json"
DATA_STUDENTS = "data/students.json"


def take_attendance(user):
    data_attendances = load(DATA_ATTENDANCES)
    data_groups = load(DATA_GROUPS)
    data_students = load(DATA_STUDENTS)
    print("=== Take attendance ===\n")
    group_id = search_input("Group ID: ")

    for data_group in data_groups:
        if (group_id == data_group["id"]) and (
            (user["role"] == "admin")
            or (user["role"] == "teacher" and data_group["teacher_id"] == user["id"])
        ):
            group = Group.from_dict(data_group)
            print(f"\n{group.info()}")

            choise = input("Take attendance (yes/no): ").lower()
            if choise == "yes":
                students = {}
                for student in data_group["students"]:
                    for data_student in data_students:
                        if student == data_student["id"]:
                            data = Student.from_dict(data_student)
                            choise = input(f"\n{data.info()} (yes/no): ").lower()

                            if choise == "yes":
                                students[data_student["id"]] = True
                            else:
                                students[data_student["id"]] = False

                attendance = Attendance(group_id=group_id)
                data = attendance.to_dict()
                data["student_id"].append(students)
                data_attendances.append(data)

                save(DATA_ATTENDANCES, data_attendances)
                print("Success")


def show_attendance(user):
    data_attendances = load(DATA_ATTENDANCES)
    print("=== Show attendance ===\n")
    for i, data_attendance in enumerate(data_attendances):
        attendance = Attendance.from_dict(data_attendance)
        print(f"{i}. {attendance}")


def student_attendance(user):
    data_attendances = load(DATA_ATTENDANCES)
    data_students = load(DATA_STUDENTS)
    print("=== Show student attendance ===\n")
    student_id = search_input("Student ID: ")
    for data_student in data_students:
        if student_id == data_student["id"]:
            student = Student.from_dict(data_student)
            print(student.info())

            choise = input("Show attendance (yes/no): ").lower()
            if choise == "yes":
                student_attendance = []
                for data_attendance in data_attendances:
                    for attendance in data_attendance["student_id"]:
                        if student_id in attendance:
                            student_attendance.append(attendance[student_id])

                print(f"\n{data_student['username']} attendance:\n{student_attendance}")
