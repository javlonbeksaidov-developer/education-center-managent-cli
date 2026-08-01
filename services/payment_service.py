from database.json_service import load, save
from models.payment import Payment
from utils.validator import add_payment_input

DATA_PAYMENTS = "data/payments.json"
DATA_STUDENTS = "data/students.json"
DATA_USERS = "data/users.json"

def add_payment(user):
    data_payments = load(DATA_PAYMENTS)
    data_students = load(DATA_STUDENTS)
    data_users = load(DATA_USERS)

    print("=== Add payment ===")
    student_id, amount, payment_date, payment_type, comment = add_payment_input()
    payment = Payment(student_id=student_id, amount=amount, payment_date=payment_date, payment_type=payment_type, comment=comment)
    data = payment.to_dict()
    data_payments.append(data)

    for i, data_student in enumerate(data_students):
        if student_id == data_student['id']:
            data_student['balance'] -= amount
            data_students[i] = data_student
            break

    for data_user in data_users:
        if student_id == data_user['id']:
            data_user['balance'] -= amount
            data_users[i] = data_user
            break

    save(DATA_PAYMENTS, data_payments)
    save(DATA_STUDENTS, data_students)
    save(DATA_USERS, data_users)


def history_payment(user):
    pass


def monthly_payment(user):
    pass


def unpaid_students(user):
    pass


def delete_payments(user):
    pass
