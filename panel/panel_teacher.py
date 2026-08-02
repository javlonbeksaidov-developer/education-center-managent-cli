from menu.menu_teacher import menu_teacher
from services.attendance_service import take_attendance
from services.teacher_service import (
    teacher_my_groups,
    teacher_students,
)
from services.user_service import profile
from utils.validator import input_text


def teacher(user):
    while True:
        print(menu_teacher())
        choice = input_text(">>> ")
        if choice == "0":
            print(f"The end | {user['name'].title()} {user['surname'].title()}")
            break
        elif choice == "1":
            print(profile(user))
        elif choice == "2":
            teacher_my_groups(user)
        elif choice == "3":
            teacher_students(user)
        elif choice == "4":
            take_attendance(user)
