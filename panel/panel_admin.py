from menu.menu_admin import (
    menu_admin,
    menu_admin_attendance,
    menu_admin_courses,
    menu_admin_groups,
    menu_admin_payments,
    menu_admin_reports,
    menu_admin_students,
    menu_admin_teachers,
)
from services.attendance_service import (
    show_attendance,
    student_attendance,
    take_attendance,
)
from services.course_service import (
    active_pause_course,
    add_course,
    delete_course,
    show_course,
    update_course,
)
from services.group_service import (
    active_pause_group,
    add_student_group,
    create_group,
    delete_group,
    remove_student,
    show_group,
    update_group,
)
from services.payment_service import (
    add_payment,
    delete_payments,
    history_payment,
    search_payments,
    unpaid_students,
)
from services.reports_service import (
    total_attendances,
    total_courses,
    total_groups,
    total_id,
    total_payments,
    total_students,
    total_teachers,
    total_users,
)
from services.student_service import (
    add_student,
    block_active_student,
    delete_student,
    search_student,
    show_students,
    update_student,
)
from services.teacher_service import (
    add_teacher,
    block_active_teacher,
    delete_teacher,
    search_teacher,
    show_teacher,
    update_teacher,
)
from services.user_service import profile
from utils.validator import input_text


def admin(user):
    while True:
        print(menu_admin())
        choice = input_text(">>> ")
        if choice == "0":
            print(f"The end | {user['name'].title()}{user['surname'].title()}")
            break
        elif choice == "1":
            print(profile(user))
        elif choice == "2":
            while True:
                print(menu_admin_students())
                choice = input_text(">>> ")
                if choice == "0":
                    break
                elif choice == "1":
                    print(add_student(user))
                elif choice == "2":
                    show_students(user)
                elif choice == "3":
                    search_student(user)
                elif choice == "4":
                    update_student(user)
                elif choice == "5":
                    delete_student(user)
                elif choice == "6":
                    block_active_student(user)

        elif choice == "3":
            while True:
                print(menu_admin_teachers())
                choice = input_text(">>> ")
                if choice == "0":
                    break
                elif choice == "1":
                    print(add_teacher(user))
                elif choice == "2":
                    show_teacher(user)
                elif choice == "3":
                    search_teacher(user)
                elif choice == "4":
                    update_teacher(user)
                elif choice == "5":
                    delete_teacher(user)
                elif choice == "6":
                    block_active_teacher(user)

        elif choice == "4":
            while True:
                print(menu_admin_courses())
                choice = input_text(">>> ")
                if choice == "0":
                    break
                elif choice == "1":
                    add_course(user)
                elif choice == "2":
                    show_course(user)
                elif choice == "3":
                    update_course(user)
                elif choice == "4":
                    delete_course(user)
                elif choice == "5":
                    active_pause_course(user)

        elif choice == "5":
            while True:
                print(menu_admin_groups())
                choice = input_text(">>> ")
                if choice == "0":
                    break
                elif choice == "1":
                    create_group(user)
                elif choice == "2":
                    show_group(user)
                elif choice == "3":
                    add_student_group(user)
                elif choice == "4":
                    remove_student(user)
                elif choice == "5":
                    update_group(user)
                elif choice == "6":
                    delete_group(user)
                elif choice == "7":
                    active_pause_group(user)

        elif choice == "6":
            while True:
                print(menu_admin_payments())
                choice = input_text(">>> ")
                if choice == "0":
                    break
                elif choice == "1":
                    add_payment(user)
                elif choice == "2":
                    history_payment(user)
                elif choice == "3":
                    unpaid_students(user)
                elif choice == "4":
                    delete_payments(user)
                elif choice == "5":
                    search_payments(user)

        elif choice == "7":
            while True:
                print(menu_admin_attendance())
                choice = input_text(">>> ")
                if choice == "0":
                    break
                elif choice == "1":
                    take_attendance(user)
                elif choice == "2":
                    show_attendance(user)
                elif choice == "3":
                    student_attendance(user)

        elif choice == "8":
            while True:
                print(menu_admin_reports())
                choice = input_text(">>> ")
                if choice == "0":
                    break
                elif choice == "1":
                    total_users(user)
                elif choice == "2":
                    total_students(user)
                elif choice == "3":
                    total_teachers(user)
                elif choice == "4":
                    total_groups(user)
                elif choice == "5":
                    total_courses(user)
                elif choice == "6":
                    total_attendances(user)
                elif choice == "7":
                    total_payments(user)
                elif choice == "8":
                    total_id(user)

        else:
            print("Xato. Noto'g'ri bo'lim.")
