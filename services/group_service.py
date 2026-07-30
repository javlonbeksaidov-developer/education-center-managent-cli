from database.json_service import load, save
from models.group import Group
from models.student import Student
from utils.validator import add_group_input, search_input

DATA_GROUPS = "data/groups.json"
DATA_USERS = "data/users.json"
DATA_TEACHERS = "data/teachers.json"
DATA_STUDENTS = "data/students.json"


def create_group(user):
    data_groups = load(DATA_GROUPS)
    print("=== Create group ===\n")
    name, start, stop, course_id, teacher_id = add_group_input()
    group = Group(
        name=name, start=start, stop=stop, course_id=course_id, teacher_id=teacher_id
    )
    data = group.to_dict()
    data_groups.append(data)
    save(DATA_GROUPS, data_groups)


def show_group(user):
    data_groups = load(DATA_GROUPS)
    print("=== Show groups ===\n")
    for i, data_group in enumerate(data_groups, start=1):
        group = Group.from_dict(data_group)
        print(f"{i}. {group.info()}")


def add_student(user):
    data_groups = load(DATA_GROUPS)
    data_users = load(DATA_USERS)
    data_students = load(DATA_STUDENTS)
    print("=== Add students for group ===\n")

    search = search_input("Group ID: ")
    for i, data_group in enumerate(data_groups):
        if search == data_group["id"]:
            group = Group.from_dict(data_group)
            print(group.info())

            choise = search_input("Add student (yes/no): ").lower()
            if choise == "yes":
                search = search_input("Student ID: ")
                for j, data_student in enumerate(data_students):
                    if search == data_student["id"]:
                        student = Student.from_dict(data_student)
                        print(student.info())

                        choise = search_input("Add student (yes/no): ").lower()
                        if choise == "yes":
                            data_group["students"].append(data_student["id"])
                            data_student["group_id"].append(data_group["course_id"])

                            data_groups[i] = data_group
                            data_students[j] = data_student

                            for data_user in data_users:
                                if data_student["id"] == data_user["id"]:
                                    data_user["group_id"].append(
                                        data_group["course_id"]
                                    )

                            save(DATA_GROUPS, data_groups)
                            save(DATA_USERS, data_users)
                            save(DATA_STUDENTS, data_students)

                            print(
                                f"{data_student['username']} {data_group['name']} guruhiga qo'shildi."
                            )
                            return
            else:
                print("Bekor qilindi.")

    print("Bunday guruh mavjud emas.")


def remove_student(user):
    data_groups = load(DATA_GROUPS)
    data_users = load(DATA_USERS)
    data_students = load(DATA_STUDENTS)
    print("=== Remove students for group ===\n")

    search = search_input("Group ID: ")
    for i, data_group in enumerate(data_groups):
        if search == data_group["id"]:
            group = Group.from_dict(data_group)
            print(group.info())

            choise = search_input("Remove student (yes/no): ").lower()
            if choise == "yes":
                search = search_input("Student ID: ")
                for j, data_student in enumerate(data_students):
                    if search == data_student["id"]:
                        student = Student.from_dict(data_student)
                        print(student.info())

                        choise = search_input("Remove student (yes/no): ").lower()
                        if choise == "yes":
                            data_group["students"].remove(data_student["id"])
                            data_student["group_id"].remove(data_group["course_id"])

                            data_groups[i] = data_group
                            data_students[j] = data_student

                            for data_user in data_users:
                                if data_student["id"] == data_user["id"]:
                                    data_user["group_id"].remove(
                                        data_group["course_id"]
                                    )

                            save(DATA_GROUPS, data_groups)
                            save(DATA_USERS, data_users)
                            save(DATA_STUDENTS, data_students)

                            print(
                                f"{data_student['username']} {data_group['name']} guruhidan o'chirildi."
                            )
                            return

            else:
                print("Bekor qilindi.")

    print("Bunday guruh mavjud emas.")


def update_group(user):
    data_groups = load(DATA_GROUPS)
    print("=== Update group ===\n")

    search = search_input("Group ID: ")
    for i, data_group in enumerate(data_groups):
        if search == data_group["id"]:
            group = Group.from_dict(data_group)
            print(group.info())

            choise = search_input("Update Group (yes/no): ").lower()
            if choise == "yes":
                name, start, stop, course_id, teacher_id = add_group_input()
                data_group["name"] = name
                data_group["start_date"] = start.isoformat()
                data_group["stop_date"] = stop.isoformat()
                data_group["course_id"] = course_id
                data_group["teacher_id"] = teacher_id
                data_groups[i] = data_group

            save(DATA_GROUPS, data_groups)
            print(f"Update ID: {data_group['id']} group.")


def delete_group(user):
    data_groups = load(DATA_GROUPS)
    print("=== Delete Group ===\n")

    search = search_input("Group ID: ")
    for data_group in data_groups:
        if search == data_group['id']:
            group = Group.from_dict(data_group)
            print(group.info())

            choise = search_input("Delete Group (yes/no): ").lower()
            if choise == "yes":
                data_groups.remove(data_group)

            save(DATA_GROUPS, data_groups)
            print(f"Delete ID: {data_group['id']} group.")



def active_pause_group(user):
    data_groups = load(DATA_GROUPS)
    print("=== Active / Pause Group ===\n")

    search = search_input("Group ID: ")
    for i, data_group in enumerate(data_groups):
        if search == data_group['id']:
            group = Group.from_dict(data_group)
            print(group.info())

            if data_group['status'] == "active":
                text = "block"
            else:
                text = "active"


            choise = search_input(f"{data_group['name']} guruhini ({text}) qilasizmi? (yes/no): ").lower()
            if choise == "yes":
                data_group['status'] = text
                data_groups[i] = data_group

            save(DATA_GROUPS, data_groups)
            print(f"{data_group['name']} {text} qilindi.")
