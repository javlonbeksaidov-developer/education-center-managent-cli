from datetime import datetime

from utils.generator import id_generator

NOW = datetime.now()  # noqa: DTZ005


class Attendance:
    def __init__(self, group_id):
        self.id = str(id_generator(10))
        self.student_id = []
        self.group_id = group_id
        self.created_at = NOW.date()

    def to_dict(self):
        return {
            "attendance id": self.id,
            "student_id": self.student_id,
            "group_id": self.group_id,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        attendance = cls(
            group_id=data["group_id"],
        )
        attendance.student_id = data["student_id"]
        attendance.id = data["id"]
        attendance.created_at = data["created_at"]
        return attendance

    def info(self):
        return f"Attendance ID: {self.id}. Student IDs: {self.student_id}. Group ID: {self.group_id}. Date: {self.created_at}."
