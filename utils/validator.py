import calendar
from datetime import date, datetime

from database.json_service import load
from models.course import Course
from models.student import Student
from models.teacher import Teacher

NOW = datetime.now()  # noqa: DTZ005


def input_text(message):
    return input(f"{message}").strip().lower()


DATA_USERS = "data/users.json"


def user_name():
    data = load(DATA_USERS)
    while True:
        username = input("Username: ")
        for user in data:
            if username != user["username"]:
                return username
            else:
                print(f"Ushbu ({username}) nomli username band.\n")
                print("Qaytadan urunib ko'ring.")


def add_user_input():
    name = input("Name: ")
    surname = input("Surname: ")

    username = user_name()

    while True:
        try:
            phone = input("Phone number: ").strip()
        except ValueError:
            print("Iltimos, butun son kiriting.")
        else:
            if len(phone) == 9 and phone.isdigit():
                break

    return name, surname, username, phone


def add_teacher_input():
    while True:
        try:
            salary = float(input("Salary: "))
            break
        except ValueError:
            print("Iltimos, butun son kiriting.")

    speciality = input("Speciality: ")
    return salary, speciality


def search_input(message):
    return input(message).strip()


def add_course_input():
    name = input("Name: ")
    while True:
        try:
            price = int(input("Price: "))
            break
        except ValueError:
            print("Iltimos, Butun son kiriting.")
    description = input("Description: ")

    return name, price, description


def year_month_day():
    while True:
        try:
            year = int(input("Year:"))
        except ValueError:
            print(f"Year (1900-{NOW.year})")
        else:
            if 1900 <= year <= NOW.year:
                break
            else:
                print(f"Year 1900-{NOW.year}.")

    while True:
        try:
            month = int(input("Month:"))
        except ValueError:
            print("Month (1-12)")
        else:
            if 1 <= month <= 12:
                break
            else:
                print("Month (1-12)")

    _, max_day = calendar.monthrange(year=year, month=month)
    while True:
        try:
            day = int(input("Day:"))
        except ValueError:
            print(f"Day (1-{max_day})")
        else:
            if 1 <= day <= max_day:
                break
            else:
                print(f"Day (1-{max_day})")

    return year, month, day


DATA_COURSES = "data/courses.json"
DATA_TEACHERS = "data/teachers.json"


def add_group_input():
    name = input("Name: ")

    print("\nStart date")
    year, month, day = year_month_day()
    start = datetime(year=year, month=month, day=day)  # noqa: DTZ001

    print("\nStop date")
    year, month, day = year_month_day()
    stop = datetime(year=year, month=month, day=day)  # noqa: DTZ001

    data_courses = load(DATA_COURSES)
    course_id = input("\nCourse ID: ")
    for data_course in data_courses:
        if course_id == data_course["id"]:
            course = Course.from_dict(data_course)
            print(course.info())

            choise = search_input("Add course (yes/no): ").lower()
            if choise == "yes":
                course_id = data_course["id"]
            else:
                course_id = ""

    data_teachers = load(DATA_TEACHERS)
    teacher_id = input("Teacher ID: ")
    for data_teacher in data_teachers:
        if teacher_id == data_teacher["id"]:
            teacher = Teacher.from_dict(data_teacher)
            print(teacher.info())

            choise = search_input("Add teacher (yes/no): ").lower()
            if choise == "yes":
                teacher_id = data_teacher["id"]
            else:
                teacher_id = ""

    return name, start, stop, course_id, teacher_id


def add_payment_input():
    DATA_STUDENTS = "data/students.json"
    data_students = load(DATA_STUDENTS)
    student_id = input("Student ID: ")
    for data_student in data_students:
        if student_id == data_student["id"]:
            student = Student.from_dict(data_student)
            print(student.info())

            choise = input("Add payment (yes/no): ").lower()
            if choise == "yes":
                break

    while True:
        try:
            amount = int(input("Amount: "))
            break
        except ValueError:
            print("Butun son kiriting.")

    print("=== Payment date ===")
    year, month, day = year_month_day()
    payment_date = date(year=year, month=month, day=day)

    payment_type = input("Payment type: ")

    comment = input("Comment: ")

    return student_id, amount, payment_date, payment_type, comment
