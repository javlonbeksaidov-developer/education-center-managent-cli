from models.user import User


class Teacher(User):
    def __init__(self, name, surname, username, phone, salary, speciality):
        super().__init__(name, surname, username, phone)
        self.salary = salary
        self.speciality = speciality
        self.role = "teacher"

    def to_dict(self):
        data = super().to_dict()

        data.update(
            {"role": self.role, "speciality": self.speciality, "salary": self.salary}
        )

        return data

    @classmethod
    def from_dict(cls, data):
        teacher = cls(
            name=data["name"],
            surname=data["surname"],
            username=data["username"],
            phone=data["phone"],
            salary=data["salary"],
            speciality=data["speciality"],
        )

        teacher.id = data["id"]
        teacher.password = data["password"]
        teacher.status = data["status"]
        teacher.created_at = data["created_at"]
        teacher.role = data["role"]

        return teacher

    def info(self):
        return f"Full name: {self.name.title()} {self.surname.title()}. Username: {self.username}. ID: {self.id}. Phone: +998{self.phone}. Speciality: {self.speciality}. Salary: {self.salary} so'm. Role: {self.role}, status: {self.status}. Created at: {self.created_at}"
