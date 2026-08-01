from database.json_service import load, save
from models.payment import Payment
from models.student import Student
from utils.validator import add_payment_input, search_input

DATA_PAYMENTS = "data/payments.json"
DATA_STUDENTS = "data/students.json"
DATA_USERS = "data/users.json"


def add_payment(user):
    data_payments = load(DATA_PAYMENTS)
    data_students = load(DATA_STUDENTS)
    data_users = load(DATA_USERS)

    print("=== Add payment ===\n")
    student_id, amount, payment_date, payment_type, comment = add_payment_input()
    payment = Payment(
        student_id=student_id,
        amount=amount,
        payment_date=payment_date,
        payment_type=payment_type,
        comment=comment,
    )
    data = payment.to_dict()
    data_payments.append(data)

    for i, data_student in enumerate(data_students):
        if student_id == data_student["id"]:
            data_student["balance"] -= amount
            data_students[i] = data_student
            break

    for j, data_user in enumerate(data_users):
        if student_id == data_user["id"]:
            data_user["balance"] -= amount
            data_users[j] = data_user
            break

    save(DATA_PAYMENTS, data_payments)
    save(DATA_STUDENTS, data_students)
    save(DATA_USERS, data_users)


def history_payment(user):
    data_payments = load(DATA_PAYMENTS)
    print("=== History payment ===\n")
    for i, data_payment in enumerate(data_payments, start=1):
        payment = Payment.from_dict(data_payment)
        print(f"{i}. {payment.info()}")


def unpaid_students(user):
    data_students = load(DATA_STUDENTS)
    print("=== Unpaid payment ===\n")
    for data_student in data_students:
        if data_student['balance'] < 0:
            student = Student.from_dict(data_student)
            print(student.info())


def delete_payments(user):
    data_payments = load(DATA_PAYMENTS)
    print("=== Delete payment ===\n")
    search = search_input("Payment ID: ")
    for data_payment in data_payments:
        if search == data_payment['id']:
            payment = Payment.from_dict(data_payment)
            print(f"{payment.info()}")

            choise = input("Delete payment (yes/no): ").lower()
            if choise == "yes":
                data_payments.remove(data_payment)

    save(DATA_PAYMENTS, data_payments)
    print(f"Delete payment ID: {data_payment['id']}.")

def search_payments(user):
    data_payments = load(DATA_PAYMENTS)
    print("=== Search payment ===\n")
    search = search_input("Payment ID or Student ID: ").lower()
    for data_payment in data_payments:
        if search == data_payment['id'] or search == data_payment['student_id']:
            payment = Payment.from_dict(data_payment)
            print(f"{payment.info()}")
