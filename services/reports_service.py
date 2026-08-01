from database.json_service import load

DATA_USERS = "data/users.json"
DATA_STUDENTS = "data/students.json"
DATA_TEACHERS = "data/teachers.json"
DATA_GROUPS = "data/groups.json"
DATA_COURSES = "data/courses.json"
DATA_ATTENDANCES = "data/attendances.json"
DATA_PAYMENTS = "data/payments.json"
DATA_IDS = "data/ids.json"


def total_users(user):
    data_users = load(DATA_USERS)
    users_count = 0
    admin = 0
    student = 0
    teacher = 0
    active = 0
    block = 0
    for data_user in data_users:
        if data_user["id"]:
            users_count += 1

        if data_user["role"] == "admin":
            admin += 1
        elif data_user["role"] == "student":
            student += 1
        elif data_user["role"] == "teacher":
            teacher += 1

        if data_user["status"] == "active":
            active += 1
        elif data_user["status"] == "block":
            block += 1

    print(f"""
======== Total Users Statistic ========

1. Total users count: -> {users_count}
2. Total admin count: -> {admin}
3. Total student count: -> {student}
4. Total teacher count: -> {teacher}
5. Total active users count: -> {active}
6. Total block users count: -> {block}
""")



def total_students(user):
    data_students = load(DATA_STUDENTS)
    students_count = 0
    active = 0
    block = 0
    balance_plus = 0
    balance_0 = 0
    balance_minus = 0
    for data_student in data_students:
        if data_student["id"]:
            students_count += 1

        if data_student["status"] == "active":
            active += 1
        elif data_student["status"] == "block":
            block += 1

        if data_student["balance"] > 0:
            balance_plus += 1
        elif data_student["balance"] < 0:
            balance_minus += 1
        else:
            balance_0 += 1

    print(f"""
======== Total Students Statistic ========

1. Total students count: -> {students_count}
2. Student (balance > 0) count: -> {balance_plus}
3. Student (balance = 0) count: -> {balance_0}
4. Student (balance < 0) count: -> {balance_minus}
5. Total active students count: -> {active}
6. Total block students count: -> {block}
""")

def total_teachers(user):
    data_teachers = load(DATA_TEACHERS)
    teachers_count = 0
    active = 0
    block = 0
    for data_teacher in data_teachers:
        if data_teacher["id"]:
            teachers_count += 1

        if data_teacher["status"] == "active":
            active += 1
        elif data_teacher["status"] == "block":
            block += 1

    print(f"""
======== Total Teachers Statistic ========

1. Total teachers count: -> {teachers_count}
2. Total active teachers count: -> {active}
3. Total block teachers count: -> {block}
""")


def total_groups(user):
    data_groups = load(DATA_GROUPS)
    groups_count = 0
    active = 0
    block = 0
    students = 0
    for data_group in data_groups:
        if data_group["id"]:
            groups_count += 1

        if data_group["status"] == "active":
            active += 1
        elif data_group["status"] == "block":
            block += 1

        if data_group["students"]:
            students += len(data_group["students"])

    print(f"""
======== Total Groups Statistic ========

1. Total groups count: -> {groups_count}
2. Total active groups count: -> {active}
3. Total block groups count: -> {block}
4. Total group students count: -> {students}
""")


def total_courses(user):
    data_courses = load(DATA_COURSES)
    courses_count = 0
    active = 0
    block = 0
    for data_course in data_courses:
        if data_course["id"]:
            courses_count += 1

        if data_course["status"] == "active":
            active += 1
        elif data_course["status"] == "block":
            block += 1

    print(f"""
======== Total Courses Statistic ========

1. Total courses count: -> {courses_count}
2. Total active courses count: -> {active}
3. Total block courses count: -> {block}
""")


def total_attendances(user):
    data_attendances = load(DATA_ATTENDANCES)
    attendances_count = 0
    students = 0
    for data_attendance in data_attendances:
        if data_attendance["attendance id"]:
            attendances_count += 1

        if data_attendance["student_id"]:
            for attendance in data_attendance["student_id"]:
                students += len(attendance)

    print(f"""
======== Total Attendances Statistic ========

1. Total attendances count: -> {attendances_count}
2. Total attendance students count: -> {students}
""")


def total_payments(user):
    data_payments = load(DATA_PAYMENTS)
    payments_count = 0
    amount = 0
    for data_payment in data_payments:
        if data_payment["id"]:
            payments_count += 1

        if data_payment["amount"]:
            amount += data_payment["amount"]

    print(f"""
======== Total Groups Statistic ========

1. Total payments count: -> {payments_count}
2. Total payments amount: -> {amount}
""")


def total_id(user):
    data_ids = load(DATA_IDS)
    ids = 0
    for data_id in data_ids:
        if data_id["id"]:
            ids += 1

    print(f"""
======== Total IDs Statistic ========

1. Total IDs count: -> {ids}
""")
