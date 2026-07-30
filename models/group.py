from datetime import datetime

from utils.generator import id_generator

NOW = datetime.now()  # noqa: DTZ005


class Group:
    def __init__(self, name, start, stop, course_id, teacher_id):
        self.id = str(id_generator(3))
        self.name = name
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.students = []
        self.start_date = start
        self.stop_date = stop
        self.status = "active"
        self.created_at = NOW.date()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "course_id": self.course_id,
            "teacher_id": self.teacher_id,
            "students": self.students,
            "start_date": self.start_date.isoformat(),
            "stop_date": self.stop_date.isoformat(),
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        group = cls(
            name=data["name"],
            start=data["start_date"],
            stop=data["stop_date"],
            course_id=data["course_id"],
            teacher_id=data["teacher_id"],
        )
        group.id = data["id"]
        group.name = data["name"]
        group.students = data["students"]
        group.created_at = data["created_at"]
        return group

    def info(self):
        return f"ID: {self.id}. Group name: {self.name}. Date: ({self.start_date} - {self.stop_date}). Status: {self.status}. Course ID: {self.course_id}. Teacher ID: {self.teacher_id}. Students count: {len(self.students)}."
