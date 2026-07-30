from database.json_service import load, save
from models.course import Course
from utils.validator import add_course_input, search_input

DATA_COURSES = "data/courses.json"


def add_course(user):
    data_courses = load(DATA_COURSES)
    name, price, description = add_course_input()
    course = Course(name=name, price=price, description=description)
    data = course.to_dict()
    data_courses.append(data)
    save(DATA_COURSES, data_courses)
    print(f"create {name} course.")


def show_course(user):
    data_courses = load(DATA_COURSES)
    for index, data_course in enumerate(data_courses, start=1):
        course = Course.from_dict(data_course)
        print(f"{index}. {course.info()}")


def update_course(user):
    data_courses = load(DATA_COURSES)
    search = search_input("ID: ")
    for i, data_course in enumerate(data_courses):
        if search == data_course["id"]:
            course = Course.from_dict(data_course)
            print(course.info())

            choise = search_input("\nUpdate course (yes/no): ").lower()
            if choise == "yes":
                name, price, description = add_course_input()
                data_course["name"] = name
                data_course["price"] = price
                data_course["description"] = description
                data_courses[i] = data_course

            save(DATA_COURSES, data_courses)
            print("Succes, Update course.")


def delete_course(user):
    data_courses = load(DATA_COURSES)
    search = search_input("ID: ")
    for data_course in data_courses:
        if search == data_course["id"]:
            course = Course.from_dict(data_course)
            print(course.info())

            choise = search_input("\nDelete course (yes/no): ").lower()
            if choise == "yes":
                data_courses.remove(data_course)

        save(DATA_COURSES, data_courses)
        print(f"Delete {data_course['name']} course.")


def active_pause_course(user):
    data_courses = load(DATA_COURSES)
    search = search_input("ID: ")
    for i, data_course in enumerate(data_courses):
        if search == data_course["id"]:
            course = Course.from_dict(data_course)
            print(course.info())

            if data_course["status"] == "active":
                text = "block"
            else:
                text = "active"

            choise = search_input(
                f"\n{data_course['name']} ({text}) qilasizmi? (yes/no): "
            ).lower()
            if choise == "yes":
                data_course["status"] = text
                data_courses[i] = data_course

            save(DATA_COURSES, data_courses)
            print(f"\n{data_course['name']} ({text}) qilindi.")
