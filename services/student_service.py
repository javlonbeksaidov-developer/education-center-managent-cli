from database.json_service import load, save
from models.student import Student
from models.group import Group
from utils.validator import add_user_input, input_text, search_input

DATA_USERS = "data/users.json"
DATA_STUDENTS = "data/students.json"
DATA_ATTENDANCES = "data/attendances.json"
DATA_PATMENTS = "data/payments.json"
DATA_GROUPS = "data/groups.json"


def add_student(user):
    data_users = load(DATA_USERS)
    data_students = load(DATA_STUDENTS)
    name, surname, username, phone = add_user_input()

    student = Student(name=name, surname=surname, username=username, phone=phone)

    add_student = student.to_dict()
    data_users.append(add_student)
    data_students.append(add_student)

    save(DATA_USERS, data_users)
    save(DATA_STUDENTS, data_students)
    return f"{name.title()} {surname.title()} o'quv markazga qo'shildi."


def show_students(user):
    data_students = load(DATA_STUDENTS)
    print("=== Show Students ===\n")
    for index, student in enumerate(data_students, start=1):
        students = Student.from_dict(student)
        print(f"{index}. {students.info()}")


def search_student(user):
    data_students = load(DATA_STUDENTS)
    print("=== Search Student ===\n")
    search = search_input("ID yoki username: ")
    for data_student in data_students:
        if search == data_student["id"] or search == data_student["username"]:
            student = Student.from_dict(data_student)
            print(student.info())
            return

    print(f"{search.title()} topilmadi")


def update_student(user):
    data_users = load(DATA_USERS)
    data_students = load(DATA_STUDENTS)
    print("=== Update Student ===\n")
    search = search_input("ID yoki username:")
    for i, data_student in enumerate(data_students):
        if search == data_student["id"] or search == data_student["username"]:
            student = Student.from_dict(data_student)
            print(student.info())

            choise = input_text("\nUpdate student (yes/no): ")
            if choise == "yes":
                name, surname, username, phone = add_user_input()

                data_student["name"] = name
                data_student["surname"] = surname
                data_student["username"] = username
                data_student["phone"] = phone

                data_students[i] = data_student

                for j, data_user in enumerate(data_users):
                    if data_student["id"] == data_user["id"]:
                        data_user["name"] = name
                        data_user["surname"] = surname
                        data_user["username"] = username
                        data_user["phone"] = phone

                        data_users[j] = data_user
                        break

                save(DATA_USERS, data_users)
                save(DATA_STUDENTS, data_students)

                print(f"{username} muvaffaqiyatli yangilandi.")
                return

    print("Student topilmadi.")


def delete_student(user):
    data_users = load(DATA_USERS)
    data_students = load(DATA_STUDENTS)
    print("=== Delete Student ===\n")
    search = search_input("ID yoki username: ")

    for data_student in data_students:
        if search == data_student["id"] or search == data_student["username"]:
            student = Student.from_dict(data_student)
            print(student.info())

            choise = input_text("\nDelete student (yes/no): ")
            if choise == "yes":
                data_students.remove(data_student)

                for data_user in data_users:
                    if data_student["id"] == data_user["id"]:
                        data_users.remove(data_student)
                        break

            save(DATA_USERS, data_users)
            save(DATA_STUDENTS, data_students)

            print(f"\n{data_student['username']} o'chirildi.")
            return


def block_active_student(user):
    data_users = load(DATA_USERS)
    data_students = load(DATA_STUDENTS)
    print("=== Block or Active Student ===\n")
    search = search_input("ID yoki username: ")

    for i, data_student in enumerate(data_students):
        if search == data_student["id"] or search == data_student["username"]:
            student = Student.from_dict(data_student)
            print(student.info())

            if data_student["status"] == "block":
                text = "active"
            else:
                text = "block"

                choise = input_text(f'"{text}" qilasizmi? (yes/no): ')
                if choise == "yes":
                    data_student["status"] = text
                    data_students[i] = data_student

                    for j, data_user in enumerate(data_users):
                        if data_student["id"] == data_user["id"]:
                            data_user["status"] = text
                            data_users[j] = data_user
                            break

                save(DATA_USERS, data_users)
                save(DATA_STUDENTS, data_students)

                print(f"\n{data_student['username']} ({text}) qilindi.")
                return


""" === Student panel ==="""


def student_my_group(user):
    data_groups = load(DATA_GROUPS)
    print(f"===== {user['username']}'s groups =====\n")
    for data_group in data_groups:
        for student_id in data_group["students"]:
            if student_id == user["id"]:
                group = Group.from_dict(data_group)
                print(group.info())


def student_attendance(user):
    data_attendances = load(DATA_ATTENDANCES)
    print(f"===== {user['username']}'s attendances =====\n")
    attendances = []
    for data_attendance in data_attendances:
        for student_ids in data_attendance["student_id"]:
            if user["id"] in student_ids:
                attendance = {
                    "attendance id": data_attendance["attendance id"],
                    "t-f": student_ids[user["id"]],
                    "group id": data_attendance["group_id"],
                    "created_at": data_attendance["created_at"],
                }
                attendances.append(attendance)

    print("No. Attendance ID - Qatnashdi - Groups ID - Date")
    for i, attendance in enumerate(attendances, start=1):
        print(
            f"{i}. {attendance['attendance id']} - {attendance['t-f']} - {attendance['group id']} - {attendance['created_at']}"
        )


def student_payments(user):
    data_payments = load(DATA_PATMENTS)
    print(f"===== {user['username']}'s payments =====\n")
    for i, data_payment in enumerate(data_payments, start=1):
        print(f"{i}. {data_payment}")
