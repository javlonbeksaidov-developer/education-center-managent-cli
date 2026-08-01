from datetime import datetime

from utils.generator import id_generator

NOW = datetime.now()  # noqa: DTZ005


class Payment:
    def __init__(self, student_id, amount, payment_date, payment_type, comment):
        self.id = str(id_generator(10))
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_type = payment_type
        self.comment = comment
        self.created_at = NOW.date()

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "amount": self.amount,
            "payment_date": self.payment_date.isoformat(),
            "payment_type": self.payment_type,
            "comment": self.comment,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        payment = cls(
            student_id=data["student_id"],
            amount=data["amount"],
            payment_date=data["payment_date"],
            payment_type=data["payment_type"],
            comment=data["comment"],
        )
        payment.id = data["id"]
        payment.created_at = data["created_at"]
        return payment

    def info(self):
        return f"Payment ID: {self.id}. Student ID: {self.student_id}. Amount: {self.amount}. Payment date: {self.payment_date}. Payment type: {self.payment_type}. Comment: {self.comment}."
