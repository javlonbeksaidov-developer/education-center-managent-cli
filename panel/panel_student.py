from menu.menu_student import menu_student
from services.student_service import (
    student_attendance,
    student_my_group,
    student_payments,
)
from services.user_service import profile
from utils.validator import input_text


def student(user):
    while True:
        print(menu_student())
        choice = input_text(">>> ")
        if choice == "0":
            print(f"The end | {user['name'].title()} {user['surname'].title()}")
            break
        elif choice == "1":
            print(profile(user))
        elif choice == "2":
            student_my_group(user)
        elif choice == "3":
            student_attendance(user)
        elif choice == "4":
            student_payments(user)