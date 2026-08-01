from database.json_service import load, save
from models.teacher import Teacher
from utils.validator import add_teacher_input, add_user_input, search_input

DATA_USERS = "data/users.json"
DATA_TEACHERS = "data/teachers.json"


def add_teacher(user):
    data_users = load(DATA_USERS)
    data_teachers = load(DATA_TEACHERS)
    name, surname, username, phone = add_user_input()
    salary, speciality = add_teacher_input()

    teacher = Teacher(
        name=name,
        surname=surname,
        username=username,
        phone=phone,
        salary=salary,
        speciality=speciality,
    )

    add_teacher = teacher.to_dict()
    data_users.append(add_teacher)
    data_teachers.append(add_teacher)

    save(DATA_USERS, data_users)
    save(DATA_TEACHERS, data_teachers)
    return f"{name.title()} {surname.title()} o'quv markazga qo'shildi."


def show_teacher(user):
    data_teachers = load(DATA_TEACHERS)
    print("=== Show Teacher ===\n")
    for index, data_teacher in enumerate(data_teachers, start=1):
        teacher = Teacher.from_dict(data_teacher)
        print(f"{index}. {teacher.info()}")


def search_teacher(user):
    data_teachers = load(DATA_TEACHERS)
    print("=== Search Teacher ===\n")
    search = search_input("ID or username: ")
    for data_teacher in data_teachers:
        if search == data_teacher["id"] or search == data_teacher["username"]:
            teacher = Teacher.from_dict(data_teacher)
            print(teacher.info())


def update_teacher(user):
    data_users = load(DATA_USERS)
    data_teachers = load(DATA_TEACHERS)
    print("=== Update Teacher ===\n")
    search = search_input("ID or username: ")
    for i, data_teacher in enumerate(data_teachers):
        if search == data_teacher["id"] or search == data_teacher["username"]:
            teacher = Teacher.from_dict(data_teacher)
            print(teacher.info())

            choise = search_input("\nUpdate Teacher (yes/no): ")
            if choise == "yes":
                name, surname, username, phone = add_user_input()
                salary, speciality = add_teacher_input()

                data_teacher["name"] = name
                data_teacher["surname"] = surname
                data_teacher["username"] = username
                data_teacher["phone"] = phone
                data_teacher["salary"] = salary
                data_teacher["speciality"] = speciality

                data_teachers[i] = data_teacher

                for j, data_user in enumerate(data_users):
                    if data_teacher["id"] == data_user["id"]:
                        data_user["name"] = name
                        data_user["surname"] = surname
                        data_user["username"] = username
                        data_user["phone"] = phone
                        data_user["salary"] = salary
                        data_user["speciality"] = speciality

                        data_users[j] = data_user
                        break

                save(DATA_USERS, data_users)
                save(DATA_TEACHERS, data_teachers)

                print(f"{username} ma'lumotlari yangilandi.")
                return


def delete_teacher(user):
    data_users = load(DATA_USERS)
    data_teachers = load(DATA_TEACHERS)
    print("=== Delete Teacher ===\n")
    search = search_input("ID or username: ")

    for data_teacher in data_teachers:
        if search == data_teacher["id"] or search == data_teacher["username"]:
            teacher = Teacher.from_dict(data_teacher)
            print(teacher.info())

            choise = search_input("\nDelete Teacher (yes/no): ").lower()
            if choise == "yes":
                data_teachers.remove(data_teacher)

                for data_user in data_users:
                    if data_user["id"] == data_teacher["id"]:
                        data_users.remove(data_user)
                        break

            save(DATA_USERS, data_users)
            save(DATA_TEACHERS, data_teachers)

            print(f"{data_teacher['username']} o'chirildi.")
            return


def block_active_teacher(user):
    data_users = load(DATA_USERS)
    data_teachers = load(DATA_TEACHERS)
    print("=== Block or Active Teacher ===\n")
    search = search_input("ID or username: ")

    for i, data_teacher in enumerate(data_teachers):
        if search == data_teacher["id"] or search == data_teacher["username"]:
            teacher = Teacher.from_dict(data_teacher)
            print(teacher.info())

            if data_teacher["status"] == "active":
                text = "block"
            else:
                text = "active"

            choise = search_input(
                f"\n{data_teacher['username']} ({text}) qilasizmi? (yes/no): "
            ).lower()
            if choise == "yes":
                data_teacher["status"] = text
                data_teachers[i] = data_teacher

                for j, data_user in enumerate(data_users):
                    if data_user["id"] == data_teacher["id"]:
                        data_user["status"] = text
                        data_users[j] = data_user
                        break

            save(DATA_USERS, data_users)
            save(DATA_TEACHERS, data_teachers)

            print(f"{data_teacher['username']} ({text}) qilindi.")
