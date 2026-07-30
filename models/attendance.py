from datetime import datetime

from utils.generator import id_generator

NOW = datetime.now()  # noqa: DTZ005


class Attendance:
    def __init__(self, student_id, group_id, date, status):
        self.id = str(id_generator(10))
        self.student_id = student_id
        self.group_id = group_id
        self.date = date
        self.status = status
        self.created_at = NOW.date()

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "group_id": self.group_id,
            "date": self.date.isoformat(),
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        attendance = cls(
            student_id=data["student_id"],
            group_id=data["group_id"],
            date=data["date"],
            status=data["status"],
        )
        attendance.id = data["id"]
        attendance.created_at = data["created_at"]
        return attendance

    def info(self):
        return f"Attendance ID: {self.id}. Student ID: {self.student_id}. Group ID: {self.group_id}. Date: {self.date}. Status: {self.status}"
