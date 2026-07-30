from datetime import datetime

from utils.generator import id_generator

NOW = datetime.now()  # noqa: DTZ005


class Course:
    def __init__(self, name, price, description):
        self.id = str(id_generator(3))
        self.name = name
        self.price = price
        self.description = description
        self.duration = 90
        self.status = "active"
        self.created_at = NOW.date()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "duration": self.duration,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        course = cls(
            name=data["name"], price=data["price"], description=data["description"]
        )

        course.id = data["id"]
        course.duration = data["duration"]
        course.status = data["status"]
        course.created_at = datetime.fromisoformat(data["created_at"])

        return course

    def info(self):
        return f"Course name: {self.name}. ID: {self.id}. Price: {self.price} so'm. Description: {self.description}. Status: {self.status}."
